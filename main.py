import streamlit as st
import re
from datetime import date

import requests

BASE_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
st.title("🔭 Space picture of the day")
st.caption("Source: NASA APOD (science.nasa.gov)")


def fetch_apod(timeout: float = 8) -> dict:
    r = requests.get(BASE_URL, timeout=timeout)
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



apod = ans

st.subheader("Title:", apod["title"])
st.write("Explanation:", apod["explanation"])
st.write("Credit:", apod["credit"])

st.image(apod["hdurl"])