import streamlit as st
import json

# Titel der App
st.title("SSV 1928 e.V. Sulzbach")
st.write("Wettbewerb")

# Initialisiere den Session State, falls noch nicht geschehen
if "data_list" not in st.session_state:
    st.session_state.data_list = []

if "wettkampf_name" not in st.session_state:
    st.session_state['wettkampf_name'] = ""

# Funktionen
def lade_daten():
    try:
        with open("wettbewerbe.json", "r") as f:
            st.session_state.data_list = json.load(f)
    except FileNotFoundError:
        st.session_state.data_list = []

# Hauptseite
# Lade und zeige Daten
lade_daten()

# Dropdown-Feld für die Auswahl des Wettkampfes
wettkampf_name = st.selectbox(
    "Name des Wettkampfes",
    options=[d["Wettbewerb"] for d in st.session_state.data_list] if st.session_state.data_list else ["Keine Wettbewerbe vorhanden"],  # Anzeige der Wettbewerbsnamen im Dropdown oder "Keine Wettbewerbe vorhanden"
    index=0 if not st.session_state.data_list else ([d["Wettbewerb"] for d in st.session_state.data_list].index(st.session_state['wettkampf_name']) if st.session_state['wettkampf_name'] in [d["Wettbewerb"] for d in st.session_state.data_list] else 0) # Vorauswahl des gespeicherten Namens oder des ersten Eintrags oder 0 wenn keine vorhanden
)

# Speichern des ausgewählten Namens im Session State
st.session_state['wettkampf_name'] = wettkampf_name

# Anzeigen des ausgewählten Wettkampfnamens unter der Überschrift
if st.session_state['wettkampf_name']:
    st.write(f"Ausgewählter Wettkampf: {st.session_state['wettkampf_name']}")