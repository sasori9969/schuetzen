import streamlit as st
import json

# Titel der Anwendung
st.title("SSV 1928 e.V. Sulzbach")
st.write("Teams")

# Überschrift "Teams bilden"
st.header("Teams bilden")

# Laden der Wettbewerbe aus der JSON-Datei
try:
    with open("wettbewerbe.json", "r", encoding="utf-8") as file:
        wettbewerbe = json.load(file)
except FileNotFoundError:
    st.error("Die Datei 'wettbewerbe.json' wurde nicht gefunden.")
    wettbewerbe = []

# Überprüfen, ob die JSON-Datei die erwartete Struktur hat
if isinstance(wettbewerbe, list) and all(isinstance(item, dict) for item in wettbewerbe):
    # Extrahieren der Wettbewerbsnamen für das Dropdown
    wettbewerbe_namen = [wettbewerb.get("name", "Unbekannter Wettbewerb") for wettbewerb in wettbewerbe]
else:
    st.error("Die JSON-Datei hat nicht das erwartete Format.")
    wettbewerbe_namen = []

# Dropdown-Menü zur Auswahl des Wettbewerbs
if wettbewerbe_namen:
    ausgewaehlter_wettbewerb = st.selectbox(
        "Wettbewerb auswählen",
        wettbewerbe_namen,
        index=0,  # Standardmäßig der erste Eintrag
    )
    st.write(f"Du hast den Wettbewerb ausgewählt: **{ausgewaehlter_wettbewerb}**")
else:
    st.write("Keine Wettbewerbe verfügbar.")