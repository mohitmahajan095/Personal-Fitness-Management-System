import pyodbc

server = "ENETR YOUR SERVER NAME"
database = "ENTER YOUR DATABASE NAME"

def connect():
    try:
        connection = pyodbc.connect("DRIVER={SQL Server};"+
                                f"Server={server};"+
                                f"Database={database};"+
                                "Trusted_Connection=True")
        print(f"Connected to SQL Server --> [ {server} ]\n" + f"Database : {database} ") 
        return connection
        
    except pyodbc.Error as ex:
        print("\nConnection Failed !\n\n",ex, " \n")
