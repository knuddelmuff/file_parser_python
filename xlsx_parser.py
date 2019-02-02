import xlrd
import csv
import datetime
import os
import pandas as pd
from datetime import datetime, date


class Parser:

    def __init__(self):
        self.csv_file = ""

        if not os.path.exists("converted_files"):
            os.makedirs("converted_files")

    def excel_to_csv(self, file_name, sheet_name):
        wb = xlrd.open_workbook(file_name)
        sh = wb.sheet_by_name(sheet_name)
        # TODO: wieder datetime.date.today() einfügen
        self.csv_file = open('converted_files/{}.csv'.format("neuer_file"), 'w')
        wr = csv.writer(self.csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        self.csv_file.close()

        os.system("open converted_files/")

        print("\n")
        print("[Done] {} was successfully converted to CSV".format(file_name))
        print("[Warning] It needs up to 10 seconds until the file is created!")

    def delete_null_rows(self, filename, column):
        # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html
        df = pd.read_csv(filename, error_bad_lines=False, encoding="utf-8")
        df = df.dropna(subset=[column])
        df.to_csv(filename, index=False)
        print("[Info] Deleted null rows from {}".format(column))

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
        input_file = csv.DictReader(open(filename, "r"))
        headers = input_file.fieldnames
        output_file = csv.DictWriter(open(filename, "w"), fieldnames=headers)

        output_file.writeheader()

        for row in input_file:
            if row[column] == string:
                row[column] = number

            output_file.writerow(row)

        print("[Info] Converted {} to {}".format(string, number))


    def delete_firstRow(self, filename):

        df = pd.read_csv(filename, error_bad_lines=False)
        df = df.drop(df.head())
        df.to_csv(filename, index=False)

    def get_maxOfColumn(self, filename, column):
        df = pd.read_csv(filename, encoding="utf-8")
        max_row = df.loc[df[column].idxmax()]
        max_value = int(df[column].max())

        print("[Info] Row with maximum value: \n\n", max_row, "\n")
        print("[Info] The max value of {} is {}".format(column, max_value))

    # TODO: Der Monat wird noch nicht beachtet
    # TODO: Funktioniert nur, wenn die Spalte Floats enthält
    def get_ageOfPerson(self, filename, bdayColumn):

        today = datetime.today()

        df = pd.read_csv(filename, error_bad_lines=False, encoding="utf-8")
        df = df[bdayColumn]
        for i, row in enumerate(df):
            if type(row) == float:
                strDate = str(row)
               # strDate = strDate.replace(".", "")
                strDate = strDate[:-2]

                year = strDate[-4:]
                month = strDate[:-4]

                #convert to generic date string
                if len(month) > 1:
                    date = month + "." + year
                else:
                    date = "0" + month + "." + year

                age = (today.year - int(year))

                print("Index in CSV: {}\n".format(i) +
                     "Born:         {}\n".format(date) +
                     "Age:          {}\n".format(age))
            else:
                print("[Error] This method is only able to handle floats as column values")
                break

    def count_value(self, filename, column, value):
        df = pd.read_csv(filename)
        df = df[column]
        counter = 0
        for v in df:
            if str(v) == value:
                counter += 1

        if counter > 0:
            print("\n[Info] Counted {} in column {}".format(value, column))
            print("Value: ", value)
            print("n:     ", counter)
        else:
            print("\n[Warning] There is no '{}' in {}".format(value, column))
