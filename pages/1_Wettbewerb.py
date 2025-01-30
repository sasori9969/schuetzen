import streamlit as st
import json

st.title("SSV 1928 e.V. Sulzbach")
st.write("Wettbewerb")

# Initialisiere den Session State, falls noch nicht geschehen
if "data_list" not in st.session_state:
    st.session_state.data_list = []

# Erstelle die Texteingabefelder und speichere die Labels separat
wettbewerb = st.text_input("Wettbewerb:")
disziplin = st.text_input("Disziplin:")
distanz = st.selectbox("Distanz:", ["10m", "25m", "50m"])
datum = st.date_input("Datum:")

# Liste der Labels
spalten_ueberschriften = ["Wettbewerb", "Disziplin", "Distanz", "Datum"]

def speichern():
    # Erstelle ein Python-Dictionary mit den eingegebenen Daten
    data = {
        "Wettbewerb": wettbewerb,
        "Disziplin": disziplin,
        "Distanz": distanz,
        "Datum": str(datum)
    }

    # Füge das Dictionary zur Liste im Session State hinzu
    st.session_state.data_list.append(data)

    # Speichere die gesamte Liste als JSON-Datei
    with open("wettbewerbe.json", "w") as f:
        json.dump(st.session_state.data_list, f)

    st.success("Daten erfolgreich gespeichert!")

# Button zum Speichern
if st.button("Speichern"):
    speichern()

def lade_daten():
    try:
        with open("wettbewerbe.json", "r") as f:
            # Lade die Daten in den Session State
            st.session_state.data_list = json.load(f)
    except FileNotFoundError:
        st.session_state.data_list = []

    # Zeige die Daten in einer Tabelle an
    for i, d in enumerate(st.session_state.data_list):
        cols = st.columns([4, 4, 4, 4, 2])
        cols[0].write(d["Wettbewerb"])
        cols[1].write(d["Disziplin"])
        cols[2].write(d["Distanz"])
        cols[3].write(d["Datum"])
        if cols[4].button("Löschen", key=f"delete_{i}"):
            loeschen(i)

def loeschen(index):
    # Entferne den Eintrag aus der Liste im Session State
    st.session_state.data_list.pop(index)

    # Speichere die aktualisierte Liste in der JSON-Datei
    with open("wettbewerbe.json", "w") as f:
        json.dump(st.session_state.data_list, f)

    # Lade die Daten neu, um die Tabelle zu aktualisieren
    st.rerun()

# Rufe die Funktion zum Laden der Daten beim ersten Laden der App auf
lade_daten()