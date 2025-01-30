import streamlit as st
import json
import os

st.title("Mannschaften löschen")

#script_dir = os.path.dirname(os.path.abspath(__file__))
finale_mannschaften_datei = "finale_mannschaften.json"

def lade_mannschaften():
    try:
        with open(finale_mannschaften_datei, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Leere Liste zurückgeben, wenn Datei nicht existiert oder ungültig ist

def speichere_mannschaften(mannschaften):
    with open(finale_mannschaften_datei, "w", encoding="utf-8") as f:
        json.dump(mannschaften, f, indent=4, ensure_ascii=False)

finale_mannschaften = lade_mannschaften()

if not finale_mannschaften:
    st.write("Noch keine Finalmannschaften vorhanden.")
else:
    mannschaft_auswahl_finale = st.selectbox("Mannschaft auswählen", [mannschaft["mannschaft"] for mannschaft in finale_mannschaften])

    if st.button("Mannschaft löschen"):
        for i, mannschaft in enumerate(finale_mannschaften):
            if mannschaft["mannschaft"] == mannschaft_auswahl_finale:
                del finale_mannschaften[i]
                break

        speichere_mannschaften(finale_mannschaften)
        st.success(f"Mannschaft '{mannschaft_auswahl_finale}' erfolgreich gelöscht!")

        # Aktualisiere die Auswahl nach dem Löschen
        finale_mannschaften = lade_mannschaften()  # Neu laden
        if finale_mannschaften:
            mannschaft_auswahl_finale = st.selectbox("Mannschaft auswählen", [mannschaft["mannschaft"] for mannschaft in finale_mannschaften])
        else:
            st.write("Alle Mannschaften wurden gelöscht.")