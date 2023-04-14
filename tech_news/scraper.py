import requests
import time
from parsel import Selector

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
    links = selector.css("header h2 > a::attr(href)").get()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next ::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    url = "https://blog.betrybe.com/"
    print(scrape_next_page_link(fetch(url)))
