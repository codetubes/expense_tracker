from .ExpenseHistory import ExpenseHistory
from .Graphs import ReportGraph
class Reports:
    '''
    This class will handle all functionality to manage reports
    (i.e. View Expense history, view report grouped by category and etc.)
    '''
    title = "Manage Reports"

    menu_options= (
        ("Expense History", ExpenseHistory),
        ("Report Graph", ReportGraph),
        ("Back to Main Menu", None),

    )

    def __init__(self):
        print("==============")
        print(self.title)
        print("==============")

    def select_option(self):
        for index, menu in enumerate(self.menu_options):
            print(f"{index}. {menu[0]}")

        print("Pls select menu option from the list (i.e. 1)")
        selectedMenu = input()
        selectedMenu = selectedMenu.strip()
        if selectedMenu:
            try:
                selectedMenu = int(selectedMenu)
                try:

                    if selectedMenu == len(self.menu_options) - 1:
                        from menu import MainMenu
                        return MainMenu()
                    selectedMenu = self.menu_options[selectedMenu]
                    selectedMenuClass = selectedMenu[1]

                    return selectedMenuClass
                except Exception as e:
                    print(f"Option {selectedMenu} doesn't exit in the list ")
                    self.select_option()

            except Exception as e:
                print("Invalid menu option selected")
                print(e)
                self.select_option()
        else:
            print("Invalid menu option selected")
            self.start()

    def start(self):
        selectedMenuClass = self.select_option()
        obj = selectedMenuClass()
        obj.start()

        self.start()