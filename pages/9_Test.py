import pandas as pd
import streamlit as st

st.set_page_config(page_title="Schützenverwaltung", page_icon="")

# Initialisiere den DataFrame im st.session_state
if "schuetzen_df" not in st.session_state:
    try:
        st.session_state.schuetzen_df = pd.read_csv("schuetzen.csv")
    except FileNotFoundError:
        st.session_state.schuetzen_df = pd.DataFrame(columns=["Startnummer", "Name", "Wertung", "Mannschaft", "Status", "Ergebnis 1", "Ergebnis 2", "Ergebnis 3", "Gesamtergebnis"])

# Funktion zum Speichern des DataFrames
def speichern():
    st.session_state.schuetzen_df.to_csv("schuetzen.csv", index=False)

# Funktion zum Hinzufügen eines Schützen
def add_schuetze(name, wertung, mannschaft, status, ergebnis1, ergebnis2, ergebnis3):
    # Validate input
    if wertung not in ["Einzel", "Team", "Einzel+Team"] or status not in ["Aktiv", "deaktivieren"]:
        st.error("Ungültige Eingabe für Wertung oder Status.")
        return

    # Check for duplicates
    if any((st.session_state.schuetzen_df['Name'] == name) & (st.session_state.schuetzen_df['Mannschaft'] == mannschaft)):
        st.error("Ein Schütze mit diesem Namen und in dieser Mannschaft existiert bereits.")
        return

    # Generate next startnummer
    next_startnummer = st.session_state.schuetzen_df['Startnummer'].max() + 1 if not st.session_state.schuetzen_df.empty else 1

    # Create new entry with calculated total score
    new_entry = {"Startnummer": next_startnummer, "Name": name, "Wertung": wertung, "Mannschaft": mannschaft,
                 "Status": status, "Ergebnis 1": ergebnis1, "Ergebnis 2": ergebnis2, "Ergebnis 3": ergebnis3}

    # Append new entry to DataFrame
    st.session_state.schuetzen_df = pd.concat([st.session_state.schuetzen_df, pd.DataFrame([new_entry])], ignore_index=True)

    # Update Gesamtergebnis
    update_gesamt_ergebnis()

    # Save DataFrame
    speichern()
    st.success("Schütze erfolgreich hinzugefügt.")

# Funktion zum Löschen eines Schützen
def delete_schuetze(index):
    if 0 <= index < len(st.session_state.schuetzen_df):
        st.session_state.schuetzen_df = st.session_state.schuetzen_df.drop(index)
        speichern()
        st.success("Schütze erfolgreich gelöscht.")
    else:
        st.error("Ungültiger Index. Bitte geben Sie einen Index innerhalb des gültigen Bereichs ein.")

# Funktion zum Aktualisieren des Gesamtergebnisses
def update_gesamt_ergebnis():
    st.session_state.schuetzen_df['Gesamtergebnis'] = st.session_state.schuetzen_df['Ergebnis 1'] + \
                                                    st.session_state.schuetzen_df['Ergebnis 2'] + \
                                                    st.session_state.schuetzen_df['Ergebnis 3']
    speichern()
    st.success("Gesamtergebnis aktualisiert.")
# Benutzerinterface
st.title("Schützenverwaltung")

# Schützen anlegen
with st.form("schuetze_anlegen"):
    name = st.text_input("Name des Schützen")
    wertung = st.selectbox("Wertung", ["Einzel", "Team", "Einzel+Team"])
    mannschaft = st.text_input("Mannschaft")
    status = st.selectbox("Status", ["Aktiv", "deaktivieren"])
    ergebnis1 = st.number_input("Ergebnis 1")
    ergebnis2 = st.number_input("Ergebnis 2")
    ergebnis3 = st.number_input("Ergebnis 3")
    submitted = st.form_submit_button("Speichern")

if submitted:
    add_schuetze(name, wertung, mannschaft, status, ergebnis1, ergebnis2, ergebnis3)

# Button zum manuellen Aktualisieren
if st.button("Gesamtergebnis aktualisieren"):
    update_gesamt_ergebnis()
    
# Schützen bearbeiten
edited_df = st.data_editor(
    st.session_state.schuetzen_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Startnummer": st.column_config.NumberColumn("Startnummer", help="Eindeutige Startnummer", disabled=True),
        "Gesamtergebnis": st.column_config.NumberColumn("Gesamtergebnis", help="Summe der Ergebnisse", disabled=True),
        # ... other column configurations
    },
    on_change=update_gesamt_ergebnis
)

# Automatisches Speichern bei Änderungen
if st.session_state.schuetzen_df is not None and not edited_df.equals(st.session_state.schuetzen_df):
    st.session_state.schuetzen_df = edited_df.copy()
    speichern()