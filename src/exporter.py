class Exporter:
    def __init__(self, path):
        self.path = path

    def export(self, results):
        count = 1
        # Loop through and save
        for result in results:
            file = open(f'{self.path}/result_{count}.txt', 'w+')
            # Give text file a title
            file.write(f'Query: {result["query"]}\n')
            # Write results
            tweet_count = 1
            for tweet in result['tweets']:
                file.write(f'Tweet {tweet_count}: {tweet}\n')
                tweet_count+=1
            # Save file
            file.close()

            count+=1