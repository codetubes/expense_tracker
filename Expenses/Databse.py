import os
from config import db_name
import sqlite3
class ExpensesModel():
    '''
    This class will handle all database interactions for expenses
    '''


    def __init__(self):
        self.init_db()

    def init_db(self):
        '''
        Create Database Table if doesn't exist
        :return: None
        '''
        db_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..",db_name
        ))
        try:
            self.conn= sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            self.init_table()
        except Exception as e:
            print(e)
            raise Exception(e)

    def init_table(self):
        '''
        Create expenses table in database if doesn't exist
        :return:
        '''
        sql = f'''
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category CHAR(50) NOT NULL,
                date CHAR(50) NOT NULL
            );
        '''
        self.cursor.execute(sql)
        self.conn.commit()

    def update(self, id, description, amount, category, date):
        '''
        Update already existing expense record
        :param id: int - expense id
        :param description: string - new description
        :param amount: float - new amount
        :param category: string - new category
        :param date: string - new date
        :return: None
        '''
        sql = ''' UPDATE expenses
                      SET description = ?,
                          amount = ?,
                          category = ?,
                          date = ?
                      WHERE id = ?'''

        try:
            self.cursor.execute(sql, (description, amount, category, date, id))
            self.conn.commit()
        except Exception as e:
            raise e


    def add(self, description, amount, category, date)->int:
        '''
        Add new expense record to database
        :param description: text
        :param amount: float
        :param category: character
        :param date: character
        :return: None
        '''
        sql = '''
            INSERT INTO expenses(description, amount, category, date)
            VALUES (?,?,?,?)
        '''
        try:
            self.cursor.execute(sql, (description, amount, category, date))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            raise e


    def get_expense(self, id):
        '''
        This function will retrieve single expense
        :param id: Expense unique id
        :return: dict
        '''
        try:
            sql = f'''
                SELECT * FROM expenses WHERE id=?
            '''
            self.cursor.execute(sql, (str(id)))
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            raise Exception(e)

    def delete_expense(self, id):
        '''
        This function will delete expense record in database
        :param id: expense id
        :return: None
        '''
        try:
            sql = f'''
                DELETE FROM expenses WHERE id=?
            '''
            self.cursor.execute(sql, (str(id), ))
            self.conn.commit()
        except Exception as e:
            raise Exception(e)



    def get_expenses(self, category=None)->list:
        '''
        Get all expenses by category
        :param category: string
        :return: list
        '''
        try:

            sql = f'''
                SELECT * FROM expenses ORDER BY id LIMIT 20
            '''
            if category:
                sql += " WHERE category=?"
                self.cursor.execute(sql, (category))
            else:
                self.cursor.execute(sql)

            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            raise Exception(e)

    def get_expense_report(self):
        '''
        Get total expenses by category
        :return:
        '''
        try:

            sql = f'''
                SELECT category, SUM(amount) as total_amount FROM expenses GROUP BY category ORDER BY total_amount DESC
            '''
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            raise Exception(e)


    def __del__(self):
        self.conn.close()






