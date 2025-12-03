import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

songs = soup.select("tr.lst50")

result = []
for s in songs[:10]:
    title = s.select_one("div.ellipsis.rank01 a").text.strip()
    artist = s.select_one("div.ellipsis.rank02 span").text.strip()
    result.append((title, artist))

for i, (title, artist) in enumerate(result, 1):
    print(f"{i}위: {title} - {artist}")
