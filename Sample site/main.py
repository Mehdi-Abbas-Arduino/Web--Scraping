import requests
from bs4 import BeautifulSoup
import html.parser

r = requests.get("https://www.theakikhan.com/")

with open("aqib_khan.html",'w') as f:
    content = r.text
    f.write(content)