import requests
import json
from unidecode import unidecode
from selectolax.parser import HTMLParser



def main():
    url = "https://www.scrapethissite.com/pages/simple/"
    session = requests.Session()
    response = session.get(url)
    html = response.text

    with open("raw.html", "w") as file:
        file.write(html)
    
    tree = HTMLParser(html)

    countries_list = []

    countries = [element.text() for element in tree.css("h3.country-name")]
    capitals = [element.text() for element in tree.css("span.country-capital")]
    population = [element.text() for element in tree.css("span.country-population")]

    for i, country in enumerate(countries):
        country = {
            "country" : unidecode(country.strip()),
            "capital" : unidecode(capitals[i].strip()),
            "population" : unidecode(population[i].strip())

        }
        countries_list.append(country)
    
    with open("countries.json", "w") as file:
        file.write(json.dumps(countries_list))
    


if __name__ == "__main__":
    main()   