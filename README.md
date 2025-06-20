# Weather_Service_Cologne-Bonn
# Dokumentation – Wetterdienst Köln/Bonn (2020–2024)

## **Überblick**

Dieses Projekt besteht aus einem **dreiteiligen Python-System** zur Analyse, Bereitstellung und Visualisierung von Wetterdaten. Die Hauptkomponenten sind:

1. **Servermodul**: Liest lokale **CSV-Datei** und beantwortet Anfragen.
2. **Clientmodul**: Stellt **Anfragen** an den Server.
3. **Diagrammmodul**: Zeigt Langzeittrends mithilfe von **Meteostat-API** an.


## **Modul 1**: **Servermodul (CSV + Socket)**

### **Datei**: `server.py`

### **Funktionen**:

* **load_data(filename)**: Liest die Wetterdaten aus einer CSV-Datei ein, wandelt sie in strukturierte Tupel um und zeigt eine Vorschau.
* **server_socket(samples_list)**: Startet einen TCP/IP-Server, verarbeitet Client-Anfragen, sucht nach passenden Wetterdaten und sendet passende Ergebnisse zurück.
* **search(arr, req**): Durchsucht die Datenliste nach einem bestimmten Datum und gibt Temperatur- sowie Regenswerte zurück.

### Eingabedaten:

* **CSV-Datei**: **airport-cgn.csv** mit Wetterdaten von **2020** bis **2024**.

### Ausgabe:

* Socket-Antwort mit **Wetterinformationen**  zum **angefragten Datum**.



## **Modul 2**: **Clientmodul**

### **Datei**: `client.py`

### **Funktionen**:

* **client_socket(req)**: Baut eine Verbindung zum Server auf, sendet das Datum und empfängt die Wetterdaten.
* **date_validity(date)**: Überprüft Format und Gültigkeit des eingegebenen Datums.
* **dateformat_test(date)**: Verhindert leere oder ungültige Eingaben.

### Benutzerinteraktion:

* Der Benutzer gibt ein Datum ein (z. B. 31.12.2021).
* Der Client sendet die Anfrage an den Server.
* Die Antwort wird formatiert angezeigt.

### Fehlerbehandlung:

* Ungültige Datumsformate
* Verbindungsprobleme
* Keine Daten zum eingegebenen Datum vorhanden



## Modul 3: **Diagrammmodul  (Meteostat)**

### **Datei**: `diagram.py`

### **Funktionen**:

* **plot_rainfall(year, data)**: Erstellt ein Balkendiagramm der monatlichen Regenmengen.
* **plot_temperature(year, data)**: Erstellt ein Liniendiagramm für min/avg/max-Temperatur pro Monat.
* **plot_pressure_and_precipitation(year, data)**: Streudiagramm für Luftdruck und Gesamtniederschlag.
* **year_validity(year)**: Überprüft, ob das Jahr im zulässigen Bereich (1931–2025) liegt.

### **Datenquelle**:

* Echtzeitdaten via **Meteostat API** , Station: **Köln/Bonn** (ID: **10513**)

### **Visualisierungen**:

1. **Monatlicher Niederschlag**
2. **Temperaturverlauf im Jahresverlauf**
3. **Tagesbasierte Luftdruck und Niederschlagsdaten**


## Systemanforderungen

| Komponente          | Bibliotheken                                        |
| ------------------- | --------------------------------------------------- |
| Allgemein           | **socket**, **datetime**, **time**, **ast**, **re** |
| Visualisierung      | **matplotlib**, **pandas**, **meteostat**           |


## Beispiel-Workflow

1. Der Benutzer startet `server.py` (Server lauscht auf Port **8080**).
2. Danach wird `client.py` gestartet, und **z. B.** mit Eingabe 25.07.2023.
3. Der Client sendet **(2023, 7, 25)** an den Server.
4. Der Server antwortet mit: **(min, avg, max, regen)**
5. Die Daten werden formatiert am Client angezeigt.
   

