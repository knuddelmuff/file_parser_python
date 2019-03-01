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
            file_name = input("filename -> ")
            sheet_name = input("sheet in {} -> ".format(file_name))
            #try:
            new_parser.excel_to_csv(file_name, sheet_name)
            #except:
                #print("[Error] There is no file called '{}' OR no sheet called '{}'".format(file_name, sheet_name))

        elif user_input == "2":
            filename = input("filename -> ")
            column = input("column -> ")
            #try:
            new_parser.delete_null_rows(filename, column)
            #except:
                #print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "3":
            filename = input("filename -> ")
            column = input("column -> ")
            try:
                new_parser.check_if_float(filename, column)
            except:
                print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "4":
            filename = input("filename -> ")
            column = input("column -> ")
            string = input("string -> ")
            number = int(input("number -> "))
            #try:
            new_parser.change_string2number(filename, column, string, number)
            #except:
                #print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "5":
            filename = input("filename -> ")
            column = input("column -> ")
            try:
                new_parser.get_maxOfColumn(filename, column)
            except:
                print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "6":
            filename = input("filename -> ")
            #try:
            new_parser.get_ageOfPerson(filename)
            #except:
                #print("[Error] There is no CSV file named {}, a bday column called {} or a date column named {}".format(filename, column1, column2))

        elif user_input == "7":
            filename = input("filename -> ")
            column = input("column -> ")
            value = input("value -> ")
            #try:
            new_parser.count_value(filename, column, value)
            #except:
                #print("[Error] There is no CSV file named {} or a column named {}".format(filename, column))

        elif user_input == "help":
            new_menu.launch_menu()
            new_menu.show_help()

        elif user_input == "":
            new_menu.launch_menu()

        elif user_input == "exit":
            print("[Info] End parser session -- {}".format(datetime.datetime.today()))
            go = False
