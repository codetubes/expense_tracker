from .Databse import ExpensesModel
from .Add import AddExpense
from datetime import datetime

class UpdateExpense:
    '''
    This class will handle operation to update expenses
    '''

    title = "Update an expense"

    def __init__(self):
        print("============")
        print(self.title)
        print("============")

    def get_expense_id(self):
        '''
        This function wil get expense id from user input
        :return:
        '''
        print("Enter the expense ID you would like to update")
        expenseId = input()
        expenseId = int(expenseId)
        return expenseId

    def get_expense_to_update(self):
        '''
        This functiol will return the expense we are trying to update
        :return: dict
        '''

        try:
            expenseId = self.get_expense_id()
        except Exception as e:
            print(e)
            self.update_expense()
        else:
            try:
                db = ExpensesModel()
                expense = db.get_expense(id=expenseId)
            except Exception as e:
                print(e)
                self.update_expense()
            else:
                return expense

    def update_expense(self, data):
        '''
        This function will update the expense with new values
        :param data: old values
        :return: None
        '''
        print(data)
        addObj = AddExpense()

        newDesc =addObj.get_description()
        newAmount = addObj.get_amount()
        newCat = addObj.get_category()
        newDate = datetime.today().strftime('%Y-%m-%d')

        db = ExpensesModel()
        db.update(id= data[0], description=newDesc, amount=newAmount, category=newCat, date=newDate)
        print("Data successfully updated")







    def start(self):
        try:
            expense = self.get_expense_to_update()
        except Exception as e:
            print(e)
            self.start()
        else:
            try:
                self.update_expense(expense)
            except Exception as e:
                print(e)
                self.start()