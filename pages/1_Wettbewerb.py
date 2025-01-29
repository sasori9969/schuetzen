import streamlit as st
import json

def speichern_wettbewerb(wettbewerb):
    """Speichert den Wettkampf in einer JSON-Datei.

    Args:
        wettbewerb: Ein Wörterbuch mit den Wettkampfdaten.
    """

    data = {
        "wettbewerbsname": wettbewerbsname,
        "datum": str(datum),
        "distanz": distanz,
        "disziplin": disziplin
    }

    try:
        with open('wettbewerbe.json', 'r+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            data.append(wettbewerb)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
    except (IOError, OSError) as e:
        st.error(f"Fehler beim Speichern des Wettbewerbs: {e}")

def anzeigen_wettbewerbe():
    """Zeigt alle gespeicherten Wettbewerbe an."""
    try:
        with open('wettbewerbe.json', 'r') as f:
            data = json.load(f)
            return data
    except (IOError, OSError) as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
    return []

def loesche_wettbewerb(index):
    """Löscht einen Wettkampf aus der JSON-Datei.

    Args:
        index: Der Index des zu löschenden Wettbewerbs.
    """

    try:
        with open('wettbewerbe.json', 'r+') as f:
            data = json.load(f)
            del data[index]
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
        st.success("Wettbewerb erfolgreich gelöscht!")
    except (IOError, OSError, IndexError) as e:
        st.error(f"Fehler beim Löschen des Wettbewerbs: {e}")

def anzeigen_wettbewerbe_mit_kaechen():
    """Zeigt alle gespeicherten Wettbewerbe in einer Kachelansicht an."""
    wettbewerbe = anzeigen_wettbewerbe()
    if wettbewerbe:
        col1, col2, col3 = st.columns(3)  # Anpassbar an die gewünschte Anzahl von Spalten

        with st.container():
            st.html("""
            <style>
                .stContainer {
                    border: 1px solid #ccc;
                    padding: 10px;
                    margin: 10px;
                    border-radius: 5px;
                    background-color: #f9f9f9;
                }
            </style>
            """)

        for i, wettbewerb in enumerate(wettbewerbe):
            with st.container():
                st.markdown(f"### Wettkampf {i+1}")
                st.write(f"**Name:** {wettbewerb['wettbewerbsname']}")
                st.write(f"**Datum:** {wettbewerb['datum']}")
                st.write(f"**Distanz:** {wettbewerb['distanz']}")
                st.write(f"**Disziplin:** {wettbewerb['disziplin']}")

                # Button zum Löschen
                if st.button("Löschen", key=f"delete_{i}"):
                    if st.button("Bestätigen?"):
                        loesche_wettbewerb(i)
                        st.experimental_rerun()  # Aktualisiert die Seite
    else:
        st.write("Keine Wettbewerbe gespeichert.")

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
    wettbewerb = {
        "wettbewerbsname": wettbewerbsname,
        "datum": str(datum),
        "distanz": distanz,
        "disziplin": disziplin
    }
    speichern_wettbewerb(wettbewerb)

# Button zum Anzeigen
if st.button("Wettbewerbe anzeigen (Kacheln)"):
    anzeigen_wettbewerbe_mit_kaechen()