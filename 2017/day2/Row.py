import sys


class Row():
    def __init__(self, data):
        self.data = data

    def getChecksum(self):
        return self.getMaximun() - self.getMinimun()

    def getMinimun(self):
        minimun = sys.maxsize
        for digit in self.data:
            if int(digit) < int(minimun):
                minimun = digit
        return int(minimun)

    def getMaximun(self):
        maximun = 0
        for digit in self.data:
                if int(digit) > int(maximun):
                    maximun = digit
        return int(maximun)
