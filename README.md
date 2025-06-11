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
