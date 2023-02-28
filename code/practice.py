import requests
import json
from unidecode import unidecode
from selectolax.parser import HTMLParser



def main():
    url = "http://books.toscrape.com/"
    response = requests.get(url=url)
    html = response.text

    with open("raw.html", "w") as file:
        file.write(html)

    tree = HTMLParser(html)

    books = []

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