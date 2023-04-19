from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
