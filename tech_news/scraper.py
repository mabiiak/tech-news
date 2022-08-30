import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list_links = selector.css(".archive-main h2 a::attr(href)").getall()
    if not list_links:
        return []
    return list_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link_button = selector.css(".nav-links .next::attr(href)").get()
    return link_button


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    # url
    link_page = selector.css("link[rel=canonical]::attr(href)").get()

    # title
    title_noticia = selector.css(".entry-title::text").get()

    # timestamp
    all_date_noticia = selector.css(".post-modified-info::text").get()
    format_data = all_date_noticia.split()
    day_create = format_data[0]

    # author
    author_noticia = selector.css(".author .url::text").get()

    # comments
    div_comments = selector.css(".post-comments").getall()
    comments_noticia = selector.css(".comment-body").getall()
    count_comments = len(comments_noticia)

    if not div_comments:
        count_comments = 0

    # paragraph
    all_text = selector.css(".entry-content p::text").getall()

    # tags
    tags_noticia = selector.css(".post-outer .label::text").getall()

    # category
    category_noticia = selector.css(".category-style .label::text").get()

    info = {
        "url": link_page,
        "title": title_noticia,
        "timestamp": day_create,
        "writer": author_noticia,
        "comments_count": count_comments,
        "summary": all_text[0],
        "tags": tags_noticia,
        "category": category_noticia,
    }

    # print(info)
    print(tags_noticia)
    return info


scrape_noticia(
    fetch(
        "https://blog.betrybe.com/carreira/passos-fundamentais-para-aprender-a-programar/"
        # "https://blog.betrybe.com/carreira/rescisao-indireta/"
    )
)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
