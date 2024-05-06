import pyodbc

def connect():
    try:
        connection = pyodbc.connect("DRIVER={SQL Server};"+
                                "Server=Your_Server_Name;"+
                                "Database=YOUR_DATABASE_NAME;"+
                                "Trusted_Connection=True")
        print("Connection Successfully Estiblished to MS-SQL-Server !") 
        return connection
        
    except pyodbc.Error as ex:
        print("\nConnection Failed !\n\n",ex, " \n")
