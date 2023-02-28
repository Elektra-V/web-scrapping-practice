import requests
import json
from unidecode import unidecode
from selectolax.parser import HTMLParser
import time


def main():
    books = []
    for index in range(1, 51):
        time.sleep(1)
        url = f"http://books.toscrape.com/catalogue/page-{index}.html"
        response = requests.get(url=url)
        html = response.text

        tree = HTMLParser(html)

        titles = [element.text() for element in tree.css("h3 a")]
        prices = [element.text() for element in tree.css("p.price_color")]
        images_url = [element.attributes["src"] for element in tree.css("img.thumbnail")]
        ratings = [element.attributes["class"] for element in tree.css("p.star-rating")]

        for i, title in enumerate(titles):
            book = {
                "title": title,
                "price": unidecode(prices[i]).replace("APS", ""),
                "image_url": f"http://books.toscrape.com/{images_url[i]}",
                "star_rating" : ratings[i].replace("star-rating", "").lstrip()
            }
            books.append(book)

    with open("books.json", "w") as file:
        file.write(json.dumps(books))


if __name__ == "__main__":
    main()