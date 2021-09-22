from gazpacho import Soup, get

from scrapping.config import countries, matches


def get_job_hub():
    results = []
    hub_url = "https://thehub.io"
    job = {code: [] for code in countries}
    for code in countries:
        again = True
        page = 0
        while again:

            page += 1
            url = (
                hub_url
                + f"/jobs?roles=datascience&countryCode={code}&sorting=mostPopular&page={page}"
            )
            html = get(url)
            soup = Soup(html)
            jobs = soup.find("div", {"class": "my-10"})
            if "No search" in soup.html:
                again = False
            if again is False:
                continue
            for job in jobs:
                if any(x in job.find("span")[-1].text.lower() for x in matches):
                    title = job.find("span", {"class": "card-job-find-list__position"}).text
                    url = (
                        hub_url + job.find("a", {"class": "card-job-find-list__link"}).attrs["href"]
                    )
                    html_job = get(url)
                    soup_job = Soup(html_job)
                    A = soup_job.find(
                        "div",
                        {
                            "class": (
                                "media-item__image media-item__image--image--big"
                                " media-item__image--gap--default"
                            )
                        },
                    ).html
                    begin = A.find("http")
                    end = A.find(")")
                    img = A[begin:end]
                    results.append({"title": title, "url": url, "image": img, "country": code})

    return results
