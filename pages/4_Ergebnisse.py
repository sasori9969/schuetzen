import streamlit as st
import json

# Titel der App
st.title("SSV 1928 e.V. Sulzbach")
st.write("Ergebnis Eingabe")

# Initialisiere den Session State
if "data_list" not in st.session_state:
    st.session_state.data_list = []
if "mannschaften" not in st.session_state:
    st.session_state.mannschaften = []
if "ausgewaehlte_mannschaft" not in st.session_state:
    st.session_state.ausgewaehlte_mannschaft = None

# Funktionen
def lade_daten():
    try:
        with open("finale_mannschaften.json", "r") as f:
            st.session_state.data_list = json.load(f)
            st.session_state.mannschaften = [mannschaft["mannschaft"] for mannschaft in st.session_state.data_list]
    except FileNotFoundError:
        st.error("finale_mannschaften.json nicht gefunden!")
        st.session_state.data_list = []

# Hauptseite
lade_daten()

# Dropdown-Menü für die Mannschaftsauswahl
if st.session_state.mannschaften:
    ausgewaehlte_mannschaft = st.selectbox("Mannschaft auswählen", st.session_state.mannschaften)
    st.session_state.ausgewaehlte_mannschaft = ausgewaehlte_mannschaft

    if ausgewaehlte_mannschaft:
        st.write(f"Ausgewählte Mannschaft: {ausgewaehlte_mannschaft}")

        # Anzeigen der Mitglieder der ausgewählten Mannschaft
        for mannschaft in st.session_state.data_list:
            if mannschaft["mannschaft"] == ausgewaehlte_mannschaft:
                st.write("Mitglieder:")
                mitglieder = mannschaft.get("mitglieder", []) # Speichere die Mitglieder in einer Variable
                for mitglied in mitglieder:
                    st.write(f"- {mitglied}")
                break  # Wichtig: Beende die Schleife, sobald die Mannschaft gefunden wurde

        # Eingabefelder für die Ergebnisse mit eindeutigen Keys
        st.subheader("Ergebnis eingeben")
        punkte = {}

        for i, mitglied in enumerate(mitglieder):
            key = f"punkte_{ausgewaehlte_mannschaft}_{mitglied}_{i}"
            punkte[mitglied] = st.number_input(f"Punkte für {mitglied}", key=key, min_value=0) # min_value hinzugefügt

        if st.button("Ergebnis speichern"):
            # Logik zum Speichern der Ergebnisse
            if punkte: # Überprüfe, ob überhaupt Punkte eingegeben wurden
                ergebnisse_liste = []
                for mitglied, wert in punkte.items():
                    ergebnisse_liste.append({"mitglied": mitglied, "punkte": wert})

                # Datenstruktur für die Speicherung (Beispiel)
                daten_zum_speichern = {
                    "wettkampf": "Dein Wettkampf Name", # Hier solltest du den Wettkampfnamen dynamisch einfügen
                    "mannschaft": ausgewaehlte_mannschaft,
                    "mitglieder": ergebnisse_liste
                }

                # TODO: Implementiere die tatsächliche Speicherung der Daten (z.B. in eine JSON-Datei)
                st.write("Ergebnisse werden gespeichert (noch nicht implementiert):") # Hinweis für den Benutzer
                st.write(daten_zum_speichern) # Ausgabe zur Kontrolle.

                # Beispiel für das Speichern in eine JSON-Datei (ersetze dies mit deiner Logik):
                # with open("ergebnisse.json", "w") as f:
                #     json.dump(daten_zum_speichern, f, indent=4)
                # st.success("Ergebnisse erfolgreich gespeichert!") # Rückmeldung an den Benutzer.
            else:
                st.warning("Bitte geben Sie Ergebnisse ein, bevor Sie speichern.")


else:
    st.write("Keine Mannschaften zum Auswählen gefunden.")