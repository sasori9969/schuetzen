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

    # Simulierte Datenbank (in einer echten Anwendung würdest du hier eine Datenbankverbindung herstellen)
gespeicherte_wettbewerbe = [
     {"name": "Sommerfest-Turnier", "datum": "2023-07-15", "disziplin": "Fußball"},
     {"name": "Volleyball-Cup", "datum": "2023-09-02", "disziplin": "Volleyball"}
]
     # Anzeige der gespeicherten Wettbewerbe
st.header("Gespeicherte Wettbewerbe")
for wettbewerb in gespeicherte_wettbewerbe:
    st.write(f"**{wettbewerb['name']}** - {wettbewerb['datum']} ({wettbewerb['disziplin']})")
