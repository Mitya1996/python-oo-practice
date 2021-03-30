"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
    >>> wf = WordFinder('words.txt')
    235886 words read

    >>> wf.url
    'words.txt'

    >>> wf2 = WordFinder('simple.txt')
    3 words read

    >>> wf2.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf2.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf2.random() in ['cat', 'dog', 'porcupine']
    True

    """
    def __init__(self, url):
        """initializes and opens a file"""
        self.url = url
        self.words = self.parse()
        print(f'{len(self.parse())} words read')


    def parse(self):
        with open(self.url) as f:
            lines = f.readlines()
        return lines

    def random(self):
        """"""
        return choice(self.words).strip()

    