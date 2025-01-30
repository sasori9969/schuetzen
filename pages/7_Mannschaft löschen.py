import streamlit as st
import json
import os

st.title("Mannschaften verwalten")

script_dir = os.path.dirname(os.path.abspath(__file__))
finale_mannschaften_datei = os.path.join(script_dir, "finale_mannschaften.json")

try:
    # Laden der Finalmannschaften
    if os.path.exists(finale_mannschaften_datei):
        with open(finale_mannschaften_datei, "r", encoding="utf-8") as f:
            finale_mannschaften = json.load(f)

        # Dropdown-Feld zur Auswahl der Mannschaft (korrigiert)
        mannschaft_auswahl_finale = st.selectbox("Mannschaft auswählen", [mannschaft["mannschaft"] for mannschaft in finale_mannschaften])

        # Button zum Löschen der Mannschaft
        if st.button("Mannschaft löschen"):
            for i, mannschaft in enumerate(finale_mannschaften):
                if mannschaft["mannschaft"] == mannschaft_auswahl_finale:
                    del finale_mannschaften[i]
                    break

            # Änderungen in finale_mannschaften.json speichern
            with open(finale_mannschaften_datei, "w", encoding="utf-8") as f:
                json.dump(finale_mannschaften, f, indent=4, ensure_ascii=False)

            st.success(f"Mannschaft '{mannschaft_auswahl_finale}' erfolgreich gelöscht!")

    else:
        st.write("Noch keine Finalmannschaften vorhanden.")

except FileNotFoundError:
    st.write("Datei für Finalmannschaften nicht gefunden.")
except json.JSONDecodeError:
    st.write("Fehler beim Lesen der Datei für Finalmannschaften. Datei ist möglicherweise beschädigt.")
except Exception as e:
    st.write(f"Ein unerwarteter Fehler ist aufgetreten: {e}")