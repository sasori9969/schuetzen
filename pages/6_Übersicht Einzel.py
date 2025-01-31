import streamlit as st
import json
import pandas as pd
import os

def parse_results(file_path):
    """Parses a JSON file containing competition results and keeps only the best score per participant.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        pd.DataFrame: A DataFrame containing the parsed results with only the best scores, sorted by points.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    for entry in data:
        for member in entry["mitglieder"]:
            results.append({
                "Starter": member["mitglied"],
                "Mannschaft": entry["mannschaft"],
                "Punkte": member["punkte"]
            })

    # Erstelle ein DataFrame und gruppiere nach "Starter", behalte nur die maximale Punktzahl
    df = pd.DataFrame(results)
    df = df.groupby("Starter", as_index=False).max()

    # Sortiere das DataFrame absteigend nach "Punkte"
    df = df.sort_values("Punkte", ascending=False)

    # Füge die Platzspalte hinzu und setze sie als Index
    df.insert(0, "Platz", range(1, len(df) + 1))
    return df.set_index("Platz")
# Streamlit App
st.title("Einzelergebnisse")

# Pfad zur JSON-Datei
ergebnisse_datei = "ergebnisse.json"

try:
    if os.path.exists(ergebnisse_datei):
        df = parse_results(ergebnisse_datei)
        st.table(df)
    else:
        st.write("Noch keine Ergebnisse vorhanden.")
except FileNotFoundError:
    st.write("Die Ergebnisdatei konnte nicht gefunden werden.")
except json.JSONDecodeError:
    st.write("Die Ergebnisdatei ist fehlerhaft und konnte nicht gelesen werden.")
except Exception as e:
    st.write(f"Ein unerwarteter Fehler ist aufgetreten: {e}")