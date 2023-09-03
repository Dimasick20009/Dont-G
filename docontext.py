import sqlite3 as sql
#from sqlite3 import Connection
class DBContext:
    def __init__(self, database = "", timeout = 5.0):
        self.DataBase = database
        self.TimeOut = timeout
    def CreateTable(self, query = ""):
        try:
            connection = sql.connect(self.DataBase, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(query)#"CREATE TABLE S2019 (id INT PRIMARY KEY, weather VARCHAR(20))"
        except Exception as ex:
            print(ex)
        finally:
            connection.close()


