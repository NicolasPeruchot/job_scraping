import webbrowser

from gazpacho import Soup, get

from scrapping.config import countries, matches

hub_url = "https://thehub.io"
job = {code: [] for code in countries}
for code in countries:
    again = True
    page = 1
    url = hub_url + f"/jobs?roles=datascience&countryCode={code}&sorting=mostPopular&page={page}"
    html = get(url)
    soup = Soup(html)
    jobs = soup.find("div", {"class": "my-10"})
    if again is False:
        continue
    for job in jobs:
        if any(
            x in job.find("span", {"class": "card-job-find-list__position"}).text for x in matches
        ):
            url = hub_url + job.find("a", {"class": "card-job-find-list__link"}).attrs["href"]
            webbrowser.open(url)
