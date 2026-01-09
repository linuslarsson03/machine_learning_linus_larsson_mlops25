import streamlit as st
from pathlib import Path

book_path = Path(__file__).parents[1] / "assets" / "fastapi_book.png"

st.markdown("# App front page")

st.image(book_path)