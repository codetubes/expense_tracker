from .Databse import ExpensesModel
from datetime import datetime

class AddExpense:
    '''
    This class will handle all functionality to add new expenses
    '''
    title = "Add New Expense"

    category_options= (
        "Insurance",
        "Entertainment",
        "Grocery",
        "Mortgage"
    )

    def __init__(self):
        print("============")
        print(self.title)
        print("============")

    def get_description(self):
        '''
        Get expense description from console
        :return: string
        '''
        print("Enter the expense description (i.e. Restaurant payment)")
        description = input()
        description = description.strip()

        if description:
            return description
        else:
            print("This field is required")
            self.get_description()

    def get_amount(self):
        '''
        Get expense amount from the console.
        :return: float
        '''
        print("Enter the expense amount (i.e. 15)")
        amount = input()
        amount = amount.strip()

        if amount:
            try:
                amount = float(amount)
            except Exception as e:
                print("Invalid amount entered")
                print(e)
                return self.get_amount()
            else:
                return amount
        else:
            print("This field is required")
            self.get_description()

    def get_category(self):
        '''
        Get expense category from the console
        :return: int - category id
        '''
        print("Select the expense category (i.e. 1)")
        for index, option in enumerate(self.category_options):
            print(f"{index}. {option}")
        category = input()
        category = category.strip()

        if category:
            try:
                category = int(category)
                try:


                    selectedCategory = self.category_options[category]
                    return selectedCategory
                except Exception as e:
                    print(f"Option {category} doesn't exit in the list ")
                    self.get_category()

            except Exception as e:
                print("Invalid category option selected")
                print(e)
                self.get_category()
        else:
            print("Invalid category option selected")
            self.get_category()


    def get_input(self):
        '''
        Get user input from console and return as dict
        :return: dict - New expense info
        '''
        data = {}

        data["description"] = self.get_description()
        data["amount"] = self.get_amount()
        data["category"] = self.get_category()
        data["date"] = datetime.today().strftime('%Y-%m-%d')

        return data

    def start(self):
        info = self.get_input()
        db = ExpensesModel()
        try:
            db.add(
                description = info["description"],
                amount=info["amount"],
                category=info["category"],
                date = info["date"]
            )
            print("Expense successfully added to database")
        except Exception as e:
            print(e)
            print("Something went wrong. Try again")
            self.start()

