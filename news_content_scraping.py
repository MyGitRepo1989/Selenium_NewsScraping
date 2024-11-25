''' if you want to do classification add this
import transformers
from transformers import pipeline
classifier = pipeline("text-classification", model="classla/multilingual-IPTC-news-topic-classifier", device=-1, max_length=512, truncation=True)
'''
# get your chromedriver from you that is compatible with your chrome
#https://developer.chrome.com/docs/chromedriver/downloads#chromedriver_1140573516

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import json
import datetime
from datetime import date


# Path to chromedriver
chrome_driver_path = "./chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

def scrapdailynews(dailynewslinks_csv):
    # Read the CSV file
    df = pd.read_csv(dailynewslinks_csv)

    # Create a list to store the scraped content
    content_scraped = []

    # Iterate through URLs
    for url in df['URL']:
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        try:
            # Open the website
            driver.get(url)
            
            # Extract all <p> elements and save the text in a list
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            paragraph_texts = [p.text for p in paragraphs if p.text.strip()]  # Remove empty texts
            print(paragraph_texts)
            content_scraped.append(" ".join(paragraph_texts))  # Combine all paragraphs into a single string
        except Exception as e:
            content_scraped.append(None)  # Use None for errors
            print(f"Not able to get content for URL {url}: {e}")
            
        driver.quit()

        # Close the browser


    # Add scraped content to the DataFrame
    df['content_scraped'] = content_scraped
    
    #get todays date and save the CSV
    today = date.today()
    formatted_date = today.strftime("%d%b%Y")

    # Save the updated DataFrame to a new CSV file
    df.to_csv(formatted_date + "news_content.csv", index=False,header=True)

    print("Scraping completed and saved to new_content.csv.")
    
if __name__=="__main__":
    dailynewslinks_csv = "23Nov2024news.csv"
    scrapdailynews(dailynewslinks_csv)
