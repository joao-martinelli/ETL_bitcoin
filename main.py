#LIBRARIES

import requests
import time 
import os
from coinbase.wallet.client import Client # for interacting with coinbase API
from dotenv import load_dotenv #for using environmental variables 
#import psycopg2 # for creating python-postgres connection 
from datetime import datetime 

def main():
    
    
    #cursor = connection.cursor() 

    # EXTRACT + TRANSFORM 

    #establishing connection to coinbase API with credentials 
    client = Client(api_key, api_secret)
    coins = ['BTC-USD', 'ETH-USD']
    #creating function to pull price data from coinbase API using client 
    def spot_price(client, c_pair): 
        # Fetch the spot price for a given currency pair
        return client.get_spot_price(currency_pair=c_pair)
    def buy_price(client, c_pair): 
        # Fetch the spot price for a given currency pair
        return client.get_buy_price(currency_pair=c_pair)
        
    try:

        #creating dictionary of 3 coins by calling spot_price function
        prices = {i: buy_price(client, i) for i in coins}

        #throw an error if any coin data is not available
        if any(not price for price in prices.values()):
            raise ValueError("Incomplete data received from API")
        print(prices)
        

    # LOAD 

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        

main()
    
    
