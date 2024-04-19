import pyodbc

def connect():
    try:
        connection = pyodbc.connect("DRIVER={SQL Server};"+
                                "Server=ANONYMOUS_\SQLEXPRESS;"+
                                "Database=USER_DATABASE;"+
                                "Trusted_Connection=True")
        print("Connected to SQL Server --> [ anonymous_\sqlexpress ]\n" + "Database : USER_DATABASE ") 
        return connection
        
    except pyodbc.Error as ex:
        print("\nConnection Failed !\n\n",ex, " \n")