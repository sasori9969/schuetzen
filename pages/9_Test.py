import pandas as pd
import streamlit as st

st.set_page_config(page_title="Schützenverwaltung")
st.title("Schützenverwaltung")

# Initialisiere den DataFrame im st.session_state
if "schuetzen_df" not in st.session_state:
    try:
        st.session_state.schuetzen_df = pd.read_csv("schuetzen.csv")
    except FileNotFoundError:
        st.session_state.schuetzen_df = pd.DataFrame(columns=["Startnummer", "Name", "Wertung", "Mannschaft"])

# Funktion zum Speichern des DataFrames
def speichern():
    st.session_state.schuetzen_df.to_csv("schuetzen.csv", index=False)

# Funktion zum Hinzufügen eines Schützen
def add_schuetze(name, wertung, mannschaft):
    next_startnummer = st.session_state.schuetzen_df['Startnummer'].max() + 1 if not st.session_state.schuetzen_df.empty else 1
    new_entry = {"Startnummer": next_startnummer, "Name": name, "Wertung": wertung, "Mannschaft": mannschaft}
    st.session_state.schuetzen_df = pd.concat([st.session_state.schuetzen_df, pd.DataFrame([new_entry])], ignore_index=True)
    speichern()

# Funktion zum Löschen ausgewählter Schützen
def loeschen():
    ausgewaehlte_indices = edited_df[edited_df["Löschen"]].index
    if ausgewaehlte_indices.any():
        if st.button("Bist du sicher, dass du diese Schützen löschen möchtest?"):
            st.session_state.schuetzen_df = st.session_state.schuetzen_df.drop(ausgewaehlte_indices)
            speichern()
            st.success("Schützen erfolgreich gelöscht.")
            st.experimental_rerun()
        else:
            st.warning("Bitte wähle mindestens einen Schützen zum Löschen aus.")

st.header("Schützen anlegen")

with st.form("schuetze_anlegen"):
    name = st.text_input("Name des Schützen")
    wertung = st.selectbox("Wertung", ["Einzel", "Team", "Einzel+Team"])
    mannschaft = st.text_input("Mannschaft")
    submitted = st.form_submit_button("Speichern")

if submitted:
    add_schuetze(name, wertung, mannschaft)

edited_df = st.data_editor(
    st.session_state.schuetzen_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Startnummer": st.column_config.NumberColumn("Startnummer", help="Eindeutige Startnummer", disabled=True),
        "Name": st.column_config.TextColumn("Name", disabled=True),
        "Wertung": st.column_config.SelectboxColumn("Wertung", help="Wie startet der Schütze", options=["Einzel", "Team", "Einzel+Team"], required=True),
        "Mannschaft": st.column_config.TextColumn("Mannschaft", default="", help="Name der Mannschaft"),
        "Löschen": st.column_config.CheckboxColumn("Löschen", default=False, help="Markiere die Schützen, die gelöscht werden sollen")
    }
)

# Automatisches Speichern bei Änderungen
if st.session_state.schuetzen_df is not None and not edited_df.equals(st.session_state.schuetzen_df):
    st.session_state.schuetzen_df = edited_df.copy()
    speichern()

if st.button("Schützen löschen"):
    loeschen()