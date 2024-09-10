import pyodbc

class DatabaseConnection:
    def __init__(self, server, database, username, password, driver='{ODBC Driver 17 for SQL Server}'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=Yes'
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(self.connection_string)
        except pyodbc.Error as ex:
            print(f"An error occurred: {ex.args[1]}")

    def get_connection(self):
        if self.connection is None:
            self.connect()
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Database connection closed.")






