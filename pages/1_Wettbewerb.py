import streamlit as st
import json

st.title("SSV 1928 e.V. Sulzbach")
st.write(
    "Eingabe des Wettbewerbs"
)

# Eingabefelder
wettbewerbsname = st.text_input("Wettbewerbsname")
datum = st.date_input("Datum")
teilnehmer = st.text_area("Teilnehmer (kommagetrennt)")
disziplin = st.selectbox("Disziplin", ["Unterhebel", "KK", "Luftgewehr"])

# Button zum Speichern
if st.button("Wettbewerb speichern"):
    # Hier würde der Code zum Speichern in der Datenbank stehen
    st.success("Wettbewerb erfolgreich gespeichert!")

def speichern_wettbewerb(wettbewerbsname, datum, teilnehmer, disziplin):
    data = {
        "wettbewerbsname": wettbewerbsname,
        "datum": str(datum),
        "teilnehmer": teilnehmer.split(','),
        "disziplin": disziplin
    }

    with open('wettbewerbe.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')  # Neue Zeile für den nächsten Eintrag