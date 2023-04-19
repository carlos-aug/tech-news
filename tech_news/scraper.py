import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    time.sleep(1)

    try:
        for _ in range(10):
            response = requests.get(url, headers=headers, timeout=3)
            if response.status_code == 200:
                return response.text
    except requests.exceptions.RequestException:
        pass
    return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links = selector.css("header h2 > a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):

    selector = Selector(text=html_content)
    url_link = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".fn > a::text").get().strip()
    reading_time = int(
        selector.css("li.meta-reading-time::text").get().split()[0]
    )
    summary = selector.css(
        "div.entry-content:first-of-type > p:nth-of-type(1) ::text"
    ).getall()
    summary = "".join(summary).strip()
    category = selector.css(".label::text").get().strip()

    new_dict = {
        "url": url_link,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }

    return new_dict


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    data_pages = fetch(url)
    data_links = []

    while len(data_links) < amount:
        data_links.extend(scrape_updates(data_pages))
        data_pages = fetch(scrape_next_page_link(data_pages))

    result_scrape = []
    for link in data_links[:amount]:
        fetch_links = fetch(link)
        result_scrape.append(scrape_news(fetch_links))

    create_news(result_scrape)
    return result_scrape


if __name__ == "__main__":
    url = "https://blog.betrybe.com"
    page_content = fetch(url)
    print(get_tech_news(5))
