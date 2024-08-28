import streamlit as st

try:
    open(".streamlit/config.toml", "w").write(open("theme.txt", 'r').read())
except Exception as e:
    st.write(e)
