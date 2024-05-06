"""" MIT License

Copyright (c) 2024 Mohit Mahajan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """""

import serverLogin
from datetime import datetime, date

current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]
todays_date = date.today()

sqlserver = serverLogin.connect()
sqlserver.autocommit = True
sqlserver = sqlserver.cursor()

class SQLManager:
    def register_user(self, username:str, password:str, email:str, dob:str, age:int, gender:str, height:int, weight:int, user_type:str):
        bmi = weight / ((height/100) ** 2)
        print(username, password, email, dob, age, gender, height, weight, bmi, user_type)
        print(type(username), type(password), type(email), type(dob), type(age), type(gender), type(height), type(weight), type(bmi), type(user_type))
        sql_query = "INSERT INTO UserProfile (username, password, email, dob, age, gender, height, weight, bmi, user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        sqlserver.execute(sql_query, (username, password, email, dob, age, gender, height, weight, bmi, user_type))
        print("\nQuery Executed !\n", username, password, email, dob, age, gender, height, weight, bmi, user_type)
    
    def login_user(self, username, password, user_type):
        query = "SELECT * FROM UserProfile WHERE username = ? AND password = ? AND user_type = ?;"
        sqlserver.execute(query, (username, password, user_type))
        for row in sqlserver:
            print(row)
            print(row[1], row[2], row[10], username, password, user_type)
            self.user_id = row[0]
            user_id = self.user_id
            if  (row[1] == username and row[2] == password and row[10] == user_type):
                print("Successfully Logged In")
                return True, user_id
            else:
                print("Login Failed !")
                return False, user_id

    def track_fitness_activity(self, UserID, activity, duration, calories_burned, current_weight, previous_weight):
        sql_query = "INSERT INTO fitness_activities (UserID, activity, duration, calories_burned, current_weight, previous_weight, date) VALUES (?, ?, ?, ?, ?, ?, ?)"
        sqlserver.execute(sql_query, (UserID, activity, duration, calories_burned, current_weight, previous_weight, str(todays_date)))
        print("\nQuery Executed !\n",UserID, activity, duration, calories_burned, current_weight, previous_weight, str(todays_date))

    def in_fitness_activity_table(self, user_id):
        rows = sqlserver.execute("SELECT TOP 7 * FROM fitness_activities WHERE UserID = ? ORDER BY activity_id DESC;", (user_id)).fetchall()
        for i in range(0, len(rows)):
            print(rows[i])
            print(f"\nFitness Activity History: {rows}")
            return rows
        
    def track_food_intake(self, UserID, food_name, quantity, CaloriesPerServing , meal_time, date):
        total_cal = CaloriesPerServing * quantity
        sql_query = "INSERT INTO food_intakes (UserID, food_name, quantity, calories_intake, meal_time, date, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)"
        sqlserver.execute(sql_query, (UserID, food_name, quantity, total_cal, meal_time, date, current_time))
        print("\nQuery Executed !\n",UserID, food_name, quantity, total_cal, meal_time, date, current_time)

    def update_weight(self, new_weight, user_id):
        sqlserver.execute("UPDATE UserProfile SET weight = ? WHERE user_id = ?;", (new_weight, user_id))
        print(f"Weight Updated to : {new_weight} kg")

    def in_food_intake_table(self, user_id):
        # rows = sqlserver.execute(f"SELECT * FROM food_intakes WHERE UserID = ? ORDER BY timestamp DESC;", (user_id)).fetchall()
        rows = sqlserver.execute("SELECT TOP 7 * FROM food_intakes WHERE UserID = ? ORDER BY food_id DESC;", (user_id)).fetchall()
        for i in range(0, len(rows)):
            print(rows[i])
            print(f"\nFood-Intake History: {rows}")
            return rows

    def get_profile_details(self, username):
        sqlserver.execute("SELECT * FROM UserProfile WHERE username = ?", (username))
        for row in sqlserver:
            if  (row[1] == username):
                user_id = row[0]
                password = row[2]
                email = row[3]
                dob = row[4]
                age = row[5]
                gender = row[6]
                height = row[7]
                weight = row[8]
                bmi = row[9]
                user_type = row[10]
                return (user_id, username, password, email, dob, age, gender, height, weight, bmi, user_type)
            else:
                print("User dosen't exist")
        
    def delete_user_acc(self, user_id):
        sqlserver.execute("DELETE FROM UserProfile WHERE user_id = ?;", (user_id))
        sqlserver.execute("DELETE FROM fitness_activities WHERE UserID = ?;", (user_id))
        sqlserver.execute("DELETE FROM food_intakes WHERE UserID = ?;", (user_id))
        print("User Account & Data Deleted Successfully !")


