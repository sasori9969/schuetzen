import streamlit as st

# Titel der Anwendung
st.title("SSV 1928 e.V. Sulzbach")
st.write("Teams")

# Überschrift "Teams bilden"
st.header("Teams bilden")

# Überprüfen, ob der Wettkampfname bereits im Session State gespeichert ist
if 'wettkampf_name' not in st.session_state:
    st.session_state['wettkampf_name'] = ""

# Eingabefeld für den Namen des Wettkampfes
wettkampf_name = st.text_input("Name des Wettkampfes", st.session_state['wettkampf_name'])

# Speichern des eingegebenen Namens im Session State
st.session_state['wettkampf_name'] = wettkampf_name

# Anzeigen des gespeicherten Wettkampfnamens unter der Überschrift
if st.session_state['wettkampf_name']:
    st.write(f"Wettkampf: {st.session_state['wettkampf_name']}")