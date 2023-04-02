import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.thehindu.com/brandhub/top-30-digital-marketing-agencies-in-india/article65255061.ece")
soup = BeautifulSoup(req.content, "html.parser")
# print(soup.prettify())
# print(req.content) => contails html webpage
# print(soup.prettify()) // we get intended page
# print(soup.get_text())
# res = soup.title
# print(res.get_text())
stuff = soup.find_all('ul', attrs={"class": 'article-body article-bullet-list'})
for ele in stuff:
    print(ele.text)