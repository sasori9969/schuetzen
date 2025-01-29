import streamlit as st

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