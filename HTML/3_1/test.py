import requests
from bs4 import BeautifulSoup

baidu = requests.get("http://www.github.com")
content = baidu.text

soup = BeautifulSoup(content)
final = soup.select("head > title")
print (final)
