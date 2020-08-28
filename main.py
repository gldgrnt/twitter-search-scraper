#!/Users/giladgrant/Documents/Code/Automation/tweet-finder/bin/python3
import time
from src.twitter_search import TwitterSearch
from src.file_parser import FileParser
from src.exporter import Exporter

def main():
    # Instatiate objects
    twitter = TwitterSearch()
    queries = FileParser("./queries.txt").queries
    exporter = Exporter('results')
    amount = 250

    # Start time
    tic = time.perf_counter()

    # Search
    twitter.search(queries, amount)
    results = twitter.results

    # End time
    toc = time.perf_counter()
    print(f'Scraped {len(queries) * amount} tweets in: {toc - tic:0.2f} seconds')

    # Export results
    exporter.export(results)

if __name__ == "__main__":
    main()