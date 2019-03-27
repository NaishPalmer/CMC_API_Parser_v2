import time, requests, json
import datetime as dt
import gtts
from gtts import gTTS
import os
import touchphat

touchphat.all_on()
def fetch(price):
   language='en-us'
   myob=gTTS(text=(price + 'dollar'),lang=language,slow=False)
   myob.save('price_usd.mp3')
   


def play():
      from pygame import mixer
      mixer.init()
      mixer.music.load("price_usd.mp3")
      mixer.music.play()
     

def bitcoin_price():
   url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC&convert=USD'
   headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'deflate, gzip',
    'X-CMC_PRO_API_KEY': 'YOUR-API-KEY-HERE',
   }
   r = requests.get(url, headers=headers)
   if r.status_code == 200:
      response = json.loads(r.text)
   price_usd = ("{0:.2f}".format((response['data']['BTC']['quote']['USD']['price'])))
   market_cap_usd = ("{0:.2f}".format((response['data']['BTC']['quote']['USD']['market_cap'])))
   cryptocurrency_name = response['data']['BTC']['slug']
   fetch('The price of 1 Bitcoin is' + price_usd)
   play()



def ethereum_price():
   url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=ETH&convert=USD'
   headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'deflate, gzip',
    'X-CMC_PRO_API_KEY': 'd49c4a54-e879-4f24-8a73-af853d3d444f',
   }
   r = requests.get(url, headers=headers)
   if r.status_code == 200:
      response = json.loads(r.text)
   price_usd = ("{0:.2f}".format((response['data']['ETH']['quote']['USD']['price'])))
   market_cap_usd = ("{0:.2f}".format((response['data']['ETH']['quote']['USD']['market_cap'])))
   cryptocurrency_name = response['data']['ETH']['slug']
   fetch('The price of 1 Ethereum is' + price_usd)
   play()
   

def ripple_price():
   url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=XRP&convert=USD'
   headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'deflate, gzip',
    'X-CMC_PRO_API_KEY': 'd49c4a54-e879-4f24-8a73-af853d3d444f',
   }
   r = requests.get(url, headers=headers)
   if r.status_code == 200:
      response = json.loads(r.text)
   price_usd = ("{0:.2f}".format((response['data']['XRP']['quote']['USD']['price'])))
   market_cap_usd = ("{0:.2f}".format((response['data']['XRP']['quote']['USD']['market_cap'])))
   cryptocurrency_name = response['data']['XRP']['slug']
   fetch('The price of 1 Ripple is' + price_usd)
   play()
 
   

def chainlink_price():
   url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=LINK&convert=USD'
   headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'deflate, gzip',
    'X-CMC_PRO_API_KEY': 'd49c4a54-e879-4f24-8a73-af853d3d444f',
   }
   r = requests.get(url, headers=headers)
   if r.status_code == 200:
      response = json.loads(r.text)
   price_usd = ("{0:.2f}".format((response['data']['LINK']['quote']['USD']['price'])))
   market_cap_usd = ("{0:.2f}".format((response['data']['LINK']['quote']['USD']['market_cap'])))
   cryptocurrency_name = response['data']['LINK']['slug']
   fetch('The price of 1 LINK Token is' + price_usd)
   play()


