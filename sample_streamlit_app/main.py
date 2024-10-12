import streamlit as st
import os
from App.UIcreate import Theme

page_title_str = "sample steamlit application"
st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title=page_title_str,

)
Theme().load_app()
