import time
# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By 
from urllib.parse import urlencode

class TwitterSearch:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "https://twitter.com/search?"
        self.results = []

    # Search methods
    def search(self, query_list):
        results = []
        # Loop through queries
        for query in query_list:
            self.get_results_page(query)
            tweets = self.parse_results_page()
            # Append to results
            results.append({ 'query': query, 'tweets': tweets })
        # store results dict
        self.results = results

    def get_results_page(self, query):
        encoded_query = urlencode({'q': query})
        self.driver.get(self.base_url + encoded_query + '&f=live')
        wait = ui.WebDriverWait(self.driver, 3)
        # Wait until results have loaded
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Timeline: Search timeline"]')))

    def parse_results_page(self):
        results = []
        tweets = self.driver.find_elements_by_css_selector('article div[lang]')
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

    def load_more_results(self):
        pass

    
        