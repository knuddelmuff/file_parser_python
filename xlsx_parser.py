import datetime
import random
import string

import xlrd
import csv
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
        name = ''.join(random.choices(string.ascii_lowercase, k=5))
        self.csv_file = open('converted_files/{}.csv'.format(name), 'w')
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
        df = pd.read_csv(filename, encoding="iso-8859-1")
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
        df = pd.read_csv(filename, encoding="iso-8859-1")

        print(df)

        # input_file = csv.DictReader(open(filename, "r", encoding="utf-8"))
        # headers = input_file.fieldnames
        # output_file = csv.DictWriter(open(filename, "w"), fieldnames=headers)
        #
        # output_file.writeheader()
        #
        # for row in input_file:
        #     if row[column] == string:
        #         row[column] = number
        #     output_file.writerow(row)
        #
        # print("[Info] Converted {} to {}".format(string, number))

    def get_maxOfColumn(self, filename, column):
        df = pd.read_csv(filename)
        max_row = df.loc[df[column].idxmax()]
        max_value = int(df[column].max())

        print("[Info] Row with maximum value: \n\n", max_row, "\n")
        print("[Info] The max value of {} is {}".format(column, max_value))


    # TODO: Write ages into csv file
    def get_ageOfPerson(self, filename):

        ages = []

        with open(filename, "r", encoding="iso-8859-1") as file:
            content = csv.reader(file, delimiter=";")
            headers = next(content, None)
            #headers.insert(5, "V0_Alter")
            #print(headers)

            today = datetime.datetime.today()
            for row in content :

                if row[0] == "" or row[4] == "":
                    ages.append("01.01.70")
                    row[0] = "01.01.70"
                    row[4] = "01.01.70"


                patDate = datetime.datetime.strptime(row[0], '%d.%m.%y')
                bdate = datetime.datetime.strptime(row[4], '%d.%m.%y')

                if bdate.year > today.year:
                    age = patDate.year - (bdate.year - 100) - ((patDate.month, patDate.day) < (bdate.month, bdate.day))
                else:
                    age = patDate.year - bdate.year - ((patDate.month, patDate.day) < (bdate.month, bdate.day))
                ages.append(age)


                print("Born: {} \t Date: {} \t Age: {}".format(bdate.strftime("%d.%m.%y'"), patDate.strftime("%d.%m.%y'"), age))


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
