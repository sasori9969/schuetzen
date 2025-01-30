import streamlit as st
import json
import os

# Dateipfade für die JSON-Dateien
MANNSCHAFTEN_DATEI = "mannschaften.json"
SCHUETZEN_DATEI = "schuetzen.json"

# Funktionen zum Speichern der Daten
def speichere_mannschaft(mannschaft_name):
    if not os.path.exists(MANNSCHAFTEN_DATEI) or os.stat(MANNSCHAFTEN_DATEI).st_size == 0:
        mannschaften = []
    else:
        with open(MANNSCHAFTEN_DATEI, "r") as f:
            mannschaften = json.load(f)

    # Überprüfen, ob der Mannschaftsname bereits existiert
    if any(mannschaft["mannschaft"] == mannschaft_name for mannschaft in mannschaften):
        st.error(f"Die Mannschaft '{mannschaft_name}' existiert bereits!")
        return  # Nicht speichern, wenn der Name bereits vorhanden ist

    mannschaften.append({"mannschaft": mannschaft_name})

    with open(MANNSCHAFTEN_DATEI, "w") as f:
        json.dump(mannschaften, f, indent=4)
    st.success(f"Mannschaft '{mannschaft_name}' wurde erfolgreich erstellt und in '{MANNSCHAFTEN_DATEI}' gespeichert!")


def speichere_schuetze(name, vorname):
    if not os.path.exists(SCHUETZEN_DATEI) or os.stat(SCHUETZEN_DATEI).st_size == 0:
        schuetzen = []
    else:
        with open(SCHUETZEN_DATEI, "r") as f:
            schuetzen = json.load(f)

    schuetzen.append({"name": name, "vorname": vorname})

    with open(SCHUETZEN_DATEI, "w") as f:
        json.dump(schuetzen, f, indent=4)
    st.success(f"Schütze '{name}, {vorname}' wurde erfolgreich angelegt und in '{SCHUETZEN_DATEI}' gespeichert!")


# Streamlit App
st.title("SSV 1928 e.V. Sulzbach")

# Abschnitt 1: Mannschaft erstellen
st.header("Mannschaft erstellen")
mannschaft_name = st.text_input("Mannschaftsname eingeben")
if st.button("Mannschaft speichern"):
    if mannschaft_name:
        speichere_mannschaft(mannschaft_name)
    else:
        st.error("Bitte gib einen Mannschaftsnamen ein.")

# Abschnitt 2: Schützen anlegen
st.header("Schützen anlegen")
name = st.text_input("Nachname des Schützen eingeben")
vorname = st.text_input("Vorname des Schützen eingeben")
if st.button("Schützen speichern"):
    if name and vorname:
        speichere_schuetze(name, vorname)
    else:
        st.error("Bitte fülle alle Felder aus.")