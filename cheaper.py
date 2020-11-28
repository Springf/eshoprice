import requests
from requests.utils import quote
from bs4 import BeautifulSoup
import boto3

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def Handler(event, context):
    game_list = event['game_list']
    for g in game_list:
        print(f'checking game {g} ... ')
        response = requests.get(f'https://eshop-prices.com/games?currency=SGD&q={quote(g)}' , headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        games = soup.findAll('div', {'class': 'games-list-item-content'})
        
        sns = boto3.client('sns')

        for game in games:
            title = game.findChild("h5" , recursive=True).text
            if title == g or title.replace(u"\u2122", '') == g:
                discount = game.findChild('span', {'class': 'discount'})
                price = game.findChild('span', {'class': 'price-tag'})
                if discount != None:
                    message = f'Got Discount {discount.text.strip()}, now @ {price.contents[2].strip()}!'
                    print(message)
                    # response = sns.publish(
                    # TopicArn='arn:aws:sns:ap-southeast-1:872764013972:company_annoucement',    
                    # Message= message,
                    # Subject = g)
                    # print(f'Sent: {response}')
                else:
                    print('No discount found.')