class feature:
    def get_w_h_a_g(username):
        sqlserver.execute("SELECT * FROM UserProfile WHERE username = ?", (username))
        for row in sqlserver:
            print(row)
            weight = float(row[8])
            height = float(row[7]/100)
            age = float(row[5])
            gender = row[6]
            return weight, height, age, gender

    def calculate_maintenance_calories(username):
        weight, height , age,  gender = feature.get_w_h_a_g(username=username)
        if gender == 'Male':
            BMR = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
        elif gender == 'Female':
            BMR = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
        BMR = round(BMR)

        activity_levels = {
            "Sedentary": 1.2,
            "Lightly active": 1.375,
            "Moderately active": 1.55,
            "Very active": 1.725,
            "Extra active": 1.9,
        }

        selected_activity = None
        if BMR < 1600:
            selected_activity = "Sedentary"
        elif BMR >= 1600 and BMR < 2200:
            selected_activity = "Lightly active"
        elif BMR >= 2200 and BMR < 2800:
            selected_activity = "Moderately active"
        elif BMR >= 2800 and BMR < 3500:
            selected_activity = "Very active"
        else:
            selected_activity = "Extra active"

        activity_level = activity_levels[selected_activity]

        daily_calories = BMR * activity_level
        print("Your BMR is:", BMR)

        return BMR, round(daily_calories)

    def calculate_body_fat_percentage(weight, height, age, gender):
        bmi = weight / (height ** 2)
        if gender == 'Male':
            return round(((1.20 * bmi) + (0.23 * age) - 16.2), 2)
        elif gender == 'Female':
            return round(((1.20 * bmi) + (0.23 * age) - 5.4), 2)

    def calculate_muscle_mass(weight, body_fat_percentage):
        fat_mass = weight * (body_fat_percentage / 100)
        muscle_mass = weight - fat_mass
        return round(muscle_mass, 2)

    def calculate_bmi(username):
        sqlserver.execute("SELECT * FROM UserProfile WHERE username = ?", (username))
        for row in sqlserver:
            weight = row[8]
            height = row[7]/100
        return weight / (height ** 2)

    def classify_bmi(bmi):
        if bmi < 18.5:
            return "Oops you are Under Weight !"
        elif bmi >= 18.5 and bmi < 25:
            return "Yay ! You have Healthy Weight"
        elif bmi >= 25 and bmi < 30:
            return "Oops you are Overweight"
        else:
            return "Your Weight is Obese"

    def cal_burned_by_cycling(self, met_level, weight, duration):
        duration_in_hr = duration/60
        met_value = {"Moderate": 8,
                     "Vigorous": 12}
        met = met_value[met_level]
        cal_burned = (met * weight * duration_in_hr)
        return cal_burned
    
    def cal_burned_by_running(self, speed_level, weight, duration):
       duration_in_hr = duration/60
       speed_value = {"Moderate": 8.3, "Vigorous": 11.0}
       calories_burned = (speed_value[speed_level] * weight * duration_in_hr)
       return calories_burned

    
    def total_calories_consumed(self, user_id, date):
        query = f"SELECT calories_intake FROM food_intakes WHERE date = '{date}' AND UserID = '{user_id}';"
        rows = sqlserver.execute(query).fetchall()
        ttl_calories_consumed = sum(row[0] for row in rows)
        return ttl_calories_consumed
    
    def total_calories_burned(self,user_id, date):
        query = f"SELECT calories_burned FROM fitness_activities WHERE date = '{date}' AND UserID = '{user_id}';"
        rows = sqlserver.execute(query).fetchall()
        ttl_calories_burned = sum(row[0] for row in rows)
        return ttl_calories_burned
