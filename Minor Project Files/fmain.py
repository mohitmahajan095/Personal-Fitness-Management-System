import customtkinter as ctk
import bmain
import in_profile
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

IMAGE_PATH = os.path.dirname(__file__)

def main_page():
    app = ctk.CTk()
    app.title("Personal Fitness Management System")
    app.geometry("800x500")

    mssql = bmain.SQLManager()

    # Side Image
    picture = ctk.CTkImage(dark_image= Image.open(os.path.join(IMAGE_PATH + "\img\login_picture.png")) , size=(425,500))
    pic_lable = ctk.CTkLabel(app, text="", image=picture)
    pic_lable.place(relx=0, rely= 0)

    # Input page for login
    def login_frame():
        lable_login = ctk.CTkFrame(master=app,height=450, width=376, bg_color="#232832", fg_color="#232832", corner_radius=0)
        lable_login.place(relx=0.532, rely=0.0)

        # Lable
        label_11 = ctk.CTkLabel(lable_login, text="Login Portal", font=("Berlin Sans FB Demi", 30), width=300)
        label_11.place(relx=0.138, rely=0.22)

        # Username & Password
        in_username_entry = ctk.CTkEntry(lable_login, placeholder_text="Enter Username", height=35, width=280)
        in_username_entry.place(relx=0.15, rely=0.34)

        in_password_entry = ctk.CTkEntry(lable_login, placeholder_text="Enter Password", height=35, width=280)
        in_password_entry.place(relx=0.15, rely=0.45)

        # User Type Option
        log_user_option = ["Select user type....", "User", "Admin"]
        user_type_option = ctk.CTkOptionMenu(lable_login, values=log_user_option, width=280 ,button_color="#545454", fg_color="#545454")
        user_type_option.place(relx=0.15, rely=0.56)

        # Login Page Button Actions
        def send_user_login():
            in_username = in_username_entry.get()
            in_password = in_password_entry.get()
            user_type = user_type_option.get()
            print("User Type:", user_type)                            # For Logs
            if "Select user type...." in user_type:
                print("Select your User Type")
            else:                                                     # For Logs
                print(f"Username: {in_username}\nPassword: {in_password}")

            try:
                status_check , user_id = mssql.login_user(in_username, in_password, user_type)
                print("UserID: ", user_id)
                if (status_check) == True:
                    app.destroy()
                    in_profile.successful_login(username=in_username, password=in_password, user_id=user_id)
            except TypeError as e:
                if str(e) == "cannot unpack non-iterable NoneType object":
                    print("Login Failed !\n"+
                          "Please Check Your Username or Password.")
                else:
                    raise
        

        # Login Button
        login_button = ctk.CTkButton(lable_login, text="LOGIN", command=send_user_login)
        login_button.place(relx=0.34, rely=0.67)
    
    login_frame() # Default Page ---> (Login Frame)

    # Input for registration data
    def registration():
        lable_registration = ctk.CTkFrame(master=app,height=450, width=376, bg_color="#232832", fg_color="#232832", corner_radius=0)
        lable_registration.place(relx=0.53, rely=0.0)

        label_21 = ctk.CTkLabel(lable_registration, text="Registration Portal", font=("Berlin Sans FB Demi", 30), width=300)
        label_21.place(relx=0.128, rely=0.03)

        # Username & Password etc. 
        reg_username_entry = ctk.CTkEntry(lable_registration, placeholder_text="Enter Username", height=30, width=280)
        reg_username_entry.place(relx=0.15, rely=0.14)

        reg_password_entry = ctk.CTkEntry(lable_registration, placeholder_text="Enter Password", height=30, width=280)
        reg_password_entry.place(relx=0.15, rely=0.23)

        reg_email_entry = ctk.CTkEntry(lable_registration, placeholder_text="Enter Your Email", height=30, width=280)
        reg_email_entry.place(relx=0.15, rely=0.32)

        reg_dob_entry = ctk.CTkEntry(lable_registration, placeholder_text="Enter DOB (YYYY-MM-DD)", height=30, width=165)
        reg_dob_entry.place(relx=0.15, rely=0.42)

        reg_age_entry = ctk.CTkEntry(lable_registration, placeholder_text="Enter Your Age", height=30, width=110)
        reg_age_entry.place(relx=0.6, rely=0.42)

        reg_gender_option = ["Select user gender....", "Male", "Female"]
        reg_gender_entry = ctk.CTkOptionMenu(lable_registration, values=reg_gender_option, width=280 ,button_color="#545454", fg_color="#545454")
        reg_gender_entry.place(relx=0.15, rely=0.52)

        reg_height_entry = ctk.CTkEntry(lable_registration, placeholder_text="Enter Your Height (cm)", height=30, width=280)
        reg_height_entry.place(relx=0.15, rely=0.62)

        reg_weight_entry = ctk.CTkEntry(lable_registration, placeholder_text="Enter Your Weight (kg)", height=30, width=280)
        reg_weight_entry.place(relx=0.15, rely=0.72)

        reg_user_option = ["Select user type....", "User", "Admin"]
        reg_user_type = ctk.CTkOptionMenu(lable_registration, values=reg_user_option, width=280 ,button_color="#545454", fg_color="#545454")
        reg_user_type.place(relx=0.15, rely=0.82)

        def send_user_reg():
            username = str(reg_username_entry.get())
            password = str(reg_password_entry.get())
            email = str(reg_email_entry.get())
            dob = str(reg_dob_entry.get())
            age = int(reg_age_entry.get())
            gender = str(reg_gender_entry.get())
            height = int(reg_height_entry.get())
            weight = int(reg_weight_entry.get())
            user_type = str(reg_user_type.get())
            
            # For Logs
            print(type(username), type(password), type(email), type(dob), type(age), type(gender), type(height), type(weight), type(user_type))
            
            # Sends data to SQL Server (for user registeration)
            mssql.register_user(username=username,password=password,email=email,dob=dob, age=age,
                             gender=gender,height=height,weight=weight,user_type=user_type)
            lable_registration.destroy()
            login_frame()

        # Registration Button
        reg_button = ctk.CTkButton(lable_registration, text="Create Account", command=send_user_reg)
        reg_button.place(relx=0.34, rely=0.92)

    # Login Page (Frame)
    login_page = ctk.CTkButton(master=app, text_color=("white", "white"), hover_color=("#20242c", "#20242c"),
                                          text="Login",command=login_frame, height=50, width=187.5, bg_color="#0c0e12",
                                          fg_color="transparent", corner_radius=0, font=("Mangal (Headings CS)", 20))
    login_page.place(relx=0.531, rely=0.9)

    # Registration Page (Frame)
    registration_page = ctk.CTkButton(master=app, text_color=("white", "white"), hover_color=("#20242c", "#20242c"),
                                          text="Registration",command=registration, height=50, width=187.5, bg_color="#0c0e12",
                                          fg_color="transparent", corner_radius=0, font=("Mangal (Headings CS)", 20))
    registration_page.place(relx=0.7657, rely=0.9)

    app.mainloop()

main_page()
