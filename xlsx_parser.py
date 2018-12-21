import xlrd
import csv
import datetime
import os
import pandas as pd

class Parser:

    def __init__(self):
        self.csv_file = ""

        if not os.path.exists("converted_files"):
            os.makedirs("converted_files")

    def excel_to_csv(self, file_name, sheet_name):
        wb = xlrd.open_workbook(file_name)
        sh = wb.sheet_by_name(sheet_name)
        self.csv_file = open('converted_files/{}_{}.csv'.format(file_name, datetime.date.today()), 'w')
        wr = csv.writer(self.csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        self.csv_file.close()

        os.system("open converted_files/")

        print("\n")
        print("[Done] {} was successfully converted to CSV".format(file_name))
        print("[Warning] It needs up to 10 seconds until the file is created!")

    def delete_null(self):

        with open(self.csv_file, 'r') as input_file:
            content = csv.reader(input_file)
            print(content)

    def check_if_float(self, filename, column):
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')

            column_content = [row[column] for row in reader]
            print(column_content[:10], "\n")

            for i, e in enumerate(column_content):
                try:
                    float(e)
                except:
                    print("[Warning] Column contains words/strings or empty!")
                    print("Column: {}".format(i))

    def change_string2number(self, filename, column, string, number):
        input_file = csv.DictReader(open(filename, "r", encoding="utf-8"))
        headers = input_file.fieldnames
        output_file = csv.DictWriter(open(filename, "w"), fieldnames=headers)

        output_file.writeheader()

        for row in input_file:
            if row[column] == string:
                row[column] = number
            output_file.writerow(row)

        print("[Info] Converted {} to {}".format(string,number))


    def get_maxOfColumn(self, filename, column):
        df = pd.read_csv(filename)
        max_row = df.loc[df[column].idxmax()]
        max_value = int(df[column].max())

        print("[Info] Row with maximum value: \n\n", max_row, "\n")
        print("[Info] The max value of {} is {}".format(column, max_value))


