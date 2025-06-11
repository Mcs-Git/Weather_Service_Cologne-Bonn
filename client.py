import socket                     # Für die Netzwerk-Kommunikation mit dem Server
import time                       # Für Pausen (z.B. bei Fehlermeldungen)
from datetime import datetime     # Für Datumsprüfung
import re                         # Für Zerlegen des Datums per regulärem Ausdruck
import ast                        # Um Strings sicher in Python-Objekte (z.B. Tupel) umzuwandeln

# Serverkonfiguration
HOST = "127.0.0.1"                # Lokaler Host (localhost)
PORT = 8080                       # Port, auf dem der Server lauscht

# Funktion zum Versenden einer Anfrage an den Server
def client_socket(req):
    try:
        # Erstellt eine TCP-Verbindung und sendet den Anfrage-String
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            client.send(req.encode("utf-8"))              # Anfrage codieren und senden
            response = client.recv(1024).decode("utf-8")  # Antwort empfangen und dekodieren
            return response
    except ConnectionRefusedError:
        raise # Fehler wird im Hauptprogramm behandelt

# Prüft, ob das Datum einem gültigen Format entspricht
def date_validity(date):
    valid_formats = ["%d-%m-%Y", "%d/%m/%Y", "%d.%m.%Y"]
    for fmt in valid_formats:
        try:
            datetime.strptime(date, fmt)  # Versucht, das Datum mit dem Format zu parsen
            return True
        except ValueError:
            continue
    return False

# Prüft, ob die Eingabe leer oder das Format ungültig ist
def dateformat_test(date):
    if not date.strip():  # Leer oder nur Leerzeichen?
        print("Ein leerer Eintrag ist nicht erlaubt.")
        return False
    if date_validity(date):
        return True
    print("Bitte gib ein gültiges Datumsformat ein (z.B. 31-12-2021, 31/12/2021 oder 31.12.2021).")
    time.sleep(2)
    return False

# Hauptprogramm
if __name__ == '__main__':
    print("\n********** Willkommen beim Wetterdienst des Flughafens Köln/Bonn (2020–2024) **********\n")

    # Wiederhole die Eingabeaufforderung bis ein gültiges Datum eingegeben wurde
    while True:
        requested_day = input("Für welches Datum sollen die Wetterdaten angezeigt werden? ").strip()
        if dateformat_test(requested_day):
            break

    # Datum in Tupel (Jahr, Monat, Tag) umwandeln
    try:
        date_parts = tuple(map(int, re.split(r"[-/.]", requested_day)))[::-1]
        request = str(date_parts)
    except ValueError:
        print("Fehler beim Umwandeln des Datums.")
        exit(1)

    print("Verbindung zum Server wird hergestellt...\n")
    time.sleep(2)

    try:
        # Anfrage senden, Antwort parsen und in Float-Werte umwandeln
        response_raw = client_socket(request)
        response_tuple  = ast.literal_eval(response_raw)
        response = tuple(map(float, response_tuple ))

        print(f"\nHier sind die Wetterdaten des {requested_day}:")
        print(" Temp (min/o/max)    | Regen")
        print("---------------------+---------------")

        # Formatierte Ausgabe der Wetterdaten
        print(f"{response[0]:4.1f} C {response[1]:4.1f} C {response[2]:4.1f} C | {response[3]:4.1f} mm\n")

    except (SyntaxError, ValueError, IndexError):  # Fehler bei ungültiger oder leerer Antwort
        print(f"\nHier sind die Wetterdaten des {requested_day}:")
        print(" Temp (min/o/max)    | Regen")
        print("---------------------+---------------")
        print(" -- C  -- C  -- C     |  -- mm")
        print("\nKein Eintrag gefunden.")
        print("Bitte beachten Sie: Die Wetterdaten sind nur im Zeitraum 2020–2024 verfügbar.\n")

    except ConnectionRefusedError: # Verbindung zum Server fehlgeschlagen
        print("\nDer Server ist momentan nicht erreichbar.")
        print("Bitte versuchen Sie es später erneut.\n")
        time.sleep(2)
