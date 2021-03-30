"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """initializes instance"""
        self.start = start
        self.cur_num = start - 1

    def generate(self):
        """generates a new number"""
        self.cur_num += 1
        return self.cur_num

    def reset(self):
        """resets count"""
        self.cur_num = self.start - 1