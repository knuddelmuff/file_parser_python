from menu import Menu
from xlsx_parser import Parser
import datetime

if __name__ == '__main__':
    new_menu = Menu()
    new_menu.general_info()
    new_menu.launch_menu()

    go = True
    while go:
        user_input = input("-> ")

        if user_input == "1":
            file_name = input("Filename (path/to/file.xlsx) -> ")
            sheet_name = input("Sheet in {} -> ".format(file_name))
            try:
                new_parser = Parser()
                new_parser.excel_to_csv(file_name, sheet_name)
            except:
                print("[Error] There is no file called '{}' OR no sheet called '{}'".format(file_name, sheet_name))

        elif user_input == "help":
            new_menu.show_help()

        elif user_input == "3":
            filename = input("Filename (path/to/file.csv) -> ")
            column = input("Column (V0_Date) -> ")
            new_parser = Parser()
            new_parser.check_if_float(filename, column)
            #except:
              #  print("[Error] There is no CSV file named {} or a column named {}".format(file_name, column))

        elif user_input == "":
            new_menu.launch_menu()
        elif user_input == "exit":
            print("[Info] End parser session -- {}".format(datetime.datetime.today()))
            go = False
