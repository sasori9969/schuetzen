import streamlit as st

# Titel der App
st.title("SSV 1928 e.V. Sulzbach")

# Abschnitt 1: Mannschaft erstellen
st.header("Mannschaft erstellen")
mannschaft_name = st.text_input("Mannschaftsname eingeben")
if st.button("Mannschaft speichern"):
    if mannschaft_name:
        st.success(f"Mannschaft '{mannschaft_name}' wurde erfolgreich erstellt!")
    else:
        st.error("Bitte gib einen Mannschaftsnamen ein.")

# Abschnitt 2: Schützen anlegen
st.header("Schützen anlegen")
schuetze_name = st.text_input("Nachname des Schützen eingeben")
schuetze_alter = st.text_input("Vorname des Schützen eingeben")
if st.button("Schützen speichern"):
    if schuetze_name and schuetze_alter:
        st.success(f"Schütze '{schuetze_name}' (Alter: {schuetze_alter}) wurde erfolgreich angelegt!")
    else:
        st.error("Bitte fülle alle Felder aus.")