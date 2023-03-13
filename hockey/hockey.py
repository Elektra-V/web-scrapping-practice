import requests
import json
from unidecode import unidecode
from selectolax.parser import HTMLParser


def main():
    session = requests.Session()
    
    teams = []

    response = session.get(url="https://www.scrapethissite.com/pages/forms/")
    html = response.text

    #with open("raw.html", "w") as file:
        #file.write(html)

    tree = HTMLParser(html)



    for element in tree.css("tr.team"):
        team = {
            "Team Name" : element.css_first("td.name").text().strip(),
            "Year" : element.css_first("td.year").text().strip(),
            "Wins" : element.css_first("td.wins").text().strip()
        }
        teams.append(team)
    print(teams)
    
if __name__ == "__main__":
    main()