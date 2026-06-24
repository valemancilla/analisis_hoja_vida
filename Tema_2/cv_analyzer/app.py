import os
import streamlit as st
from dotenv import load_dotenv
from ui.streamlit_ui import main

# Carga las variables del .env (incluida OPENAI_API_KEY) usando una ruta EXPLÍCITA
# basada en la ubicación de este archivo. Así funciona aunque sea Streamlit quien
# ejecute el script (find_dotenv() falla en ese caso).
RUTA_ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(RUTA_ENV)

if __name__ == "__main__":
    main()