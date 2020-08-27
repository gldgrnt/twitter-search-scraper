import os
import sys
from csv import reader

class FileParser:
    def __init__(self, file_path):
        # Load file
        filename, extension = os.path.splitext(file_path)

        # Check for correct file format
        if extension != '.txt':
            print('Invalid file type, must be .txt with one query per line')
            sys.exit()

        # Get queries from file
        self.queries = self.parse_file(file_path)

    def parse_file(self, file_path):
        file = open(file_path, 'r')
        queries = []

        # Read each line of file
        for line in file:
            queries.append(line.replace('\n', ''))
        # Close and return queries
        file.close()
        return queries