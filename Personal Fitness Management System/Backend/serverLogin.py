import pyodbc

def connect():
    try:
        connection = pyodbc.connect("DRIVER={SQL Server};"+
                                "Server=anonymous_\sqlexpress;"+
                                "Database=USER_DATABASE;"+
                                "Trusted_Connection=True")
        print("Connected to SQL Server --> [ anonymous_\sqlexpress ]\n" + "Database : USER_DATABASE ")

    except pyodbc.Error as ex:
        print("\nConnection Failed !\n\n",ex, " \n")
    return connection