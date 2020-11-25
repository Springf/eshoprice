import requests
from requests.utils import quote
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def Handler(event, context):
    game_list = event['game_list']
    print(game_list[0])
    response = requests.get(f'https://eshop-prices.com/games?currency=SGD&q={quote(game_list[1])}' , headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    discount = soup.find('span', {'class': 'discount'})
    price = soup.find('span', {'class': 'price-tag'})
    if discount != None:
        print(discount.text)
        print(price.contents[2])
    print(price.contents[0])
    #print(soup.prettify())
