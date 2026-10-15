# fetch.py: downloads a web page with the requests library
import requests

url = "https://books.toscrape.com"
try:
    response = requests.get(url, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Characters received: {len(response.text)}")
except requests.RequestException as error:
    print(f"Could not reach {url}: {error}") 