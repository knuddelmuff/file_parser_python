import xlrd
import csv
import datetime
import os


class Parser:

    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.csv_file = ""

        


    def excel_to_csv(self):
        wb = xlrd.open_workbook(self.file_name)
        sh = wb.sheet_by_name(self.sheet_name)
        self.csv_file = open('converted_files/{}_{}.csv'.format(self.file_name, datetime.date.today()), 'w')
        wr = csv.writer(self.csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        self.csv_file.close()

        os.system("open converted_files/")

        print("\n")
        print("[Done] {} was successfully converted to CSV".format(self.file_name))
        print("[Warning] It needs up to 10 seconds until the file is created!")

    def delete_null(self):

        with open(self.csv_file, 'r') as input_file:
            content = csv.reader(input_file)
            print(content)
