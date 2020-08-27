#!/Users/giladgrant/Documents/Code/Automation/tweet-finder/bin/python3
from src.twitter_search import TwitterSearch
from src.file_parser import FileParser
from src.exporter import Exporter

def main():
    # Instatiate objects
    twitter = TwitterSearch()
    queries = FileParser("./queries.txt").queries
    exporter = Exporter('results')

    # Search
    twitter.search(queries)
    results = twitter.results

    # Export results
    exporter.export(results)


if __name__ == "__main__":
    main()