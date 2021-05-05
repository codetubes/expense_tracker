from Expenses.Databse import ExpensesModel


class ExpenseHistory():
    '''
    This class will show all expense history submitted by user
    '''
    title = "Show Expense History"

    def __init__(self):
        print("=================")
        print(self.title)
        print("=================")

    def start(self):
        obj = ExpensesModel()
        try:
            expenses = obj.get_expenses()
            categoryReports = obj.get_expense_report()
            print("==== Report grouped by Category ====")
            for categoryReport in categoryReports:
                print(categoryReport)

            print("==== Expense History ====")
            for expense in expenses:
                print(expense)

        except Exception as e:
            print(e)
            raise Exception(e)




