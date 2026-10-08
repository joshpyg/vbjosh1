import streamlit as st
import re
from datetime import date

import requests

BASE_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
st.title("🔭 Space picture of the day")
st.caption("Source: NASA APOD (science.nasa.gov)")


# if st.button("Show picture"):
#     st.subheader(f"{info['title']}  ({info['date']})")
#     if info["image_url"]:
#         st.image(info["image_url"], width="stretch")
#     else:
#         st.info("No image file for this date - see the page below.")
#     st.write(info["explanation"])
#     st.caption("© " + info["copyright"] if info["copyright"] else "Public domain (NASA)")
#     st.markdown(f"[Open on nasa's site]({info['page_url']})")

def fetch_apod(date, timeout: float = 6):
    date = str(date)
    date = date.replace("-", "")
    date = date[2:]
    final_URL = BASE_URL + "/" + date
    r = requests.get(
        final_URL,
        params={"api_key": "DEMO_KEY"},
        timeout=timeout
    )
    r.raise_for_status()
    return r.json()

date = st.date_input("Date")
st.write(date)

if st.button("Show picture"):
    ans = fetch_apod(date)
    st.write("Title:", ans["title"])
    st.write("Explanation:", ans["explanation"])
    st.image(ans["hdurl"])

st.write("https://science.nasa.gov/wp-json/wp/v2/apod-basic")