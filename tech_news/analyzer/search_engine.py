from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    find = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )

    return [(item["title"], item["url"]) for item in find]


# Requisito 7
def search_by_date(date):
    try:
        find_by_date = list()
        date = datetime.strptime(date, '%Y-%m-%d')
        default_date = datetime.strftime(date, '%d/%m/%Y')
        new_date = search_news({
            'timestamp': default_date
        })
        for date in new_date:
            find_by_date.append((date['title'], date['url']))

    except ValueError:
        raise ValueError('Data inválida')
    return find_by_date


# Requisito 8
def search_by_tag(tag):
    find = search_news(
        {"tags": {"$regex": tag, "$options": "i"}}
    )

    return [(item["title"], item["url"]) for item in find]


# Requisito 9
def search_by_category(category):
    find = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    return [(item["title"], item["url"]) for item in find]
