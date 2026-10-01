import streamlit as st

import requests

st.title("a")
def fetch_apod(pick_date: date, timeout: float = 8) -> dict:
    """Date goes in the path as YYMMDD, e.g. 2026-09-29 -> 260929. 404 if no entry."""
    r = requests.get(f"{BASE_URL}/{pick_date.strftime('%y%m%d')}", timeout=timeout)
    r.raise_for_status()
    return r.json()