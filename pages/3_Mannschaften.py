import streamlit as st
import json

# Titel der App
st.title("SSV 1928 e.V. Sulzbach")
st.write("Wettbewerb")

# Initialisiere den Session State
if "data_list" not in st.session_state:
    st.session_state.data_list = []
if "mannschaften" not in st.session_state:
    st.session_state.mannschaften = []
if "schuetzen" not in st.session_state:
    st.session_state.schuetzen = []
if "wettkampf_name" not in st.session_state:
    st.session_state['wettkampf_name'] = ""
if "selected_names" not in st.session_state:  # Speichert die ausgewählten Schützennamen
    st.session_state.selected_names = [""] * 3  # Initialisiert mit leeren Strings

# Funktionen
def lade_daten():
    try:
        with open("wettbewerbe.json", "r") as f:
            st.session_state.data_list = json.load(f)
    except FileNotFoundError:
        st.error("wettbewerbe.json nicht gefunden!")
        st.session_state.data_list = []

    try:
        with open("mannschaften.json", "r") as f:
            st.session_state.mannschaften = json.load(f)
    except FileNotFoundError:
        st.error("mannschaften.json nicht gefunden!")
        st.session_state.mannschaften = []

    try:
        with open("schuetzen.json", "r") as f:
            st.session_state.schuetzen = json.load(f)
    except FileNotFoundError:
        st.error("schuetzen.json nicht gefunden!")
        st.session_state.schuetzen = []

def speichere_mannschaft():
    neue_mannschaft = {
        "wettkampf": st.session_state['wettkampf_name'],
        "mannschaft": team_name,
        "mitglieder": st.session_state.selected_names
    }

    try:
        with open("finale_mannschaften.json", "r") as f:
            finale_mannschaften = json.load(f)
    except FileNotFoundError:
        finale_mannschaften = []

    finale_mannschaften.append(neue_mannschaft)

    with open("finale_mannschaften.json", "w") as f:
        json.dump(finale_mannschaften, f, indent=4)

    st.success("Mannschaft erfolgreich in finale_mannschaften.json gespeichert!")


# Hauptseite
lade_daten()

# Wettbewerbsauswahl
wettkampf_name = st.selectbox(
    "Name des Wettkampfes",
    options=[d["Wettbewerb"] for d in st.session_state.data_list] if st.session_state.data_list else ["Keine Wettbewerbe vorhanden"],
    index=0 if not st.session_state.data_list else ([d["Wettbewerb"] for d in st.session_state.data_list].index(st.session_state['wettkampf_name']) if st.session_state['wettkampf_name'] in [d["Wettbewerb"] for d in st.session_state.data_list] else 0)
)
st.session_state['wettkampf_name'] = wettkampf_name

if st.session_state['wettkampf_name']:
    st.write(f"Ausgewählter Wettkampf: {st.session_state['wettkampf_name']}")

    # Team- und Schützenauswahl mit Layoutverbesserung
    cols = st.columns(4)
    with cols[0]:
        team_name = st.selectbox("Mannschaft", options=[t["mannschaft"] for t in st.session_state.mannschaften] if st.session_state.mannschaften else ["Keine Teams vorhanden"])
    for i in range(3):
        with cols[i+1]:
            name = st.selectbox(f"Name {i+1}", options=[f"{s['vorname']} {s['name']}" for s in st.session_state.schuetzen] if st.session_state.schuetzen else ["Keine Schützen vorhanden"], key=f"name_{i}")  # Eindeutige Keys hinzufügen
            st.session_state.selected_names[i] = name  # Speichern der ausgewählten Namen im Session State

    # Anzeige der ausgewählten Teammitglieder
    st.subheader("Ausgewählte Teammitglieder:")
    st.write(f"Mannschaft: {team_name}")
    for i in range(3):
        st.write(f"Name {i+1}: {st.session_state.selected_names[i]}")

    # Button zum Speichern der Daten
    if st.button("Mannschaft speichern"):
        speichere_mannschaft()