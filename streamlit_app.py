import datetime
import streamlit as st

st.title("My new app")

lastPlayed = datetime.date(2025, 1,2)

st.write(lastPlayed.strftime('%d %B %Y'))

