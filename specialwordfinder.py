from wordfinder import WordFinder
from random import choice

class SpecialWordFinder(WordFinder):
    """
    >>> swf = SpecialWordFinder('complex.txt')
    3 words read

    >>> swf.random() in ['pear', 'carrot', 'kale']
    True

    >>> swf.random() in ['pear', 'carrot', 'kale']
    True

    >>> swf.random() in ['pear', 'carrot', 'kale']
    True
    """
    def __init__(self, url):
        super().__init__(url)

    def parse(self):
        with open(self.url) as f:
            lines = [line for line in f if line.strip() and not line.startswith('#')]
        return lines
