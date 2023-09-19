import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://8.208.84.236:8080", 
    "https": "http://8.208.84.236:8080",
}


url = "https://in.indeed.com/jobs?q=python+developer&advn=5986286851620397&vjk=06d4e363f24b7a19&from=mobRdr&l="


response = requests.get(url, proxies=proxies)

soup = BeautifulSoup(response.content, "html.parser")


target_div = soup.find("div", class_="jobTitle css-1u6tfqq eu4oa1w0")

if target_div:
    print(target_div.prettify())
else:
    print("Div not found.")