import streamlit as st
import json
import os

st.title("Team bearbeiten")

# Pfad zur JSON-Datei
script_dir = os.path.dirname(os.path.abspath(__file__))
ergebnisse_datei = os.path.join(script_dir, "ergebnisse.json")

try:
    if os.path.exists(ergebnisse_datei):
        with open(ergebnisse_datei, "r", encoding="utf-8") as f:
            ergebnisse = json.load(f)

        # Dropdown-Feld zur Auswahl der Mannschaft
        mannschaft_auswahl = st.selectbox("Mannschaft auswählen", [eintrag["mannschaft"] for eintrag in ergebnisse])

        # Anzeigen der aktuellen Teamzusammensetzung
        for eintrag in ergebnisse:
            if eintrag["mannschaft"] == mannschaft_auswahl:
                st.write(f"Aktuelle Teamzusammensetzung für {mannschaft_auswahl}:")
                for mitglied in eintrag["mitglieder"]:
                    st.write(f"- {mitglied['mitglied']} ({mitglied['punkte']} Punkte)")
                break

        # Eingabefelder zum Ändern der Teamzusammensetzung
        st.subheader("Teamzusammensetzung ändern")

        # Neues Mitglied hinzufügen
        neues_mitglied_name = st.text_input("Name des neuen Mitglieds")
        neues_mitglied_punkte = st.number_input("Punkte des neuen Mitglieds", min_value=0)
        if st.button("Mitglied hinzufügen"):
            for eintrag in ergebnisse:
                if eintrag["mannschaft"] == mannschaft_auswahl:
                    eintrag["mitglieder"].append({"mitglied": neues_mitglied_name, "punkte": neues_mitglied_punkte})
                    break
            st.success(f"Mitglied '{neues_mitglied_name}' erfolgreich hinzugefügt!")

        # Mitglied entfernen
        mitglied_zum_entfernen = st.selectbox(
            "Mitglied zum Entfernen auswählen",
            [mitglied["mitglied"] for eintrag in ergebnisse if eintrag["mannschaft"] == mannschaft_auswahl for mitglied in eintrag["mitglieder"]]
        )
        if st.button("Mitglied entfernen"):
            for eintrag in ergebnisse:
                if eintrag["mannschaft"] == mannschaft_auswahl:
                    eintrag["mitglieder"] = [mitglied for mitglied in eintrag["mitglieder"] if mitglied["mitglied"] != mitglied_zum_entfernen]
                    break
            st.success(f"Mitglied '{mitglied_zum_entfernen}' erfolgreich entfernt!")

        # Änderungen speichern
        if st.button("Änderungen speichern"):
            with open(ergebnisse_datei, "w", encoding="utf-8") as f:
                json.dump(ergebnisse, f, indent=4, ensure_ascii=False)
            st.success("Änderungen erfolgreich gespeichert!")

    else:
        st.write("Noch keine Ergebnisse vorhanden.")

except FileNotFoundError:
    st.write("Ergebnisdatei nicht gefunden.")
except json.JSONDecodeError:
    st.write("Fehler beim Lesen der Ergebnisdatei. Datei ist möglicherweise beschädigt.")
except Exception as e:
    st.write(f"Ein unerwarteter Fehler ist aufgetreten: {e}")