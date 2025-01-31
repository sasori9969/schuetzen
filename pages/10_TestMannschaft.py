import streamlit as st
import json
import os
import pandas as pd

st.title("Mannschaftsergebnisse")

# Pfad zur JSON-Datei im Hauptverzeichnis
ergebnisse_datei = "ergebnisse.json" # Direkt im Hauptverzeichnis

try:
    if os.path.exists(ergebnisse_datei):
        with open(ergebnisse_datei, "r", encoding="utf-8") as f:
            ergebnisse = json.load(f)

        # Sortieren der Ergebnisse absteigend nach Team-Ergebnis
        sortierte_ergebnisse = sorted(ergebnisse, key=lambda x: x["team_ergebnis"], reverse=True)

        # Pandas DataFrame erstellen
        df = pd.DataFrame(sortierte_ergebnisse)
        df.insert(0, 'Platz', range(1, len(df) + 1))  # Platznummer hinzufügen

        df = df.drop(["wettkampf", "mitglieder"], axis=1)        # Streamlit-Tabelle anzeigen (Spalte "Mitglieder" wird nicht angezeigt)
        # Spalten umbenennen
        df = df.rename(columns={"mannschaft": "Mannschaft", "team_ergebnis": "Gesamtpunkte"})
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.write("Noch keine Ergebnisse vorhanden.")

except FileNotFoundError:
    st.write("Ergebnisdatei nicht gefunden.")
except json.JSONDecodeError:
    st.write("Fehler beim Lesen der Ergebnisdatei. Datei ist möglicherweise beschädigt.")
except Exception as e:
    st.write(f"Ein unerwarteter Fehler ist aufgetreten: {e}")