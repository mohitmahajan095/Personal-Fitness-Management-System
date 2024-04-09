import pyodbc
import customtkinter
import tkinter
import serverLogin


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("Personal Fitness Management System")
app.geometry("900x500")


page_1 = "Log-In"
lable_1 = customtkinter.CTkLabel(app, text="Login Portal", font=("Arial", 24), width=300)
lable_1.place(relx=0.345, rely=0.37)
in_username = customtkinter.CTkEntry(app, placeholder_text="Enter Username")
in_username.place(relx=0.44,rely=0.45)

in_password = customtkinter.CTkEntry(app, placeholder_text="Enter Password")
in_password.place(relx=0.44, rely=0.52)

server = serverLogin.connect()
def login():
    username = in_username.get()
    password = in_password.get()
    if " " in username:
        print("Space Detected")
    print(f"Username = {username}\nPassword = {password}\n")
    server.execute('')
        
login_button = customtkinter.CTkButton(app, text="LOGIN", command=login)
login_button.place(relx=0.44, rely=0.60)


app.mainloop()