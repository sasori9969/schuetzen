import streamlit as st
import json
import os

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
if "wettkampf_name" not in st.session_state:  # Für den dynamischen Wettkampfnamen
    st.session_state.wettkampf_name = ""

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

# Eingabefeld für den Wettkampfnamen
st.session_state.wettkampf_name = st.text_input("Wettkampf Name", st.session_state.wettkampf_name)

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
                mitglieder = mannschaft.get("mitglieder", [])
                for mitglied in mitglieder:
                    st.write(f"- {mitglied}")
                break

        # Eingabefelder für die Ergebnisse
        st.subheader("Ergebnis eingeben")
        punkte = {}

        for i, mitglied in enumerate(mitglieder):
            key = f"punkte_{ausgewaehlte_mannschaft}_{mitglied}_{i}"
            punkte[mitglied] = st.number_input(f"Punkte für {mitglied}", key=key, min_value=0)

        # Berechnung des Teamergebnisses
        team_ergebnis = sum(punkte.values())
        st.write(f"Team Ergebnis: {team_ergebnis}")

        if st.button("Ergebnis speichern"):
            # Logik zum Speichern der Ergebnisse
            if punkte:
                ergebnisse_liste = []
                for mitglied, wert in punkte.items():
                    ergebnisse_liste.append({"mitglied": mitglied, "punkte": wert})

                # Datenstruktur für die Speicherung
                daten_zum_speichern = {
                    "wettkampf": st.session_state.wettkampf_name,  # Dynamischer Wettkampfname
                    "mannschaft": ausgewaehlte_mannschaft,
                    "mitglieder": ergebnisse_liste,
                    "team_ergebnis": team_ergebnis
                }

                # Pfad zur JSON-Datei (relativ zum aktuellen Skript)
                script_dir = os.path.dirname(os.path.abspath(__file__))
                ergebnisse_datei = os.path.join(script_dir, "ergebnisse.json")

                try:
                    # Laden vorhandener Ergebnisse (falls vorhanden)
                    if os.path.exists(ergebnisse_datei):
                        with open(ergebnisse_datei, "r") as f:
                            gespeicherte_ergebnisse = json.load(f)
                    else:
                        gespeicherte_ergebnisse = []

                    # Hinzufügen der neuen Ergebnisse
                    gespeicherte_ergebnisse.append(daten_zum_speichern)

                    # Speichern der aktualisierten Ergebnisse
                    with open(ergebnisse_datei, "w") as f:
                        json.dump(gespeicherte_ergebnisse, f, indent=4, ensure_ascii=False)

                    st.success(f"Ergebnisse für Mannschaft '{ausgewaehlte_mannschaft}' erfolgreich gespeichert!")

                except Exception as e:
                    st.error(f"Fehler beim Speichern der Ergebnisse: {e}")

            else:
                st.warning("Bitte geben Sie Ergebnisse ein, bevor Sie speichern.")

else:
    st.write("Keine Mannschaften zum Auswählen gefunden.")