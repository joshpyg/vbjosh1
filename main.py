import streamlit as st
import re
from datetime import date

import requests

BASE_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
st.title("🔭 Space picture of the day")
st.caption("Source: NASA APOD (science.nasa.gov)")


def fetch_apod(pick_date: date, timeout: float = 8) -> dict:
    """Date goes in the path as YYMMDD, e.g. 2026-09-29 -> 260929. 404 if no entry."""
    r = requests.get(f"{BASE_URL}/{pick_date.strftime('%y%m%d')}", timeout=timeout)
    r.raise_for_status()
    return r.json()

# if st.button("Show picture"):
#     st.subheader(f"{info['title']}  ({info['date']})")
#     if info["image_url"]:
#         st.image(info["image_url"], width="stretch")
#     else:
#         st.info("No image file for this date - see the page below.")
#     st.write(info["explanation"])
#     st.caption("© " + info["copyright"] if info["copyright"] else "Public domain (NASA)")
#     st.markdown(f"[Open on nasa's site]({info['page_url']})")

ans = fetch_apod()



apod = ans[0]

st.subheader("Title:", apod["title"])
st.write("Explanation:", apod["explanation"])
st.write("Credit:", apod["credit"])

st.image(apod["hdurl"])

