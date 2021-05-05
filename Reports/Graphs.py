from Expenses.Databse import ExpensesModel
import matplotlib.pyplot as plt

class ReportGraph:
    '''
    This class will display reports in graphical user interface
    '''
    title = "Report Graphs"


    def __init__(self):
        print("==============")
        print(self.title)
        print("===============")

    def display_pie(self, reports: list)->None:
        '''
        This function will display pie graph
        :param reports:list- data need to be reported
        :return: None
        '''
        labels = [report[0] for report in reports]
        amounts = [report[1] for report in reports]
        print(labels)
        print(amounts)

        fig1, ax1 = plt.subplots()
        ax1.pie(amounts,  labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)

        #ax1.axis('equal')
        plt.show()


    def start(self):
        obj = ExpensesModel()
        try:
            categoryReports = obj.get_expense_report()
            print("==== Report grouped by Category ====")
            for categoryReport in categoryReports:
                print(categoryReport)

            self.display_pie(categoryReports)



        except Exception as e:
            print(e)
            raise Exception(e)

