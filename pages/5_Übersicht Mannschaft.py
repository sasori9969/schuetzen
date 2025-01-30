import streamlit as st
import json
import os

st.title("Mannschaftsergebnisse")

# Pfad zur JSON-Datei
script_dir = os.path.dirname(os.path.abspath(__file__))
ergebnisse_datei = os.path.join(script_dir, "ergebnisse.json")

try:
    if os.path.exists(ergebnisse_datei):
        with open(ergebnisse_datei, "r", encoding="utf-8") as f:
            ergebnisse = json.load(f)

        # Sortieren der Ergebnisse absteigend nach Team-Ergebnis
        sortierte_ergebnisse = sorted(ergebnisse, key=lambda x: x["team_ergebnis"], reverse=True)

        # Streamlit-Tabelle erstellen mit Platznummerierung
        data = []
        for i, eintrag in enumerate(sortierte_ergebnisse):  # enumerate für den Index
            data.append({
                "Platz": i + 1,  # Platznummer (beginnend mit 1)
                "Mannschaft": eintrag["mannschaft"],
                "Team Ergebnis": eintrag["team_ergebnis"]
            })
        st.dataframe(data, column_config={"Platz": st.column_config.Column(label="Platz", width=50)}, hide_index=True)

    else:
        st.write("Noch keine Ergebnisse vorhanden.")

except FileNotFoundError:
    st.write("Ergebnisdatei nicht gefunden.")
except json.JSONDecodeError:
    st.write("Fehler beim Lesen der Ergebnisdatei. Datei ist möglicherweise beschädigt.")
except Exception as e:
    st.write(f"Ein unerwarteter Fehler ist aufgetreten: {e}")