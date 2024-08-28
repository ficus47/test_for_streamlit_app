import streamlit as st

import os

# Dossier .streamlit et fichier config.toml
config_dir = ".streamlit"
config_file = "config.toml"

# Crée le dossier .streamlit s'il n'existe pas
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

# Contenu du fichier config.toml
config_content = """
[theme]
primaryColor = "#120ca0"
backgroundColor = "#0d6364"
secondaryBackgroundColor = "#2d0431"
textColor = "#fbd1d1"
"""

# Écrit le contenu dans le fichier config.toml
with open(os.path.join(config_dir, config_file), "w") as file:
    file.write(config_content)

st.write(f"Le fichier {config_file} a été créé/modifié avec succès.")
