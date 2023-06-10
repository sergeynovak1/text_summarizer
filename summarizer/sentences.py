import requests
from bs4 import BeautifulSoup


def parse_wikipedia_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлекаем заголовок страницы
    title = soup.find('h1', {'class': 'firstHeading'}).text.strip()

    # Извлекаем основной текст страницы
    content_div = soup.find('div', {'id': 'mw-content-text'})
    paragraphs = content_div.find_all('p')
    text = '\n'.join([p.text for p in paragraphs])

    return f'{title}\n\n\n{text}'
