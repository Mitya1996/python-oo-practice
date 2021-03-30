"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """"""
    def __init__(self, url):
        """initializes and opens a file"""
        self.url = url
        with open(url) as f:
            self.lines = f.readlines()
        self.words_read = len(self.lines)

    def __repr__(self):
        return f'{self.words_read} words read'

    def random(self):
        """"""
        return choice(self.lines).strip()

    