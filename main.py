import requests
from bs4 import BeautifulSoup

s = requests.Session()

url = "https://bsd.sos.mo.gov/BusinessEntity/BESearch.aspx"
#page = s.get(url)
requests.post(url)
#print(page.text)