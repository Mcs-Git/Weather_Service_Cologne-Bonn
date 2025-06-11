import socket     # Für Netzwerk-Kommunikation (TCP/IP)
import ast        # Für sichere Umwandlung von Zeichenketten in Python-Objekte (z.B. Tupel)

# Funktion zum Einlesen und Parsen der Wetterdaten aus einer CSV-Datei
def load_data(filename):
    samples = []  # Liste zur Speicherung der eingelesenen Datensätze

    with open(filename) as file:
        header = file.readline()  # Erste Zeile (Spaltenüberschriften) wird ignoriert
        for line in file:
            # Zerlegt die Zeile anhand von Kommas und konvertiert die Werte in passende Datentypen
            year, month, day, tavg, tmin, tmax, prcp, snow, wdir, wspd, wpgt, pres, tsun = line.strip().split(',')
            samples.append(
                (int(year), int(month), int(day),           # Datum
                 float(tavg), float(tmin), float(tmax),     # Temperaturen
                 float(prcp), float(snow),                  # Niederschlag und Schnee
                 int(wdir), float(wspd), float(wpgt),       # Windrichtung und -geschwindigkeit
                 float(pres), int(tsun))                    # Luftdruck und Sonnenscheindauer
            )

    # Überschrift für tabellarische Vorschau
    print(" Temp (min/o/max)    | Niederschlag  | Luftdruck  | Sonne    | Datum")
    print("---------------------+---------------+------------+----------+-----------")

    # Ausgabe der Daten in formatiertem Layout
    for s in samples:
        year, month, day, tavg, tmin, tmax, prcp, snow, wdir, wspd, wpgt, pres, tsun = s
        print(f"{tmin:4.1f} C {tavg:4.1f} C {tmax:4.1f} C | {prcp:4.1f} mm {snow:2.0f} mm | {pres:6.1f} hPa | {tsun:4d} min | {day:02d}.{month:02d}.{year:04d}")

    print(len(samples), "Tageswerte eingelesen.")
    return samples  # Rückgabe der Liste aller Wetterdaten

# Funktion, die den Server startet und eine Client-Anfrage verarbeitet
def server_socket(samples_list):
    HOST = "127.0.0.1"  # Lokale IP-Adresse
    PORT = 8080         # Port, auf dem der Server lauscht

    # Erzeugt einen TCP-Socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))  # Verknüpft IP und Port
    server.listen()            # Wartet auf eingehende Verbindung

    print(f"Server läuft auf {HOST}:{PORT}")
    try:
        while True:
            client_socket, client_address = server.accept()  # Nimmt erste Verbindung an
            print(f"Neue Verbindung von {client_address}")

            with client_socket:
                request = client_socket.recv(1024)  # Empfang der Anfrage (max. 1024 Bytes)
                if not request:
                    print("Verbindung geschlossen.")
                    continue # Zur nächsten Verbindung

                try:
                    # Anfrage (Bytes) zu String dekodieren und in Tupel umwandeln
                    request_str  = request.decode("utf-8")
                    request_tuple = ast.literal_eval(request_str)

                    # Prüfen, ob Anfrage ein Tupel mit genau 3 Elementen ist (Jahr, Monat, Tag)
                    assert isinstance(request_tuple, tuple) and len(request_tuple) == 3, "Ungültige Anfrage"
                    print(f"Empfangen: {request_tuple}")

                    # Wetterdaten suchen
                    result = search(samples_list, request_tuple)

                    # Antwort als String kodieren und senden
                    response = str(result).encode("utf-8")
                    client_socket.send(response)

                except Exception as e:
                    # Bei Fehlern eine Fehlermeldung senden
                    error_msg = "Ungültige Anfrage"
                    client_socket.send(error_msg.encode("utf-8"))
                    print(f"Fehler bei der Anfrage: {e}")
                    continue # Verbindung wird geschlossen, nächster Client
    except KeyboardInterrupt:
        print("\nServer wird beendet.")
        server.close()

# Funktion, die das passende Datum sucht und relevante Wetterwerte zurückgibt
def search(arr, req):
    for entry in arr:
        try:
            if entry[0] == req[0] and entry[1] == req[1] and entry[2] == req[2]:
                # Rückgabe: , Minimum (tmin), Durchschnittstemp (tavg), Maximum (tmax), Regen (prcp)
                return entry[4], entry[3], entry[5], entry[6]
        except (ValueError, IndexError):
            continue
    return "Keinen Eintrag gefunden."  # Falls kein passender Eintrag gefunden wird



# Hauptprogramm: Datei laden und Server starten
if __name__ == '__main__':
    input_file = "airport-cgn.csv"  # Pfad zur CSV-Datei
    samples = load_data(input_file)  # Wetterdaten einlesen
    server_socket(samples)           # Server mit geladenen Daten starten
