import unittest
import sys
from Row import Row
from Reader import SpreadsheetReader

class RowTest(unittest.TestCase):

    def test_case_1(self):
        sys.stdout.flush()
        print("First Test")
        row = Row("5195")
        expected_minimun = 1
        expected_maximun = 9
        expected_checksum = 8
        result = row.getChecksum()
        print("Result: " + str(result))
        self.assertTrue(result==expected_checksum)

    def test_case_2(self):
        sys.stdout.flush()
        print("Second Test")
        row = Row("753")
        expected_minimun = 3
        expected_maximun = 7
        expected_checksum = 4
        result = row.getChecksum()
        print("Result: " + str(result))
        self.assertTrue(result == expected_checksum)

    def test_case_3(self):
        sys.stdout.flush()
        print("Third Test")
        row = Row("2468")
        expected_minimun = 2
        expected_maximun = 8
        expected_checksum = 6
        result = row.getChecksum()
        print("Result: " + str(result))
        self.assertTrue(result == expected_checksum)

    def test_case_4(self):
        sys.stdout.flush()
        print("Fourth Test")
        reader = SpreadsheetReader("spreadsheet.dat")
        expected_checksum = reader.get_checksum()
        print ("Result: " + str(expected_checksum))

if __name__ == '__main__':
    unittest.main()
