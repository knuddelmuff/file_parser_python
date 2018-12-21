from menu import Menu
from xlsx_parser import Parser
import datetime

if __name__ == '__main__':
    new_menu = Menu()
    new_menu.general_info()
    new_menu.launch_menu()

    new_parser = Parser()

    go = True
    while go:
        user_input = input("-> ")

        if user_input == "1":
            file_name = input("Filename (path/to/file.xlsx) -> ")
            sheet_name = input("Sheet in {} -> ".format(file_name))
            try:
                new_parser.excel_to_csv(file_name, sheet_name)
            except:
                print("[Error] There is no file called '{}' OR no sheet called '{}'".format(file_name, sheet_name))

        elif user_input == "2":
            filename = input("Filename (path/to/file.csv) -> ")
            column = input("Column (V0_Date) -> ")
            #try:
            new_parser.delete_null_rows(filename, column)
            #except:
                #print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "3":
            filename = input("Filename (path/to/file.csv) -> ")
            column = input("Column (V0_Date) -> ")
            try:
                new_parser.check_if_float(filename, column)
            except:
                print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "4":
            filename = input("Filename (path/to/file.csv) -> ")
            column = input("Column (V0_Date) -> ")
            string = input("String to change -> ")
            number = int(input("Number to change string into -> "))
            try:
                new_parser.change_string2number(filename, column, string, number)
            except:
                print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "5":
            filename = input("Filename (path/to/file.csv) -> ")
            column = input("Column (V0_Date) -> ")
            try:
                new_parser.get_maxOfColumn(filename, column)
            except:
                print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "help":
            new_menu.show_help()
        elif user_input == "":
            new_menu.launch_menu()
        elif user_input == "exit":
            print("[Info] End parser session -- {}".format(datetime.datetime.today()))
            go = False
