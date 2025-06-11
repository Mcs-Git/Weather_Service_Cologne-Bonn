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
