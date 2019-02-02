class Menu:

    def general_info(self):
        print("""

 #     # #       ######  #     #    ######                                     
  #   #  #       #     #  #   #     #     #   ##   #####   ####  ###### #####  
   # #   #       #         # #      #     #  #  #  #    # #      #      #    # 
    #    #        #####     #       ######  #    # #    #  ####  #####  #    # 
   # #   #             #   # #      #       ###### #####       # #      #####  
  #   #  #       #     #  #   #     #       #    # #   #  #    # #      #   #  
 #     # #######  #####  #     #    #       #    # #    #  ####  ###### #    # 

 by Alexander Teusz and Ellen Oldenburg
        """)

    def launch_menu(self):
        print("""
        ---------- MENU ----------
        
        (1)\t\t convert to CSV & opens directory
        (2)\t\t delete rows with null in a specific cell
        (3)\t\t check if column only has numbers
        (4)\t\t change string in column with number ('Hi' -> 1)
        (5)\t\t get the max value of a specific column
        (6)\t\t get the ages of all persons
        (7)\t\t count a value in a column
        
        (help)\tshows help information
        
        (exit)\twill end the parser 
        """)

    def show_help(self):
        print("""
        Usage: python app.py 

            Simple program to analyze and manipulate Excel and CSV files.

        Options:

            (1)
                [filename]  the Excel file
                [sheet]     the specific sheet in your Excel file

            (2)
                [filename]  the CSV file
                [column]    the column needed to delete rows with null cells in this column

            (3)
                [filename]  the CSV file
                [column]    the column that got checked for numbers

            (4)
                [filename]  the CSV file
                [column]    the column in which the string will change
                [string]    the string which will change into a number
                [number]    the number the string will got changed into

            (5)
                [filename]  the CSV file
                [column]    column with the max value

            (6)
                [filename]  the CSV file

            (7)
                [filename]  the CSV file
                [column]    column with the value to count
                [value]     value to count
        """)