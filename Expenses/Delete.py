from .Databse import ExpensesModel

class DeleteExpense:
    '''
    This classs will handle all functionality to delete expenses
    '''
    title = "Delete the expense"

    def __init__(self):
        print("============")
        print(self.title)
        print("============")

    def get_expense_id(self)->id:

        expense_id = input("Enter expense id: ")
        if not expense_id:
            print("This field can't be empty")
            return self.get_expense_id()

        try:
            expense_id = int(expense_id)
        except Exception as e:
            print(e)
            return self.get_expense_id()
        else:
            return expense_id

    def delete_expense(self, expense_id):
        try:
            db = ExpensesModel()
            expense = db.get_expense(expense_id)
        except Exception as e:
            raise Exception(e)
        else:
            print("==========")
            print(expense)
            confirm = input("Are you sure you want to delete? (y)")
            print("===========")

            if confirm == "y":
                db.delete_expense(id)
            else:
                return





    def start(self):
        '''
        Starting point of the application
        :return: None
        '''
        expenseId = self.get_expense_id()
        try:
            self.delete_expense(expenseId)
        except Exception as e:
            print(e)
            self.start()