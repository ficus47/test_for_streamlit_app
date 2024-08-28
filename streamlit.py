import streamlit as st

#try:
#    open(".streamlit/config.toml", "a").write(open("theme.txt", 'r').read())
#except Exception as e:
#    st.write(e)

st.set_page_config(theme={"primaryColor":"#120ca0",
                          "backgroundColor":"#0d6364",
                          "secondaryBackgroundColor":"#2d0431",
                          "textColor":"#fbd1d1"}
