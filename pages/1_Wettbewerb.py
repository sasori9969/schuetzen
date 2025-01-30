import streamlit as st
import json

st.title("SSV 1928 e.V. Sulzbach")
st.write("Wettbewerb")

# Erstelle die Texteingabefelder und speichere die Labels separat
wettbewerb = st.text_input("Wettbewerb:")
disziplin = st.text_input("Disziplin:")
distanz = st.selectbox("Distanz:", ["10m", "25m", "50m"])
datum = st.date_input("Datum:")

# Liste der Labels
spalten_ueberschriften = ["Wettbewerb", "Disziplin", "Distanz", "Datum"]

# Leere Liste zum Speichern der Daten
data_list = []

def speichern():
    # Erstelle ein Python-Dictionary mit den eingegebenen Daten
    data = {
        "Wettbewerb": wettbewerb,
        "Disziplin": disziplin,
        "Distanz": distanz,
        "Datum": str(datum)
    }

    # Füge das Dictionary zur Liste hinzu
    data_list.append(data)

    # Speichere die gesamte Liste als JSON-Datei
    with open("wettbewerbe.json", "w") as f:
        json.dump(data_list, f)

    st.success("Daten erfolgreich gespeichert!")

# Button zum Speichern
st.button("Speichern", on_click=speichern)

def lade_daten():
    try:
        with open("wettbewerbe.json", "r") as f:
            global data_list
            data_list = json.load(f)
    except FileNotFoundError:
        data_list = []

    # Erstelle eine Liste von Listen, wobei jede innere Liste eine Zeile der Tabelle darstellt
#    data = [[d[col] for col in spalten_ueberschriften] for d in data_list]
    data = [[d[col] for col in spalten_ueberschriften] + [st.button("Löschen", key=f"delete_{i}")] for i, d in enumerate(data_list)]

    # Zeige die Tabelle an
    st.dataframe(data)

def loeschen(index):
    del data_list[index]
    with open("wettbewerbe.json", "w") as f:
        json.dump(data_list, f)
    lade_daten()

# Rufe die Funktion zum Laden der Daten beim ersten Laden der App auf
lade_daten()