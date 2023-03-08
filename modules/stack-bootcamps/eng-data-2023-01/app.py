from ast import Str, Try
import json
from sqlite3 import Date
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, null
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Coins
from requests import Request, Session
from datetime import datetime
import pandas as pd


def check_if_valid_data(df: pd.DataFrame) -> bool:
    
    # Check if dataframe is empty
    if df.empty:
        print("\nDataframe empty. Finishing execution")
        return False 

    # Check for nulls
    if df.symbol.empty:
        raise Exception("\nSymbol is Null or the value is empty")
 
     # Check for nulls
    if df.price.empty:
        raise Exception("\nPrice is Null or the value is empty")

    # Check for nulls
    if df.data_added.empty:
        raise Exception("\nData is Null or the value is empty")

    return True
    
def load_data(table_name, coins_df, session_db, engine_db):
    
    # validate
    if check_if_valid_data(coins_df):
        print("\nData valid, proceed to Load stage")
    
    # load data on database
    try:
        coins_df.to_sql(table_name, engine_db, index=False, if_exists='append')
        print ('\nData Loaded on Database')

    except Exception as err:
        print(f"\nFail to load data on database: {err}")

    session_db.commit()
    session_db.close()
    print("\nClose database successfully")
    return session_db

def get_data(session_db, engine_db, start, limit, convert, key, url):
    
    # set limit of data from api
    parameters = {
        'start': start,
        'limit': limit,
        'convert': convert
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
    }

    # Session instance (request).
    session = Session()
    session.headers.update(headers)

    # Empty lists to persist data.
    name = []
    symbol = []
    data_added = []
    last_updated = []
    price = []
    volume_24h = []
    circulating_supply = []
    total_supply = []
    max_supply = []
    volume_24h = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []

    try:
        # Get data from API (url + parameters).
        response = session.get(url, params=parameters)
        data = json.loads(response.text) # Convert data (text) to JSON.

        print ('\n')
        for coin in data['data']:
            name.append(coin['name']) # Append to list "name".
            symbol.append(coin['symbol']) # Append to list "symbol".
            data_added.append(coin['date_added']) # Append to list "date_added".
            last_updated.append(coin['last_updated']) # Append to list "last_updated".
            circulating_supply.append(coin['circulating_supply']) # Append to list "circulating_supply".
            total_supply.append(coin['total_supply']) # Append to list "total_supply".
            max_supply.append(coin['max_supply']) # Append to list "max_supply".
            price.append(coin['quote']['USD']['price']) # Append to list "price".
            volume_24h.append(coin['quote']['USD']['volume_24h']) # Append to list "volume_24h".
            percent_change_1h.append(coin['quote']['USD']['percent_change_1h']) # Append to list "percent_change_1h".
            percent_change_24h.append(coin['quote']['USD']['percent_change_24h']) # Append to list "percent_change_24h".
            percent_change_7d.append(coin['quote']['USD']['percent_change_7d']) # Append to list "percent_change_7d".


        # Prepare a dictionary in order to turn it into a pandas dataframe below       
        coin_dict = {
            "name" : name,
            "symbol": symbol,
            "data_added" : data_added,
            "last_updated" : last_updated,
            "price": price,
            "volume_24h": volume_24h,
            "circulating_supply" : circulating_supply,
            "total_supply": total_supply,
            "max_supply": max_supply,
            "volume_24h": volume_24h,
            "percent_change_1h": percent_change_1h,
            "percent_change_24h": percent_change_24h,
            "percent_change_7d": percent_change_7d

        }
    except Exception as e:
        print (f'Error to get data from APi: {e}')
        exit(1) # Stop application.
    
    # create dataframe to structure data
    coins_df = pd.DataFrame(coin_dict, columns = ["name", "symbol", "data_added", "last_updated","price","volume_24h","circulating_supply","total_supply","max_supply","percent_change_1h","percent_change_24h","percent_change_7d"])
    print ("Data on Pandas Dataframe:\n")
    print(coins_df.head(100))
    
    # call the function to load data on database
    load_data('tb_coins',coins_df, session_db, engine_db)

# Declaration base
Base = declarative_base()

# Make the coin table
get_session_db, get_engine = Coins.start()

# call the get_data function and load data on database
get_data(get_session_db,
         get_engine,
         '1',
         '5000',
         'USD',
         '7e8d0c0c-187a-4e0e-830a-5bbc92a73486',
         'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest')
