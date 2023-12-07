import requests
from bs4 import BeautifulSoup as BS

def parse(url):
    r = requests.get(url)
    progres = 1
    html = BS(r.content, 'html.parser')
    for element in html.find_all("div", class_ = "track__info-r"):
        d_link = element.find("a")["href"]
        name = d_link.split("/")[-1]

        try:
            song = requests.get(d_link)
            with open(f"songs/{name}", "wb") as file:
                file.write(song.content)
            print(progres)
            progres+=1
        except Exception as error:
            print(error)


url = "https://rur.hitmotop.com/search?q=lofi"
parse(url)
for page in range(48 ,48*9,48):
    print("Page: ", page//48)
    url = f"https://rur.hitmotop.com/search/start/{page}?q=lofi"
    parse(url)