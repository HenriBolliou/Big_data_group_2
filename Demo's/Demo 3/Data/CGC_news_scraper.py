"""
A web scraper for Canadian Gold Corp news articles using Selenium.
Saves scraped articles to a JSON file, appending new articles while avoiding duplicates.
SelectorGadget: https://selectorgadget.com/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json
import os

def scrape_cgc_news():
    # Initialize the driver
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    #driver.get("https://canadiangoldcorp.com/news-releases-2025/")
    driver.get("https://canadiangoldcorp.com/news-2024/")
    
    wait = WebDriverWait(driver, 10)
    articles_data = []
    
    try:
        # You can find the CSS selectors by using SelectorGadget or inspecting the webpage
        article_links = driver.find_elements(By.CSS_SELECTOR, ".wp-show-posts-entry-title a")
        article_dates_elements = driver.find_elements(By.CSS_SELECTOR, ".published")
        article_urls = [link.get_attribute('href') for link in article_links]
        article_dates = [date.text for date in article_dates_elements]
        
        print(f"Found {len(article_urls)} articles to scrape")

        # Navigate to each article URL and extract data
        for idx, url in enumerate(article_urls):
            driver.get(url)
            time.sleep(2)  # Wait for page load
            
            try:
                title = driver.find_element(By.CSS_SELECTOR, "#primary .ut-flowtyped").text
                #content = driver.find_element(By.CSS_SELECTOR, ".category-78").text # for 2025
                content = driver.find_element(By.CSS_SELECTOR, ".category-77").text # for 2024
                
                articles_data.append({
                    'title': title,
                    'date': article_dates[idx] if idx < len(article_dates) else "Unknown",
                    'content': content,
                    'url': url
                })
                
                print(f"Scraped: {title}")
            except Exception as e:
                print(f"Error scraping {url}: {e}")
        
        # Load existing data if file exists, otherwise start with empty list
        existing_data = []
        if os.path.exists('./Data/cgc_news.json'):
            try:
                with open('./Data/cgc_news.json', 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                print(f"Loaded {len(existing_data)} existing articles")
            except json.JSONDecodeError:
                print("Warning: Existing JSON file was invalid, starting fresh")
        
        # Combine existing and new data (avoiding duplicates based on URL)
        existing_urls = {article['url'] for article in existing_data}
        new_articles = [article for article in articles_data if article['url'] not in existing_urls]
        
        combined_data = existing_data + new_articles
        
        # Save combined data to JSON
        with open('./Data/cgc_news.json', 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, indent=2, ensure_ascii=False)
        
        print(f"Added {len(new_articles)} new articles. Total: {len(combined_data)} articles")
                
    finally:
        driver.quit()
    
    return articles_data

if __name__ == "__main__":
    articles = scrape_cgc_news()
    print(f"Scraped {len(articles)} articles")