import pandas as pd
import streamlit as st

st.set_page_config(page_title="Schützen anlegen")
st.title("Schützen anlegen")

# Initialisiere den DataFrame im st.session_state, falls er noch nicht existiert
if "schuetzen_df" not in st.session_state:
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
    # Füge den neuen Eintrag zum DataFrame hinzu (mit .loc für Effizienz)
    st.session_state.schuetzen_df.loc[len(st.session_state.schuetzen_df)] = new_entry

# Zeige den DataFrame an (außerhalb des Formulars!)
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
    # Disable editing the ID and Date Submitted columns.
    disabled=["Name"],
)