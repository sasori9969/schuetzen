import pandas as pd
import streamlit as st

st.set_page_config(page_title="Schützen anlegen")
st.title("Schützen anlegen")

# Initialisiere den DataFrame im st.session_state, falls er noch nicht existiert
# oder lade ihn aus der CSV-Datei, falls sie existiert
if "schuetzen_df" not in st.session_state:
    try:
        st.session_state.schuetzen_df = pd.read_csv("schuetzen.csv")
    except FileNotFoundError:
        st.session_state.schuetzen_df = pd.DataFrame(columns=["Name", "Wertung"])

st.header("Schützen anlegen")

with st.form("schütze_anlegen"):
    name = st.text_input("Name des Schützen")
    wertung = st.selectbox("Wertung", ["Einzel", "Team", "Einzel+Team"])
    submitted = st.form_submit_button("Speichern")

if submitted:
    new_entry = {
        "Name": name,
        "Wertung": wertung,
    }
    # Füge den neuen Eintrag zum DataFrame hinzu
    st.session_state.schuetzen_df.loc[len(st.session_state.schuetzen_df)] = new_entry

    # Speichere den DataFrame in der CSV-Datei
    st.session_state.schuetzen_df.to_csv("schuetzen.csv", index=False)

# Zeige den DataFrame an
st.header("Übersicht der Schützen")

edited_df = st.data_editor(
    st.session_state.schuetzen_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Wertung": st.column_config.SelectboxColumn(
            "Wertung",
            help="Ticket status",
            options=["Einzel", "Team", "Einzel+Team"],
            required=True,
        ),
    },
    disabled=["Name"],
)

# Wenn der DataFrame bearbeitet wurde, speichere die Änderungen
if not edited_df.equals(st.session_state.schuetzen_df):
    st.session_state.schuetzen_df = edited_df
    st.session_state.schuetzen_df.to_csv("schuetzen.csv", index=False)
    st.experimental_rerun()  # Erzwingt ein Neuladen der App, um die Änderungen anzuzeigen