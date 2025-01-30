import streamlit as st
import json

# Titel der App
st.title("SSV 1928 e.V. Sulzbach")
st.write("Wettbewerb")

# Initialisiere den Session State, falls noch nicht geschehen
if "data_list" not in st.session_state:
    st.session_state.data_list = []

if "selected_competition" not in st.session_state:
    st.session_state.selected_competition = None

if "wettkampf_name" not in st.session_state:
    st.session_state['wettkampf_name'] = ""

# Funktionen
def speichern():
    data = {
        "Wettbewerb": wettbewerb,
        "Disziplin": disziplin,
        "Distanz": distanz,
        "Datum": str(datum)
    }
    st.session_state.data_list.append(data)
    with open("wettbewerbe.json", "w") as f:
        json.dump(st.session_state.data_list, f)
    st.success("Daten erfolgreich gespeichert!")

def loeschen(index):
    st.session_state.data_list.pop(index)
    with open("wettbewerbe.json", "w") as f:
        json.dump(st.session_state.data_list, f)
    st.rerun()

def auswahlen(index):
    st.session_state.selected_competition = st.session_state.data_list[index]
    st.session_state.current_page = "details"  # Wechsle zur Detailseite

def lade_daten():
    try:
        with open("wettbewerbe.json", "r") as f:
            st.session_state.data_list = json.load(f)
    except FileNotFoundError:
        st.session_state.data_list = []

# Navigation zwischen Seiten
if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

# Hauptseite
if st.session_state.current_page == "main":
    # Eingabefelder
    wettbewerb = st.text_input("Wettbewerb:")
    disziplin = st.text_input("Disziplin:")
    distanz = st.selectbox("Distanz:", ["10m", "25m", "50m"])
    datum = st.date_input("Datum:")

    # Button zum Speichern
    if st.button("Speichern"):
        speichern()

    # Lade und zeige Daten
    lade_daten()
    for i, d in enumerate(st.session_state.data_list):
        cols = st.columns([4, 4, 4, 4, 2, 2])
        cols[0].write(d["Wettbewerb"])
        cols[1].write(d["Disziplin"])
        cols[2].write(d["Distanz"])
        cols[3].write(d["Datum"])
        if cols[4].button("del", key=f"delete_{i}"):
            loeschen(i)
        if cols[5].button("Go", key=f"select_{i}"):
            auswahlen(i)

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


# Detailseite für den ausgewählten Wettbewerb
elif st.session_state.current_page == "details":
    st.write("### Details des ausgewählten Wettbewerbs")
    if st.session_state.selected_competition:
        st.write(f"**Wettbewerb:** {st.session_state.selected_competition['Wettbewerb']}")
        st.write(f"**Disziplin:** {st.session_state.selected_competition['Disziplin']}")
        st.write(f"**Distanz:** {st.session_state.selected_competition['Distanz']}")
        st.write(f"**Datum:** {st.session_state.selected_competition['Datum']}")
    else:
        st.write("Kein Wettbewerb ausgewählt.")

    # Button zur Rückkehr zur Hauptseite
    if st.button("Zurück zur Hauptseite"):
        st.session_state.current_page = "main"
        st.rerun()