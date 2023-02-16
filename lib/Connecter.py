import pyodbc
import os

class connector:
    def __init__(self, dbName):
        self.conn = pyodbc.connect('Driver={SQL Server};Server='+os.getenv('COMPUTERNAME')+';Database='+dbName+';Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
    
    def getConnection(self):
        return self.conn
    
    def getCursor(self):
        return self.cursor
    
    def close(self):
        self.cursor.close()
        self.conn.close()
    