import requests
# import urllib3

# urllib3.disable_warnings()

proxies = {
    "http": "http://8.208.84.236:8080", 
    "https": "http://8.208.84.236:8080",
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def fetchAndSave(url, path):
    r = requests.get(url, headers=headers)
    # r = requests.get(url, verify=False, proxies=proxies)
    with open(path, "w") as f:
        f.write(r.text)

# url = "https://in.indeed.com/?r=us"
url = "https://www.amazon.in/s?k=smartphones"
# url = "https://in.indeed.com/jobs?q=python+developer&l=&from=searchOnHP&vjk=a872478789aa35c4"
fetchAndSave(url, "data/sample8.html")