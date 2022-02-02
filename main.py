import requests
from bs4 import BeautifulSoup

url = "https://bsd.sos.mo.gov/BusinessEntity/BESearch.aspx"
page = requests.get(url)
print(page.text)