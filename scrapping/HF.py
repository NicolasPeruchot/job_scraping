import pandas as pd
from gazpacho import Soup, get

from scrapping.config import matches

url = "https://www.hellofresh.com.au/careers/team/data-science-business-intelligence-7043"

html = get(url)
soup = Soup(html)

titles = []
places = []
for job in soup.find("div", {"class": "fela-_1y1x7xu"}):
    title = job.find("a", {"class": "fela-_eumwml"}).text
    if any(x in title for x in matches):
        titles.append(title)
        places.append(job.find("div", {"class": "fela-_17b356z"}).text)

print(pd.DataFrame({"Title": titles, "City": places}))
