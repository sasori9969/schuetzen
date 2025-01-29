import streamlit as st
import json

def speichern_wettbewerb(wettbewerbsname, datum, distanz, disziplin):
    """Speichert die Wettkampfdaten in einer JSON-Datei.

    Args:
        wettbewerbsname: Der Name des Wettbewerbs.
        datum: Das Datum des Wettbewerbs.
        distanz: 10m, 25m, 50m.
        disziplin: Die Disziplin des Wettbewerbs.
    """

    data = {
        "wettbewerbsname": wettbewerbsname,
        "datum": str(datum),
        "distanz": distanz,
        "disziplin": disziplin
    }

    try:
        with open('wettbewerbe.json', 'a') as f:
            json.dump(data, f)
            f.write('\n')
    except (IOError, OSError) as e:
        st.error(f"Fehler beim Speichern: {e}")
    except json.JSONEncodeError as e:
        st.error(f"Fehler bei der JSON-Codierung: {e}")

def anzeigen_wettbewerbe():
    """Zeigt alle gespeicherten Wettbewerbe an."""
    try:
        with open('wettbewerbe.json', 'r') as f:
            data = []
            for line in f:
                data.append(json.loads(line))
            return data
    except (IOError, OSError) as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
    return []

# Streamlit-App
st.title("SSV 1928 e.V. Sulzbach")
st.write("Eingabe des Wettbewerbs")

# Eingabefelder
wettbewerbsname = st.text_input("Wettbewerbsname")
datum = st.date_input("Datum")
distanz = st.selectbox("Distanz", ["10m", "25m", "50m"])
disziplin = st.selectbox("Disziplin", ["Unterhebel", "KK", "Luftgewehr"])

# Button zum Speichern
if st.button("Wettbewerb speichern"):
    speichern_wettbewerb(wettbewerbsname, datum, distanz, disziplin)

# Button zum Anzeigen
if st.button("Wettbewerbe anzeigen"):
    wettbewerbe = anzeigen_wettbewerbe()
    if wettbewerbe:
        for wettbewerb in wettbewerbe:
            st.write(f"Wettbewerb: {wettbewerb['wettbewerbsname']}")
            st.write(f"Datum: {wettbewerb['datum']}")
            st.write(f"Distanz: {wettbewerb['distanz']}")
            st.write(f"Disziplin: {wettbewerb['disziplin']}")
    else:
        st.write("Keine Wettbewerbe gespeichert.")