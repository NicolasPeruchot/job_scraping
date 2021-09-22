import streamlit as st

from scrapping.config import countries
from scrapping.HF import get_job_HF
from scrapping.the_hub import get_job_hub

FLAGS = {x: "flag-" + x.lower() for x in countries}


def header() -> None:
    """Header of streamlit app."""
    st.title("Where should I apply?")


def build_hub_rows():
    jobs = get_job_hub()
    for job in jobs:
        col1, col2, col3 = st.columns([3, 7, 1])
        col1.image(job["image"])
        col2.write(f"[{job['title']}]({job['url']})")
        col3.write(f":{FLAGS[job['country']]}:")


def build_HF_rows():
    jobs = get_job_HF()
    for i, row in jobs.iterrows():
        col1, col2 = st.columns([5, 1])
        col1.write(row["Title"])
        col2.write(row["City"])


if __name__ == "__main__":
    header()
    st.write("## The Hub:")
    with st.spinner("Loading Hub jobs..."):
        build_hub_rows()
    st.write("## Hello Fresh:")
    with st.spinner("Loading HF jobs..."):
        build_HF_rows()
