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
        self.cur_num = start

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} cur_num={self.cur_num}>"


    def generate(self):
        """generates a new number"""
        self.cur_num += 1
        return self.cur_num - 1

    def reset(self):
        """resets count"""
        self.cur_num = self.start