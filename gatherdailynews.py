#!pip install newsapi-python
import requests
import newsapi
from newsapi import NewsApiClient
import json
import pandas as pd
import datetime
from datetime import date


def get_todays_news(key):
    # get the news articles
    url = url = f"https://newsapi.org/v2/top-headlines?" \
      f"country=us&" \
      f"apiKey={key}"
    response = requests.get(url)
    data =response.json()
    
    # Assuming `data` contains your API response and `classifier` processes content
    results_list = []

    for news in data['articles']:
        title = news.get('title', None)
        content = news.get('content', None)
        url = news.get('url', None)

        # Append the extracted information to results_list
        results_list.append({
            'Title': title,
            'Content': content,
            'URL': url
        })

    # Convert the results_list to a DataFrame
    df = pd.DataFrame(results_list)
    
    #get todays date and save the CSV
    today = date.today()
    formatted_date = today.strftime("%d%b%Y")
    
    #save the csv
    df.to_csv(str(formatted_date)+'news.csv', index = False , header=True)

   
if __name__ =="__main__":
    key = "c6dcf4ea69ea47b88bca4466ef339df5"
    #key2='d0542c7bbc2448959d240afb54beed71'
    #key = "your key here"
    get_todays_news(key)