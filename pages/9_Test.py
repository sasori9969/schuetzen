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

# Passe die Spaltenbreite mit column_config an
st.dataframe(
    st.session_state.schuetzen_df,
    column_config={
        "Name": st.column_config.Column(width="medium"),  # Oder "small", "large", oder eine spezifische Breite in Pixeln
        "Wertung": st.column_config.Column(width="medium"),
    },
)