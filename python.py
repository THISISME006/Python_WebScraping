import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Albert_Einstein"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

content_section = soup.find(id="mw-content-text")

titles = []
paragraphs = []

for section in content_section.find_all(["h2","h3"]):
	title = section.get_text(strip=True)
	titles.append(title)
	paragraph = ""
	next_sibling = section.find_next_sibling()
	while next_sibling and next_sibling.name not in ["h2","h3"]:
		if next_sibling.name == "p":
			paragraph+=next_sibling.get_text(strip=True)+""
		next_sibling = next_sibling.find_next_sibling()
	paragraphs.append(paragraph.strip())

data = []

for i in range(len(titles)):
	data.append({
        "title": titles[i],
        "paragraph": paragraphs[i]
    })

for entry in data:
	print("Title:", entry["title"])
	print("Paragraph:", entry["paragraph"])
	print()
		
