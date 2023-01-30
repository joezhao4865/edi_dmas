import pyodbc
class connector:
    def __init__(self, dbName):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-IC51KS2G;'
                      'Database='+dbName+';'
                      'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
    
    def getConnection(self):
        return self.conn
    
    def getCursor(self):
        return self.cursor
    
    def close(self):
        self.cursor.close()
        self.conn.close()
    