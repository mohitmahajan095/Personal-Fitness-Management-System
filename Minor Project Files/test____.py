# def calculate_bmi(weight, height):
#     return weight / (height ** 2)

# def classify_bmi(bmi):
#     if bmi < 18.5:
#         return "underweight"
#     elif bmi >= 18.5 and bmi < 25:
#         return "Healthy Weight"
#     elif bmi >= 25 and bmi < 30:
#         return "overweight"
#     else:
#         return "obese"

# def calculate_bmr(weight, height, age, gender):
#     if gender == 'male':
#         return 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
#     elif gender == 'female':
#         return 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)

# def calculate_maintenance_calories(bmr, activity_level):
#     activity_multipliers = {
#         "sedentary": 1.2,
#         "lightly active": 1.375,
#         "moderately active": 1.55,
#         "very active": 1.725,
#         "extra active": 1.9,
#     }
#     return bmr * activity_multipliers[activity_level]

# def calculate_body_fat_percentage(weight, height, gender, age):
#     bmi = calculate_bmi(weight, height)
#     print(bmi)
#     if gender == 'male':
#         body_fat_percentage = (1.20 * bmi) + (0.23 * age) - 16.2
#     elif gender == 'female':
#         body_fat_percentage = (1.20 * bmi) + (0.23 * age) - 5.4
#     return body_fat_percentage

# def calculate_muscle_mass(weight, body_fat_percentage):
#     # Assume muscle mass is the difference between total weight and fat mass
#     # Adjust as needed for more accurate estimations
#     fat_mass = weight * (body_fat_percentage / 100)
#     muscle_mass = weight - fat_mass
#     return muscle_mass

# # Prompt the user to enter weight, height, age, and gender
# weight = int(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
# age = int(input("Enter your age: "))
# gender = input("Enter your gender (male/female): ")

# # Calculate BMI
# bmi = calculate_bmi(weight, height)

# # Classify BMI
# classification = classify_bmi(bmi)

# # Calculate BMR
# bmr = calculate_bmr(weight, height, age, gender)

# # Determine activity level based on BMR
# activity_levels = {
#     "sedentary": "Little to no exercise",
#     "lightly active": "Light exercise or sports 1-3 days a week",
#     "moderately active": "Moderate exercise or sports 3-5 days a week",
#     "very active": "Hard exercise or sports 6-7 days a week",
#     "extra active": "Very hard exercise or sports, a physical job, or training twice a day",
# }

# activity_level = None
# if bmr < 1600:
#     activity_level = "sedentary"
# elif bmr >= 1600 and bmr < 2200:
#     activity_level = "lightly active"
# elif bmr >= 2200 and bmr < 2800:
#     activity_level = "moderately active"
# elif bmr >= 2800 and bmr < 3500:
#     activity_level = "very active"
# else:
#     activity_level = "extra active"

# # Calculate maintenance calories
# maintenance_calories = calculate_maintenance_calories(bmr, activity_level)

# # Print BMI, classification, BMR, activity level, and maintenance calories
# print("Your BMI is:", bmi)
# print("You fall within the", classification, "range.")
# print("Your Basal Metabolic Rate (BMR) is:", bmr)
# print("Your activity level is:", activity_levels[activity_level])
# print("Your maintenance calories are:", maintenance_calories)

print(120/60)