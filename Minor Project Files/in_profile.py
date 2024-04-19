import customtkinter as ctk
from CTkTable import CTkTable
import bmain
from PIL import Image, ImageTk
import datetime
import os

# Theme 
# c1 = "#181c1c"
# c2 = "#30343c"

# Executes after successful login only !
def successful_login(username, password, user_id):
 
    ms_sql = bmain.SQLManager()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    main_frame = ctk.CTk()
    main_frame.title(f"Home - Welcome back {username} !")
    main_frame.geometry("1000x755")
    button_font_family = "Mangal (Headings CS)"
    
    weight, height, age, gender = bmain.feature.get_w_h_a_g(username=username)    # To get weight, height, age & gender of user from database
    
    IMAGE_PATH = os.path.dirname(__file__)

    # Left Frame (Buttons Frame)
    side_frame = ctk.CTkFrame(master=main_frame,height=1000, width=250, bg_color="#0c0e12", fg_color="#0c0e12", corner_radius=0)
    side_frame.place(relx=0,rely=0)

    app_icon = ctk.CTkImage(dark_image=Image.open(IMAGE_PATH  + "\img\home_3.png"), size=(250,99.5))
    _icon_lable = ctk.CTkLabel(master=side_frame, text="",image=app_icon)
    _icon_lable.place(relx=0, rely=0.0)



    # Home Button Action
    def goto_home():
        home_frame = ctk.CTkFrame(master=main_frame,height=1000, width=790, bg_color="#232832", fg_color="#232832", corner_radius=0)
        home_frame.place(relx=0.25,rely=0)

        # Home Background Frame
        home_label_bg = ctk.CTkFrame(master=home_frame, height=75, width=300, bg_color="transparent", fg_color="#15181e", 
                                        corner_radius=30, border_color="#15181e", border_width=1)
        home_label_bg.place(relx=0.27,rely=0.02)

        label_21 = ctk.CTkLabel(home_label_bg, text=f"Home Page", font=("Berlin Sans FB Demi", 30), width=0, fg_color="transparent", bg_color="transparent")
        label_21.place(relx=0.245, rely=0.09)
        
        # Upper Frame
        home_additional_frame = ctk.CTkFrame(master=home_frame, height=350, width=735, bg_color="transparent", fg_color="#15181e",
                                        corner_radius=30, border_color="#15181e", border_width=1)
        home_additional_frame.place(relx=0.011,rely=0.07)

        user_bmi = bmain.feature.calculate_bmi(username=username)
        weight_status = bmain.feature.classify_bmi(user_bmi)
        label_weight = ctk.CTkLabel(home_additional_frame, text=f"* {weight_status}", font=("Berlin Sans FB", 25), width=0, fg_color="transparent", bg_color="transparent")
        label_weight.place(relx=0.04, rely=0.1)

        bmr, maintenance_cal = bmain.feature.calculate_maintenance_calories(username=username)
        label_bmr_m = ctk.CTkLabel(home_additional_frame, text=f"* Your BMR is {bmr} Calories/day", font=("Berlin Sans FB", 25), width=0, fg_color="transparent", bg_color="transparent")
        label_bmr_m.place(relx=0.04, rely=0.28)

        label_maintenance_cal = ctk.CTkLabel(home_additional_frame, text=f"* Your Maintenance Kcal are {maintenance_cal}/day", font=("Berlin Sans FB", 25), width=0, fg_color="transparent", bg_color="transparent")
        label_maintenance_cal.place(relx=0.04, rely=0.46)

        fat_percentage = bmain.feature.calculate_body_fat_percentage(weight, height, age, gender)
        label_fat_perc = ctk.CTkLabel(home_additional_frame, text=f"* You body has {fat_percentage}% fat", font=("Berlin Sans FB", 25), width=0, fg_color="transparent", bg_color="transparent")
        label_fat_perc.place(relx=0.04, rely=0.64)

        muscle_mass = bmain.feature.calculate_muscle_mass(weight, fat_percentage)
        label_muscle_mass = ctk.CTkLabel(home_additional_frame, text=f"* You have {muscle_mass}% Muscle Mass", font=("Berlin Sans FB", 25), width=0, fg_color="transparent", bg_color="transparent")
        label_muscle_mass.place(relx=0.04, rely=0.82)


        # Second Frame
        home_additional_frame_2 = ctk.CTkFrame(master=home_frame, height=310, width=735, bg_color="transparent", fg_color="#15181e", corner_radius=30, border_color="#15181e", border_width=1)
        home_additional_frame_2.place(relx=0.011,rely=0.432)

        label_22 = ctk.CTkLabel(home_additional_frame_2, text=f"Your Tracking !", font=("Berlin Sans FB Demi", 30), width=0, fg_color="transparent", bg_color="transparent")
        label_22.place(relx=0.362, rely=0.05)

        label_cal_intake = ctk.CTkLabel(home_additional_frame_2, text=f"Calories Intake :", font=("Berlin Sans FB", 22), width=0, fg_color="transparent", bg_color="transparent")
        label_cal_intake.place(relx=0.05, rely=0.25)
        cal_intake_bar = ctk.CTkProgressBar(home_additional_frame_2 ,orientation="horizontal", height=20, width=550, determinate_speed=.05211047)
        cal_intake_bar.place(relx=0.05, rely=0.38)
        
        total_cal_intake = 959                                                 # To Do: Connect to bmain sql track_food_intake() function
        per_percent_cal = round(float(total_cal_intake*(1/maintenance_cal)), 2)
        cal_intake_bar.set(per_percent_cal)

        label_cal_burned = ctk.CTkLabel(home_additional_frame_2, text=f"Calories Burned :", font=("Berlin Sans FB", 22), width=0, fg_color="transparent", bg_color="transparent")
        label_cal_burned.place(relx=0.05, rely=0.58)
        cal_burned_bar = ctk.CTkProgressBar(home_additional_frame_2 ,orientation="horizontal", height=20, width=550, determinate_speed=.05211047)
        cal_burned_bar.place(relx=0.05, rely=0.71)
        cal_burned_bar.set(0)


        total_cal_burned = 959                                                 # To Do: Connect to bmain sql track_fitness_activity() function
        per_percent_burned = round(float(total_cal_burned*(1/2500)), 2)
        print(per_percent_burned)
        cal_burned_bar.set(per_percent_burned)



    # Activity Button Action
    def fitness_activities():
        
        ft_frame = ctk.CTkFrame(master=main_frame, height=1000, width=790, bg_color="#232832", fg_color="#232832", corner_radius=0)
        ft_frame.place(relx=0.25,rely=0)
        
        # Data Entry (Upper Frame)
        ft_additional_frame = ctk.CTkFrame(master=ft_frame, height=470, width=735, bg_color="transparent", fg_color="#15181e", 
                                        corner_radius=30, border_color="#15181e", border_width=1)
        ft_additional_frame.place(relx=0.011,rely=0.01)

        label_22 = ctk.CTkLabel(ft_additional_frame, text=f"Enter your activities !", font=("Berlin Sans FB Demi", 30), width=300,
                                fg_color="transparent", bg_color="transparent")
        label_22.place(relx=0.3, rely=0.1)
        
        ft_option_1 = ["Select a workout....", "Running" ,"Cycling"]
        activity_type = ctk.CTkOptionMenu(ft_additional_frame, values=ft_option_1,  height=35, width=280 , button_color="#0c0e12",
                                          fg_color="#0c0e12", text_color="white", corner_radius=10, dropdown_fg_color="#0c0e12",
                                          dropdown_hover_color="#20242c")
        activity_type.place(relx=0.1, rely=0.35)

        ft_option_2 = ["Select MET Level....", "Moderate" ,"Vigorous"]
        MET_level = ctk.CTkOptionMenu(ft_additional_frame, values=ft_option_2,  height=35, width=280 , button_color="#0c0e12",
                                          fg_color="#0c0e12", text_color="white", corner_radius=10, dropdown_fg_color="#0c0e12",
                                          dropdown_hover_color="#20242c")
        MET_level.place(relx=0.52, rely=0.35)
        
        ft_duration = ctk.CTkEntry(ft_additional_frame, placeholder_text="Enter Duration (in min)", height=35, width=280,
                                   border_width=1.5, bg_color="transparent", fg_color="#0c0e12",
                                   text_color="white", border_color="#0c0e12", corner_radius=10)
        ft_duration.place(relx=0.1, rely=0.55)

        current_weight = ctk.CTkEntry(ft_additional_frame, placeholder_text="Enter current weight", height=35, width=280,
                                   border_width=1.5, bg_color="transparent", fg_color="#0c0e12",
                                   text_color="white", border_color="#0c0e12", corner_radius=10)
        current_weight.place(relx=0.52, rely=0.55)


        def ft_send_data():
            ms_sql.track_fitness_activity(activity_type=activity_type.get(), duration=ft_duration.get(), user_id=user_id, date=current_weight.get(), calories_burned=206)
            met_level = str(MET_level.get())
            weight = int(current_weight.get())
            duration = int(ft_duration.get())
            
            if  activity_type.get() == "Cycling":
                kcalburned = bmain.feature.cal_burned_by_cycling(met_level=met_level, weight=weight, duration=duration)
            elif activity_type.get() == "Running":
                print("Helloooo you just came form running !")

            ft_table.insert(row=1, column=0, value=user_id)
            ft_table.insert(row=1, column=1, value=activity_type.get())
            ft_table.insert(row=1, column=2, value=ft_duration.get())
            ft_table.insert(row=1, column=3, value=round(kcalburned))
            ft_table.insert(row=1, column=4, value=current_weight.get())
            ft_table.insert(row=1, column=5, value=datetime.date.today())

        ft_submit_button = ctk.CTkButton(ft_additional_frame, text="Submit", height=35, width=180,corner_radius=10, command=ft_send_data)
        ft_submit_button.place(relx=0.37, rely=0.8)
        
        # Table Frame (Down Frame)
        ft_additional_frame_2 = ctk.CTkFrame(master=ft_frame, height=256.5, width=735, bg_color="transparent", fg_color="#15181e", corner_radius=30, border_color="#15181e", border_width=1)
        ft_additional_frame_2.place(relx=0.011,rely=0.49)

        ft_table = CTkTable(master=ft_additional_frame_2, row=6, column=6, justify="center", width=114, font=("Berlin Sans FB", 15), colors=("#2f3333", "#464949"))
        ft_table.pack(expand=True, fill="both", padx=20, pady=20)
        ft_table.add_row(index=0,values=("UserID", "Activity Type","Duration (mins)","Kcal Burned","Today's Weight","Date"))



    # Food Intake Button Action
    def food_intake():
        fi_frame = ctk.CTkFrame(master=main_frame, height=1000, width=790, bg_color="#232832", fg_color="#232832", corner_radius=0)
        fi_frame.place(relx=0.25,rely=0)

        fi_additional_frame = ctk.CTkFrame(master=fi_frame, height=470, width=735, bg_color="transparent", fg_color="#15181e", 
                                        corner_radius=30, border_color="#15181e", border_width=1)
        fi_additional_frame.place(relx=0.011,rely=0.01)

        label_31 = ctk.CTkLabel(fi_additional_frame, text=f"Enter your food intakes !", font=("Berlin Sans FB Demi", 30), width=300,
                                fg_color="transparent", bg_color="transparent")
        label_31.place(relx=0.27, rely=0.1)

        food_name = ctk.CTkEntry(fi_additional_frame, placeholder_text="Enter Food Name", height=35, width=280,
                                   border_width=1.5, bg_color="transparent", fg_color="#0c0e12",
                                   text_color="white", border_color="#0c0e12", corner_radius=10)
        food_name.place(relx=0.1, rely=0.35)

        fi_option_2 = ["Select meal time....", "Lunch" ,"Snacks","Dinner"]
        fi_meal_time = ctk.CTkOptionMenu(fi_additional_frame, values=fi_option_2,  height=35, width=280 , button_color="#0c0e12",
                                          fg_color="#0c0e12", text_color="white", corner_radius=10, dropdown_fg_color="#0c0e12",
                                          dropdown_hover_color="#20242c")
        fi_meal_time.place(relx=0.52, rely=0.35)

        food_quantity = ctk.CTkEntry(fi_additional_frame, placeholder_text="Enter Food Quantity", height=35, width=280,
                                   border_width=1.5, bg_color="transparent", fg_color="#0c0e12",
                                   text_color="white", border_color="#0c0e12", corner_radius=10)
        food_quantity.place(relx=0.1, rely=0.55)

        calories_per_qty = ctk.CTkEntry(fi_additional_frame, placeholder_text="Enter per plate calories", height=35, width=280,
                                   border_width=1.5, bg_color="transparent", fg_color="#0c0e12",
                                   text_color="white", border_color="#0c0e12", corner_radius=10)
        calories_per_qty.place(relx=0.52, rely=0.55)

        def fi_send_data():

            fi_table.insert(row=1, column=0, value=user_id)
            fi_table.insert(row=1, column=1, value=food_name.get())
            fi_table.insert(row=1, column=2, value=food_quantity.get())
            fi_table.insert(row=1, column=3, value=calories_per_qty.get())
            fi_table.insert(row=1, column=4, value=fi_meal_time.get())
            fi_table.insert(row=1, column=5, value=datetime.date.today())


        fi_submit_button = ctk.CTkButton(fi_additional_frame, text="Submit", height=35, width=180,corner_radius=10, command=fi_send_data)
        fi_submit_button.place(relx=0.37, rely=0.8)

        # Table Frame (Down Frame)
        fi_additional_frame_2 = ctk.CTkFrame(master=fi_frame, height=256.5, width=735, bg_color="transparent", fg_color="#15181e", corner_radius=30, border_color="#15181e", border_width=1)
        fi_additional_frame_2.place(relx=0.011,rely=0.49)

        fi_table = CTkTable(master=fi_additional_frame_2, row=6, column=6, justify="center", width=114, font=("Berlin Sans FB", 15), colors=("#2f3333", "#464949"))
        fi_table.pack(expand=True, fill="both", padx=20, pady=20)
        fi_table.add_row(index=0,values=("UserID", "Food","Quantity","Calories Intake", "Meal Time", "Date"))



    def push_get_profile():
        get_profile(username)

    def get_profile(username):
        try:
            user_info = ms_sql.get_profile_details(username=username)
        except Exception as e:
            print(f"Error fetching profile for {username}: {e}")

        print(user_info)  # For Logs
        u_bmi = round(bmain.feature.calculate_bmi(username=username))
        gp_frame = ctk.CTkFrame(master=main_frame,height=1000, width=790, bg_color="#232832", fg_color="#232832", corner_radius=0)
        gp_frame.place(relx=0.25,rely=0)

        # Data Entry (Upper Frame)
        gp_additional_frame = ctk.CTkFrame(master=gp_frame, height=735, width=735, bg_color="transparent", fg_color="#15181e", 
                                        corner_radius=30, border_color="#15181e", border_width=1)
        gp_additional_frame.place(relx=0.011,rely=0.01)
        
        c = user_info[1]
        char = c[0]
        get_char = char.upper()
        profile_pic = ctk.CTkImage(dark_image=Image.open(IMAGE_PATH + "\img\profile_pic.png"), size=(207,211))
        profile_icon = ctk.CTkLabel(master=gp_additional_frame, text=f"{get_char}", font=("Berlin Sans FB Demi", 110),image=profile_pic)
        profile_icon.place(relx=0.66, rely=0.13)

        label_41 = ctk.CTkLabel(gp_additional_frame, text=f"This is your profile !", font=("Berlin Sans FB Demi", 30, ), width=300, fg_color="transparent", bg_color="transparent")
        label_41.place(relx=0.3, rely=0.04)

        label_UID = ctk.CTkLabel(gp_additional_frame, text=f"User ID:-            {user_info[0]}", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_UID.place(relx=0.05, rely=0.14)

        label_username = ctk.CTkLabel(gp_additional_frame, text=f"Username:-         {user_info[1]}", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_username.place(relx=0.05, rely=0.21)

        label_password = ctk.CTkLabel(gp_additional_frame, text=f"Password:-         {user_info[2]} ", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_password.place(relx=0.05, rely=0.28)

        label_email = ctk.CTkLabel(gp_additional_frame, text=f"Email:-                {user_info[3]}", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_email.place(relx=0.05, rely=0.35)

        label_dob = ctk.CTkLabel(gp_additional_frame, text=f"Date Of Birth:-     {user_info[4] } (YYYY-MM-DD)", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_dob.place(relx=0.05, rely=0.42)

        label_age = ctk.CTkLabel(gp_additional_frame, text=f"Age:-                   {user_info[5]}", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_age.place(relx=0.05, rely=0.49)

        label_gender = ctk.CTkLabel(gp_additional_frame, text=f"Gender:-              {user_info[6]}", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_gender.place(relx=0.05, rely=0.56)

        label_height = ctk.CTkLabel(gp_additional_frame, text=f"Height:-               {user_info[7]} cm", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_height.place(relx=0.05, rely=0.63)

        label_weight = ctk.CTkLabel(gp_additional_frame, text=f"Weight:-               {user_info[8]} Kg", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_weight.place(relx=0.05, rely=0.70)

        label_bmi = ctk.CTkLabel(gp_additional_frame, text=f"BMI:-                   {u_bmi}", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_bmi.place(relx=0.05, rely=0.77)

        label_usertype = ctk.CTkLabel(gp_additional_frame, text=f"User Type:-          {user_info[10]}", font=("Mangal (Headings CS)", 20), width=0, fg_color="transparent", bg_color="transparent")
        label_usertype.place(relx=0.05, rely=0.84)

    # Settings Button Action
    def settings():
        settings_frame = ctk.CTkFrame(master=main_frame, height=1000, width=790, bg_color="#232832", fg_color="#232832", corner_radius=0)
        settings_frame.place(relx=0.25,rely=0)

        label_51 = ctk.CTkLabel(settings_frame, text=f"Settings !", font=("Berlin Sans FB Demi", 40, ), width=0, fg_color="transparent", bg_color="transparent")
        label_51.place(relx=0.36, rely=0.03)

        settings_additional_frame = ctk.CTkFrame(master=settings_frame, height=83, width=735, bg_color="transparent", fg_color="#15181e",
                                                 corner_radius=30, border_color="#15181e", border_width=1)
        settings_additional_frame.place(relx=0.011,rely=0.1)

        delete_acc_label = ctk.CTkLabel(settings_additional_frame, text=f"Delete your account : ", font=("Berlin Sans FB", 25), width=0, fg_color="transparent", bg_color="transparent")
        delete_acc_label.place(relx=0.045, rely=0.3)

        def delete_acc():
            pass
        delete_acc_button = ctk.CTkButton(settings_additional_frame, text="Delete Account", height=35, width=180, corner_radius=30, command=delete_acc, fg_color="#F45850", hover_color="#C34640")
        delete_acc_button.place(relx=0.70, rely=0.27)

    # Logout Button Action
    def logout():
            main_frame.destroy()
            print("Logged Out !")
 
    # Buttons Structure (Arranged)
    home_button = ctk.CTkButton(master=side_frame, text_color=("white", "white"), hover_color=("#20242c", "#20242c",),
                                          text="Home",command=goto_home, height=50, width=245, bg_color="#0c0e12",
                                          fg_color="transparent", corner_radius=10, font=(button_font_family, 20))
    home_button.place(relx=0.012, rely=0.105)

    your_activities_button = ctk.CTkButton(master=side_frame, text_color=("white", "white"), hover_color=("#20242c", "#20242c"),
                                          text="Your Activities",command=fitness_activities, height=50, width=245, bg_color="#0c0e12",
                                          fg_color="transparent", corner_radius=10, font=(button_font_family, 20))
    your_activities_button.place(relx=0.012, rely=0.155)

    food_intake_button = ctk.CTkButton(master=side_frame, text_color=("white", "white"), hover_color=("#20242c", "#20242c"),
                                          text=" Food Intake",command=food_intake, height=50, width=245, bg_color="#0c0e12",
                                          fg_color="transparent", corner_radius=10, font=(button_font_family, 20))
    food_intake_button.place(relx=0.012, rely=0.205)

    profile_button = ctk.CTkButton(master=side_frame, text_color=("white", "white"), hover_color=("#20242c", "#20242c"),
                                          text="Profile",command=push_get_profile, height=50, width=245, bg_color="#0c0e12",
                                          fg_color="transparent", corner_radius=10, font=(button_font_family, 20))
    profile_button.place(relx=0.012, rely=0.6)

    setting_button = ctk.CTkButton(master=side_frame, text_color=("white", "white"), hover_color=("#20242c", "#20242c"),
                                          text="Settings",command=settings, height=50, width=245, bg_color="#0c0e12",
                                          fg_color="transparent", corner_radius=10, font=(button_font_family, 20))
    setting_button.place(relx=0.012, rely=0.65)

    logout_button = ctk.CTkButton(master=side_frame, text_color=("white", "white"), hover_color=("#20242c", "#20242c"),
                                          text="Logout",command=logout, height=50, width=245, bg_color="#0c0e12",
                                          fg_color="transparent", corner_radius=10, font=(button_font_family, 20))
    logout_button.place(relx=0.012, rely=0.7)
    
    # Default Page (--->> Home Page)
    goto_home()
    
    main_frame.mainloop()

# successful_login("arjun", "123456", 34)
