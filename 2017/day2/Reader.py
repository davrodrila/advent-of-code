from Row import Row

class SpreadsheetReader():
    def __init__(self, file_name):
        self.row_list = []
        self.file_name = file_name
        self.read_file()

    def read_file(self):
        file = open(self.file_name, "r")
        spreadsheet_data = file.read()
        spreadsheet_data = spreadsheet_data.replace('\t'," ")

        for row_data in spreadsheet_data.split(" "):
            self.row_list.append(Row(row_data))
        file.close()

    def get_checksum(self):
        checksum = 0
        for row in self.row_list:
            result = row.getChecksum()
            if result < 0:
                print(row.data)
            checksum = checksum + result
        return checksum

    # Remove all the spaces so every row is separated by exactly one
    def clean_file(self):
        spreadsheet_data = open(self.file_name, "r+")
        spreadsheet = spreadsheet_data.read()
        spreadsheet_fixed = ' '.join(spreadsheet.split())
        print(spreadsheet_fixed)
        spreadsheet_data.truncate()
        spreadsheet_data.write(spreadsheet_fixed)
        spreadsheet_data.close()