Optional kann `diagram.py` gestartet werden, um z. B. das Jahr 2023 grafisch auszuwerten.


## Benutzerhandbuch

### 1. **Server** (`server.py`)

- **Start**: Beim Starten lädt der Server automatisch **airport-cgn.csv**.

    ![](https://codi.ide3.de/uploads/52aaa6bf-6a00-4032-95ab-891c0953f78d.png)

- **Funktion**: Wartet auf Anfragen und liefert Wetterdaten zum angefragten Datum zurück.
- **Anfrageformat**: Ein **Tupel** im Format **(Jahr, Monat, Tag)**.

    ![](https://codi.ide3.de/uploads/5405d78e-d576-4452-8dbf-be5b21173fe8.png)

- **Antwort**: Temperaturwerte **(min, avg, max)** und **Regensmenge**.


### 2. **Client** (`client.py`)

- **Start**:  Fragt den Benutzer nach einem Datum.

    ![](https://codi.ide3.de/uploads/d9c17790-d959-49d8-87e6-ff029a4e7577.png)

- **Unterstützte Formate**: **31-12-2021**, **31/12/2021** oder **31.12.2021**.
 
    ![](https://codi.ide3.de/uploads/7aefc38f-1b47-4ea5-ad76-3d3a327ea845.png)

- **Ausgabe**: Tabellarische Darstellung der Wetterdaten oder Fehlermeldung bei fehlenden Einträgen.


    ![](https://codi.ide3.de/uploads/d5792feb-8f12-4f16-81a9-43046ca522e0.png)

    ![](https://codi.ide3.de/uploads/25047da5-a343-41b6-8e4b-fa0e3c6387f9.png)


### 3. **Diagramme** (`diagram.py`)

- **Start**: Führt eine Jahresabfrage durch.
 
    ![](https://codi.ide3.de/uploads/2ea653eb-0bea-4957-bc65-9011739fb465.png)

- **Datenquelle**: Automatischer Abruf via  **Meteostat**.

- **Diagramme**:
     - **Monatliche Regenmengen** (***Balkendiagramm***)
     
        ![](https://codi.ide3.de/uploads/698d2d85-9e45-4da3-96ee-ef0c918e913f.png)

    - **Monatliche Temperaturentwicklung** (***Liniendiagramm***)
     
        ![](https://codi.ide3.de/uploads/df5e10d7-33ce-44cd-b94b-3f69619fc830.png)
        
    - **Tagliche Luftdruck- und Niederschlagsdaten** (***Streudiagramm***)

        ![](https://codi.ide3.de/uploads/0c0b0a69-0374-4787-b651-dc2b6618ec1c.png)
        
        - Detailansicht: **Luftdruckverlauf**

        
            ![](https://codi.ide3.de/uploads/a333f3b0-ab19-4efd-911f-40122fdcc6e5.png)

        
        - Detailansicht: **Niederschlagsverlauf**

            ![](https://codi.ide3.de/uploads/c6b10cb3-caa3-4286-b478-bb7da7225a42.png)


- **Nutzung**: Nach Auswahl eines Jahres werden die Diagramme automatisch angezeigt.

### **Hinweise**:

- Die Programme verwenden sowohl **lokale CSV-Daten** als auch **Online-Daten** (**Meteostat**).

- Eine funktionierende **Internetverbindung** ist für **diagram\.py** **erforderlich**.

## Fazit

Das Projekt ermöglicht:

* Wetterabfragen über ein **Client-Server-Modell**

* **Grafische** **Jahresanalysen** mit **Echtzeitdaten**

* Eine sinnvolle Kombination aus **lokalen Datensätzen** und **externer API-Anbindung**


## Projektquellcode

`server.py` :
```#
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
    input_file = "airport-cgn.csv"   # Pfad zur CSV-Datei
    samples = load_data(input_file)  # Wetterdaten einlesen
    server_socket(samples)           # Server mit geladenen Daten starten

```

`client.py` : 

```#
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

```

`diagram.py` : 

```#
import time
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from meteostat import Daily


# Funktion: Zeigt die monatliche Regenmenge für ein Jahr
def plot_rainfall(year, data):
    if data.empty:
        print(f"Keine Daten für das Jahr {year} vorhanden.")
        return

    # Gruppierung nach Monat, Summierung der Regenmenge
    monthly = data.groupby(data["time"].dt.month)["prcp"].sum().reindex(range(1, 13), fill_value=0)

    fig, ax = plt.subplots()
    ax.bar(monthly.index, monthly.values)
    ax.set_xlabel('Monat')
    ax.set_ylabel('Regenmenge (mm)')
    ax.set_title(f"Regenmenge im Jahr {year}")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'])
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


# Funktion: Zeigt monatliche Temperaturstatistiken (min/avg/max)
def plot_temperature(year, data):
    if data.empty:
        print(f"Keine Daten für das Jahr {year} vorhanden.")
        return

    monthly = data.groupby(data["time"].dt.month).agg({
        "tmin": "min",
        "tavg": "mean",
        "tmax": "max"
    }).reindex(range(1, 13))

    fig, ax = plt.subplots()
    ax.plot(monthly.index, monthly["tmax"], label="Maximalwerte", color="red")
    ax.plot(monthly.index, monthly["tavg"], label="Durchschnitt", color="orange")
    ax.plot(monthly.index, monthly["tmin"], label="Minimalwerte", color="blue")
    ax.set_xlabel('Monat')
    ax.set_ylabel('Temperatur (°C)')
    ax.set_title(f"Temperaturstatistik im Jahr {year}")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'])
    ax.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


# Funktion: Zeigt Luftdruck und gesamten Niederschlag (Regen + Schnee) pro Tag
def plot_pressure_and_precipitation(year, data):
    if data.empty:
        print(f"Keine Daten für das Jahr {year} vorhanden.")
        return


    # Gesamt-Niederschlag berechnen (Regen + Schnee)
    data_precipitation = data["prcp"] + data["snow"]

    fig, ax = plt.subplots()

    # Tagesbasierte Punktwolke: Luftdruck
    ax.scatter(data["time"], data["pres"], color="blue", label="Luftdruck (hPa)", alpha=0.6)

    # Tagesbasierte Punktwolke: Niederschlag
    ax.scatter(data["time"], data_precipitation, color="cyan", label="Niederschlag in mm", alpha = 0.6)

    ax.set_xlabel('Datum')
    ax.set_ylabel('Messwerte')
    ax.set_title(f"Luftdruck und Niederschlag im Jahr {year}")
    ax.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


# Gültigkeitsprüfung für das Jahr
def year_validity(year):
    if year < 1931 or year > 2025:
        print("Bitte beachten Sie: Die Wetterdaten sind nur im Zeitraum 1931–2025 verfügbar.")
        time.sleep(2)
        return False
    return True


# Hauptprogramm
if __name__ == '__main__':
    print("\n********** Willkommen beim Wetterdienst des Flughafens Köln/Bonn **********\n")

    # Benutzereingabe für Jahr
    while True:
        try:
            year = int(input("Bitte geben Sie das gewünschte Jahr ein: "))
            if year_validity(year):
                break
        except ValueError:
            print("Ungültige Eingabe. Bitte eine gültige Jahreszahl eingeben.")

    try:
        # Datenabruf mit Meteostat
        start = datetime(year, 1, 1)
        end = datetime(year, 12, 31)
        weather_df = Daily('10513', start=start, end=end).fetch().reset_index()

        # Fehlende Spalten auffüllen
        for col in ['prcp', 'snow', 'pres', 'tmin', 'tavg', 'tmax']:
            if col not in weather_df.columns:
                weather_df[col] = pd.NA

        # Aufruf der Visualisierungen
        plot_rainfall(year, weather_df[["time", "prcp"]])
        plot_temperature(year, weather_df[["time", "tmin", "tavg", "tmax"]])
        plot_pressure_and_precipitation(year, weather_df[["time", "prcp", "snow", "pres"]])
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

```