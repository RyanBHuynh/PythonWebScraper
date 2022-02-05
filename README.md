# PythonWebScraper
## Ryan Huynh

A simple Python web scraper that grabs business info from the first two pages in Missouri’s Business Entity Search Tool for businesses that start with the letter A. 

The program makes a POST request for each page and stores the response in an HTML file. The data from each HTML file is formatted and stored in a separate CSV file.

## Installing necessary packages

Make sure you have these Python packages installed:
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests](https://docs.python-requests.org/en/latest/)

To install the Python packages, first install [pip](https://pip.pypa.io/en/stable/).

In order to use pip to install the packages, run these commands in your terminal:

`pip install requests`

`pip install beautifulsoup4`

## Running the program
To run the program, extract the zip file or clone the repository into your directory of choice.
Then, change directory to that repository and run the following command:

`python3 main.py`
