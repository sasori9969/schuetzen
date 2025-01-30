import streamlit as st

st.title("SSV 1928 e.V. Sulzbach")
st.write(
    "Schützen"
)

container1 = st.container(border=True)
container1.write("Mannschaft erstellen")
container1.text_input("Mannschaftsname")
container1.button("Speichern")

container2 = st.container(border=True)
container2.write("Schützen anlegen")
container2.text_input("Vorname")
container2.text_input("Name")
container2.button("Speichernn")
