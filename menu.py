from Expenses.ManageExpenses import Expenses
from Reports.ManageReports import Reports

class MainMenu:
    '''
    This class will handle all Menu related functionality
    '''
    title = "Welcome to Main Menu"

    menu_options = (
        ("Manage Expenses", Expenses),
        ("Reports", Reports),
    )
    def __init__(self):
        print("==============")
        print(self.title)
        print("==============")

    def start(self):
        '''
        Starting point of this section
        :return: None
        '''

        for index, menu in enumerate(self.menu_options):
            print(f"{index}. {menu[0]}")

        print("Pls select menu option from the list (i.e. 1)")
        selectedMenu = input()
        selectedMenu = selectedMenu.strip()
        if selectedMenu:
            try:
                selectedMenu = int(selectedMenu)
                try:
                    selectedMenu = self.menu_options[selectedMenu]
                    selectedMenuClass = selectedMenu[1]
                    obj = selectedMenuClass()
                    obj.start()
                except Exception as e:
                    print(f"Option {selectedMenu} doesn't exit in the list ")
                    self.start()

            except Exception as e:
                print("Invalid Menu option selected")
                print(e)
                self.start()
        else:
            print("Invalid menu option selected")
            self.start()







