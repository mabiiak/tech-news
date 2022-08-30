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

    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "comments_count": len(selector.css(".post-comments").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) ::text").getall()
        ).strip(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css(".label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
