# # question -1
# user_input_1 = int(input("Enter the integer: "))
# if user_input_1 > 0 :
#     print("Number is greater: ")

# # question -2
# user_age = int(input("Enter the Age: "))
# if user_age >= 18 :
#     print("Eligible to vote: ")

# # question -3
# user_input_2 = int(input("Enter the integer: "))
# if user_input_2 % 2 == 0:
#     print("Number is Even: ")
# else:
#     print("Number is Odd: ")

# # question -4
# user_input_3 = int(input("Enter the integer: "))
# if user_input_3 % 5 ==0 :
#     print("Number is divisble by 5: ")
# else:
#     print("Number is not divisble by 5: ")

# # question -5
# user_str = input("Enter the string: ")
# length_str = len(user_str)
# if length_str > 10 :
#     print("Long string")

# # question -6
# number_1 = int(input("Enter the number: "))
# if number_1 >= 0 :
#     print("Positive")
# else:
#     print("Negative")

# # question -7
# user_number = int(input("Enter the number: "))
# if user_number % 2 == 0:
#     print("even")
# else:
#     print("Odd")

# # question -8
# marks = int(input("Enter the number: "))
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")

# # question -9
# correct_username = "admin"
# correct_password = "1234"

# username = input("Enter the username: ")
# password = input("Enter the password: ")

# if username == correct_username and password == correct_password :
#     print("Login successful")
# else:
#     print("Invalid username and password")

# # question -10
# number_a = int(input("Enter the first number: "))
# number_b = int(input("Enter the second number: "))
# if number_a > number_b :
#     print("First number is greater")
# else:
#     print("Second number is greater")

# # question -11
# number_user = int(input("Enter the number: "))
# if number_user > 0 :
#     print("Positive")
# elif number_user < 0 :
#     print("Negative")
# else:
#     print("Zero")

# # question -12
# marks = int(input("Enter the marks: "))
# if marks >= 90 :
#     print("A")
# elif marks >= 80 :
#     print("B")
# elif marks >= 70 :
#     print("C")
# elif marks >= 60 :
#     print("D")
# else:
#     print("F")

# # question -13
# temp = int(input("Enter the temperature: "))
# if temp < 10:
#     print("cold")
# elif temp < 25:
#     print(" Cool")
# elif temp < 35:
#     print("warm")
# else:
#     print("Hot")

# # question -14
# day = int(input("Enter the number btw 1 - 7 :"))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("wednesday")
# elif day == 4:
#     print("thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid Day")

# # question - 15
# num_1 = int(input("Enter the number 1: "))
# num_2 = int(input("Enter the number 2: "))
# operator = input("Enter the Operator: ")

# if operator == "+" :
#     print(num_1 + num_2)
# elif operator == "-" :
#     print(num_1 - num_2)
# elif operator == "*" :
#     print(num_1 * num_2)
# elif operator == "/" :
#     if num_2 == 0:
#         print("Number cannot be zero")
#     else:
#         print(num_1 / num_2)
# else:
#     print("Invalid operator")

# # question -16
# user_age = int(input("Enter Your Age: "))
# if user_age < 5 :
#     print("Price of tickets : Free")
# elif user_age <= 12 :
#     print("Price of tickets : Rs 100")
# elif user_age <= 59 :
#     print("Price of tickets : Rs 200")
# else:
#     print("Price of tickets : Rs 120")

# # question -17
# units = int(input("Enter our Electricity units: "))
# print("Units consumed",units)
# if units <= 100 :
#     print("Total Bills amount is",units * 5)
# elif units <= 200:
#     print("Total Bills amount is",units * 7)
# elif units <= 300:
#     print("Total Bills amount is",units * 10)
# else:
#     print("Total Bills amount is",units * 12)

# # question -18
# python = int(input("Enter the python marks: "))
# sql = int(input("Enter the sql marks: "))
# maths = int(input("Enter the maths marks: "))
# total = python + sql + maths
# print("Total marks: ", total)
# avg_marks = (python + sql + maths)/3
# print("Average marks", avg_marks)
# if avg_marks >= 90:
#     print("A")
# elif avg_marks >= 75:
#     print("B")
# elif avg_marks >= 60:
#     print("C")
# elif avg_marks >= 40:
#     print("D")
# else:
#     print("Fail")

# # question- 19
# acc = int(input("Enter the acc bal :"))
# withdrawal = int(input("Enter the withdrawal amount :"))
# if withdrawal < 0:
#     print("Invalid amount")
# elif withdrawal > acc:
#     print("Insufficient amount")
# else:
#     print("Withdrawal Successful")
#     print("Remaining amount:", acc - withdrawal)


# # question -20
# Age = int(input("Enter the Age: "))
# Percentage = float(input("Enter the Percentage: "))
# Attendance_percentage = int(input("Enter the Attendance_percentage: "))
# Backlog_status = input("Enter the Status in Yes/No: ").lower()
# entrance_exam_status = input("Enter the Entrance Exam Status in Yes/No: ").lower()

# if Age < 17:
#     print("Not eligible: Age requirement not met")
# elif Percentage < 60:
#     print("Not eligible: Percentage requirement not met")
# elif Attendance_percentage < 75:
#     print("Not eligible: Attendance requirement not met")
# elif Backlog_status == "yes" :
#     print("Not eligible: Backlog detected")
# elif entrance_exam_status == "no" :
#     print("Not eligible: Entrance exam not cleared")
# else:
#     print("Congratulations! You are eligible.")
