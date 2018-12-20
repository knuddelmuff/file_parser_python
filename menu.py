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

        GENERAL INFO:
        You can type in your command using the command line. The numbers in the menu below are used to start a command.

        e.g.:
        -> 1 
        
        --- Just type in an emptry string to take a look at the menu --- 

        """)

    def launch_menu(self):
        print("""
        ### MENU ###
        (1)\t\t convert to CSV & opens directory
        (2)\t\t delete null cells
        (3)\t\t check if column only has numbers
        (help)\tshows help information
        (exit)\twill end the parser 
        """)

    def show_help(self):
        print("""
        file_name:  needs to be a *.xlsx e.g. file.xlsx
        sheet_name: the specific sheet in the excel workbook (the table name)
        """)