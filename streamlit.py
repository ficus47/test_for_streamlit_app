import streamlit as st

try:
    open(".streamlit/config.toml", "w").write("""
    [theme]
    primaryColor="#120ca0"
    backgroundColor="#0d6364"
    secondaryBackgroundColor="#2d0431"
    textColor="#fbd1d1"
""")
except Exception as e:
    st.write(e)