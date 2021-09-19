import streamlit as st

from scrapping.config import countries
from scrapping.the_hub import get_job_hub

FLAGS = {x: "flag-" + x.lower() for x in countries}


def header() -> None:
    """Header of streamlit app."""
    st.title("Where should I apply?")


def build_row(job: dict):
    col1, col2, col3 = st.columns([3, 10, 1])
    col1.image(job["image"])
    col2.write(f"[{job['title']}]({job['url']})")
    col3.write(f":{FLAGS[job['country']]}:")


if __name__ == "__main__":
    header()
    jobs = get_job_hub()
    for job in jobs:
        build_row(job)
