import streamlit as st
import json
import os
import pandas as pd

st.title("Einzelergebnisse")

# Pfad zur JSON-Datei
ergebnisse_datei = "ergebnisse.json"

try:
    if os.path.exists(ergebnisse_datei):
        with open(ergebnisse_datei, "r", encoding="utf-8") as f:
            ergebnisse = json.load(f)

        einzel_ergebnisse = []
        for eintrag in ergebnisse:
            for mitglied in eintrag["mitglieder"]:
                einzel_ergebnisse.append({
                    "Starter": mitglied["mitglied"],
                    "Mannschaft": eintrag["mannschaft"],
                    "Punkte": mitglied["punkte"]
                })

        # Sortieren der Einzelergebnisse absteigend nach Punkten
        sortierte_einzel_ergebnisse = sorted(einzel_ergebnisse, key=lambda x: x["Punkte"], reverse=True)

        # Streamlit-Tabelle erstellen mit Pandas DataFrame
        df = pd.DataFrame(sortierte_einzel_ergebnisse)
        df.insert(0, "Platz", range(1, len(df) + 1))  # Füge Platzspalte ein
        st.table(df.set_index("Platz"))  # Setze "Platz" als Index und zeige Tabelle an

    else:
        st.write("Noch keine Ergebnisse vorhanden.")

except FileNotFoundError:
    st.write("Ergebnisdatei nicht gefunden.")
except json.JSONDecodeError:
    st.write("Fehler beim Lesen der Ergebnisdatei. Datei ist möglicherweise beschädigt.")
except Exception as e:
    st.write(f"Ein unerwarteter Fehler ist aufgetreten: {e}")