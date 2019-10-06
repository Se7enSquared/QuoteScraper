import requests

quotes_page = requests.get('http://quotes.toscrape.com/')
print(quotes_page)