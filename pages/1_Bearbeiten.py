import streamlit as st
import json
import os

st.title("Ergebnis ändern")

# Pfad zur JSON-Datei
#script_dir = os.path.dirname(os.path.abspath(__file__))
ergebnisse_datei = "ergebnisse.json"

try:
    if os.path.exists(ergebnisse_datei):
        with open(ergebnisse_datei, "r", encoding="utf-8") as f:
            ergebnisse = json.load(f)

        # Dropdown-Feld zur Auswahl der Mannschaft
        mannschaft_auswahl = st.selectbox("Mannschaft auswählen", [eintrag["mannschaft"] for eintrag in ergebnisse])

        # Dropdown-Feld zur Auswahl des Mitglieds
        mitglied_auswahl = st.selectbox(
            "Mitglied auswählen",
            [
                mitglied["mitglied"]
                for eintrag in ergebnisse
                if eintrag["mannschaft"] == mannschaft_auswahl
                for mitglied in eintrag["mitglieder"]
            ],
        )

        # Aktuelles Ergebnis anzeigen
        for eintrag in ergebnisse:
            if eintrag["mannschaft"] == mannschaft_auswahl:
                for mitglied in eintrag["mitglieder"]:
                    if mitglied["mitglied"] == mitglied_auswahl:
                        aktuelles_ergebnis = mitglied["punkte"]
                        st.write(f"Aktuelles Ergebnis für {mitglied_auswahl}: {aktuelles_ergebnis}")
                        break
                break

        # Eingabefeld für das neue Ergebnis
        neues_ergebnis = st.number_input("Neues Ergebnis", min_value=0)

        # Button zum Speichern der Änderung
        if st.button("Ergebnis ändern"):
            for eintrag in ergebnisse:
                if eintrag["mannschaft"] == mannschaft_auswahl:
                    for mitglied in eintrag["mitglieder"]:
                        if mitglied["mitglied"] == mitglied_auswahl:
                            mitglied["punkte"] = neues_ergebnis

                            # Aktualisiere das Gesamtmannschaftsergebnis
                            eintrag["team_ergebnis"] = sum(m["punkte"] for m in eintrag["mitglieder"])
                            break  # Innere Schleife beenden, sobald das Mitglied gefunden wurde
                    break  # Äußere Schleife beenden, sobald die Mannschaft gefunden wurde

            # Änderungen in ergebnisse.json speichern
            with open(ergebnisse_datei, "w", encoding="utf-8") as f:
                json.dump(ergebnisse, f, indent=4, ensure_ascii=False)

            st.success("Ergebnis erfolgreich geändert und Team-Ergebnis aktualisiert!")

    else:
        st.write("Noch keine Ergebnisse vorhanden.")

except FileNotFoundError:
    st.write("Ergebnisdatei nicht gefunden.")
except json.JSONDecodeError:
    st.write("Fehler beim Lesen der Ergebnisdatei. Datei ist möglicherweise beschädigt.")
except Exception as e:
    st.write(f"Ein unerwarteter Fehler ist aufgetreten: {e}")


