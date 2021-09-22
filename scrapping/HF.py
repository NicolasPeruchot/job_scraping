import pandas as pd
from gazpacho import Soup, get

HF_url = "https://www.hellofresh.com.au/careers/team/data-science-business-intelligence-7043"


def get_job_HF():

    html = get(HF_url)
    soup = Soup(html)

    titles = []
    places = []
    for job in soup.find("div", {"class": "fela-_1y1x7xu"}):
        title = job.find("a", {"class": "fela-_eumwml"}).text
        if "Intern" in title:
            titles.append(title)
            places.append(job.find("div", {"class": "fela-_17b356z"}).text)

    return pd.DataFrame({"Title": titles, "City": places})
