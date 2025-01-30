import pandas as pd
import streamlit as st

st.set_page_config(page_title="Schützen anlegen")
st.title("Schützen anlegen")

# Initialisiere den DataFrame im st.session_state
if "schuetzen_df" not in st.session_state:
    try:
        st.session_state.schuetzen_df = pd.read_csv("schuetzen.csv")
    except FileNotFoundError:
        st.session_state.schuetzen_df = pd.DataFrame(columns=["Startnummer", "Name", "Wertung", "Mannschaft"])

    # Stelle sicher, dass 'Startnummer' existiert und fülle sie, falls nötig
    if 'Startnummer' not in st.session_state.schuetzen_df.columns:
        st.session_state.schuetzen_df['Startnummer'] = []  # Initialisiere als leere Liste
    elif st.session_state.schuetzen_df.empty:  # Handle leeren DataFrame mit vorhandener Spalte
        st.session_state.schuetzen_df['Startnummer'] = []  # Initialisiere als leere Liste
    # Fülle die Startnummern, wenn die Spalte existiert und der DataFrame nicht leer ist.
    if not st.session_state.schuetzen_df.empty and not st.session_state.schuetzen_df['Startnummer'].tolist(): # Überprüfe, ob der DataFrame nicht leer ist und die Liste leer ist
        st.session_state.schuetzen_df['Startnummer'] = range(1, len(st.session_state.schuetzen_df) + 1)


st.header("Schützen anlegen")

with st.form("schütze_anlegen"):
    name = st.text_input("Name des Schützen")
    wertung = st.selectbox("Wertung", ["Einzel", "Team", "Einzel+Team"])
    mannschaft = st.text_input("Mannschaft")
    submitted = st.form_submit_button("Speichern")

if submitted:
    # Finde die höchste bestehende Startnummer oder starte bei 1, wenn DataFrame leer ist oder keine Startnummern vorhanden sind
    if not st.session_state.schuetzen_df.empty and st.session_state.schuetzen_df['Startnummer'].tolist(): # Überprüfe, ob der DataFrame nicht leer ist und die Liste nicht leer ist
        next_startnummer = st.session_state.schuetzen_df['Startnummer'].max() + 1
    else:
        next_startnummer = 1

    new_entry = {
        "Startnummer": next_startnummer,
        "Name": name,
        "Wertung": wertung,
        "Mannschaft": mannschaft,
    }
    st.session_state.schuetzen_df.loc[len(st.session_state.schuetzen_df)] = new_entry
    st.session_state.schuetzen_df.to_csv("schuetzen.csv", index=False)
    st.rerun()

# Zeige den DataFrame an
st.header("Übersicht der Schützen")

edited_df = st.data_editor(
    st.session_state.schuetzen_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Startnummer": st.column_config.NumberColumn(
            "Startnummer",
            help="Eindeutige Startnummer",
            disabled=True,  # Startnummer kann nicht bearbeitet werden
        ),
        "Wertung": st.column_config.SelectboxColumn(
            "Wertung",
            help="Wie startet der Schütze",
            options=["Einzel", "Team", "Einzel+Team"],
            required=True,
        ),
        "Mannschaft": st.column_config.TextColumn(
            "Mannschaft",
            default="",  # Standardwert ist leer
            help="Name der Mannschaft",
        ),
    },
    disabled=["Name"],
)

# Wenn der DataFrame bearbeitet wurde, speichere die Änderungen
if not edited_df.equals(st.session_state.schuetzen_df):
    st.session_state.schuetzen_df = edited_df.copy()  # Erstelle eine Kopie
    st.session_state.schuetzen_df.to_csv("schuetzen.csv", index=False)
    st.rerun()  # oder st.experimental_rerun()