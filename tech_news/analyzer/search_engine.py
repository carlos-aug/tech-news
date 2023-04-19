from tech_news.database import search_news
import datetime


# Requisito 7
def search_by_title(title):
    regex = {"title": {"$regex": title, "$options": "i"}}
    query = search_news(regex)
    news_list = []
    for i in query:
        news_list.append((i["title"], i["url"]))
    return news_list


# Requisito 8
def search_by_date(date):
    try:
        dt = datetime.datetime.strptime(date, "%Y-%m-%d")
        date_str = dt.strftime("%d/%m/%Y")

        news = search_news({"timestamp": {"$regex": f"^{date_str}"}})

        return [(i["title"], i["url"]) for i in news]

    except ValueError:

        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    regex = {"category": {"$regex": category, "$options": "i"}}
    query = search_news(regex)
    news_list = []
    for i in query:
        news_list.append((i["title"], i["url"]))
    return news_list
