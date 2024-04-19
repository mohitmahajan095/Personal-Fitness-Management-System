import serverLogin

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

    def track_fitness_activity(self, user_id, activity_type, duration, calories_burned, date):
        print(user_id, activity_type, duration, calories_burned, date)

    def track_food_intake(self, user_id, food_item, quantity, calories_consumed, date):
        pass


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
        
    def cal_burned_by_cycling(met_level, weight, duration):
        duration_in_hr = duration/60
        met_value = {"Moderate": 8,
                     "Vigorous": 12}
        met = met_value[met_level]
        cal_burned = (met * weight * duration_in_hr)
        return cal_burned

    def Total_Calories_Consumed(Quantity, CaloriesPerServing):
         pass

    def Weight_Loss_Progress(InitialWeight, CurrentWeight):
       pass


####################################################################################################################################################################
# mssql_ = sql()
# mssql_.register_user(username="mohit", password="aws555", email="mohit@email.com", dob="2004-02-09", age=20, gender="Male", weight=57, height=183, user_type="User")
# mssql_.login_user(in_username, in_password)
# ab = sql()
# # a,b,c,d,e,f,g,h,i,j = ab.profile_details("mohitmahajan")
# print(ab.profile_details("mohitmahajan"))
