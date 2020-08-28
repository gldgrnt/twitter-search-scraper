# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from urllib.parse import urlencode
# Custom
from src.custom_waits import css_property_change

class TwitterSearch:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "https://twitter.com/search?"
        self.results = []
        self.wait = WebDriverWait(self.driver, 3)

    # Search methods
    def search(self, query_list, amount):
        results = []

        # Loop through queries
        for query in query_list:
            # Get results page for the query
            self.get_results_page(query)
            tweets = set()

            # Scrape the tweets
            while True:
                # Scrape and add to set
                scraped_tweets = self.scrape_tweets()

                # Add up to amount needed
                for tweet in scraped_tweets:
                    if len(tweets) < amount:
                        tweets.add(tweet)
                    else:
                        break

                # Check if we need to get more
                if len(tweets) < amount:
                    self.load_more_tweets()
                else:
                    break

            # Append to results
            results.append({ 'query': query, 'tweets': tweets })

        # store results dict
        self.results = results

    def get_results_page(self, query):
        # Url encode the query string
        encoded_query = urlencode({'q': query})
        self.driver.get(self.base_url + encoded_query + '&f=live')

        # Wait until results have loaded
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Timeline: Search timeline"]')))    

    def scrape_tweets(self):
        tweets = self.driver.find_elements_by_css_selector('article div[lang]')
        results = []

        # Get all tweets on page
        for tweet in tweets:
            tweet_spans = tweet.find_elements_by_css_selector('span')
            tweet_text = ''

            # loop through spans
            for span in tweet_spans:
                tweet_text = tweet_text + span.text

            # Append to results
            results.append(tweet_text)

        # Return list of results
        return results

    def load_more_tweets(self):
        # Scroll to the btotom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Timeline variables
        timeline_css_selector = 'div[aria-label="Timeline: Search timeline"] > div'
        timeline_css_property = 'min-height'

        # Wait for change in timeline height
        self.wait.until(css_property_change(self.driver, (By.CSS_SELECTOR, timeline_css_selector), timeline_css_property))
        
    
        