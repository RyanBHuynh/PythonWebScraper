import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://bsd.sos.mo.gov/BusinessEntity/BESearch.aspx"

page = urlopen(url)
print(page)

html_bytes = page.read()
html = html_bytes.decode("UTF-8")
print(html)
