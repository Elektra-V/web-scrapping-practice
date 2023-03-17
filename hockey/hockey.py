import requests
import json
from unidecode import unidecode
from selectolax.parser import HTMLParser


def main():
    session = requests.Session()
    
    teams = []
    index = 1
    while True:
        response = session.get(url=f"https://www.scrapethissite.com/pages/forms/?page_num={index}&per_page=25")
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
        
        if index > 24:
            break

        index += 1
        print(teams)
        
if __name__ == "__main__":
    main()