import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find_all("div"))
# <table class="jobCard_mainContent big6_visualChanges" cellpadding="0" cellspacing="0" role="presentation">