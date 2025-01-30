import streamlit as st
import json
import os

st.title("Admin-Bereich")

# Pfad zum übergeordneten Ordner, der die JSON-Dateien enthält
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(script_dir, ".."))  # Gehe eine Ebene höher

# Funktion zum Leeren einer JSON-Datei
def json_datei_leeren(datei_pfad):
    try:
        with open(datei_pfad, "w") as f:
            json.dump([], f)  # Leere Liste in die Datei schreiben
        st.success(f"{datei_pfad} wurde erfolgreich geleert.")
    except Exception as e:
        st.error(f"Fehler beim Leeren von {datei_pfad}: {e}")

# Liste der JSON-Dateien, die geleert werden sollen
json_dateien = [
    "ergebnisse.json",
    "finale_mannschaften.json",
    "mannschaften.json",
    "schuetzen.json",
    "wettbewerbe.json"
]

# Button zum Leeren aller Dateien
if st.button("Alle JSON-Dateien leeren"):
    for datei in json_dateien:
        datei_pfad = os.path.join(data_dir, datei)  # Verwende data_dir
        if os.path.exists(datei_pfad):
            json_datei_leeren(datei_pfad)
        else:
            st.warning(f"{datei_pfad} nicht gefunden.")

# Option zum einzelnen Leeren von Dateien
st.subheader("Einzelne Dateien leeren")
for datei in json_dateien:
    datei_pfad = os.path.join(data_dir, datei)  # Verwende data_dir
    if os.path.exists(datei_pfad):
        if st.button(f"{datei} leeren"):
            json_datei_leeren(datei_pfad)
    else:
        st.warning(f"{datei_pfad} nicht gefunden.")