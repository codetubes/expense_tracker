from .Add import AddExpense
from .Update import UpdateExpense
from .Delete import DeleteExpense

class Expenses:
    '''
    This class will handle all functionality to manage expenses
    (i.e. add, update, delete expenses and etc.)
    '''

    title = "Manage Expenses"
    menu_options = (
        ("Add Expense", AddExpense),
        ("Update Expense", UpdateExpense),
        ("Delete Expense", DeleteExpense),
        ("Search Expense", None),
        ("Back to Main Menu", None),
    )

    def __init__(self):
        print("==================")
        print(self.title)
        print("==================")



    def start(self):
        for index, menu in enumerate(self.menu_options):
            print(f"{index}. {menu[0]}")

        print("Pls select menu option from the list (i.e. 1)")
        selectedMenu = input()
        selectedMenu = selectedMenu.strip()
        if selectedMenu:
            try:
                selectedMenu = int(selectedMenu)
                try:

                    if selectedMenu == len(self.menu_options)-1:
                        from menu import MainMenu
                        obj = MainMenu()
                        return obj.start()
                    selectedMenu = self.menu_options[selectedMenu]
                    selectedMenuClass = selectedMenu[1]
                    obj = selectedMenuClass()
                    obj.start()
                    return self.start()
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
