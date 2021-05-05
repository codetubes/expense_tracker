from menu import MainMenu
from config import db_name

def init_database():
    '''
    Create database if doesn't exist
    :return: None
    '''
    pass

def main():
    '''
    Starting Point of the application
    :return: None
    '''
    print("Welcome Expense Tracker")
    init_database()


    mainMenu = MainMenu()
    mainMenu.start()


main()
