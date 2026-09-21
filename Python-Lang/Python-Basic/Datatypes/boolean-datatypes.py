# # question -1
# is_student = True
# has_job = False
# print(is_student, "DataType: ", type(is_student))
# print(has_job, "DataType: ", type(has_job))

# # question -2
# value1 = int(input("Enter 0: "))
# value2 = int(input("Enter 1: "))
# value3 = input("Enter an empty string: ")
# value4 = input("Enter any text: ")

# print(bool(value1))
# print(bool(value2))
# print(bool(value3))
# print(bool(value4))

# # question -3
# a = 25
# b = 40
# print("A is greater than b: ", a > b)
# print("A is less than b: ", a < b)
# print("A is equals to b: ", a == b)

# # question -4
# input_1 = int(input("Enter Number 1: "))
# input_2 = int(input("Enter Number 2: "))
# print("Are they equal: ", input_1 == input_2)
# print("Are they Different: ", input_1 != input_2)

# # question -5
# input_user = int(input("Enter Number: "))
# is_even = input_user % 2 == 0
# print("Is even : ", is_even)

# # queston -6
# input_age = int(input("Enter Your Age: "))
# is_adult = (input_age >= 18)
# print("Is Adult : ", is_adult)

# # question -7
# input_marks = int(input("Enter Your Marks: "))
# is_pass = (input_marks >= 40)
# print("Is Passes : ", is_pass)

# # question - 8
# number_1 = int(input("Enter number: "))
# condition_1 = number_1 >=10
# condition_2 = number_1 <=50
# print("Is between 10 and 50: ", condition_1 and condition_2)

# # question -9
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# print("Is the first number greater? ", a>b)
# print("Is the second number greater? ", a<b)
# print("Are they equal? ", a==b)

# # question -10
# a = int(input("Enter Tempurature: "))
# print("below 10°C ", 10>a )
# print("between 10°C and 30°C ", a >= 10 and a<=30)
# print("Above 30°C ", a<30)

# # question - 11
# age = int(input("Enter the Age: "))
# has_id = input("Enter the status in (yes/no)").lower() == "yes"
# is_eligible = (age >= 18) and has_id
# print("Is eligible:", is_eligible)

# # question -12
# student_id = input("Enter the Student ID: ")
# reg_number = int(input("Enter The register Number: "))
# condition_1 = bool(student_id)
# condition_2 = bool(reg_number)
# print("Eligible Status: ",condition_1 or condition_1)

# # question -13
# is_raining = False
# if not is_raining:
#     print("not raining")

# # question -14
# age = int(input("Enter the age : "))
# has_degree = input("Do you have a degree? (yes/no): ").lower() == "yes"
# has_experience = input("Do you have relevant experience? (yes/no): ").lower() == "yes"
# can_apply = age >= 18 and (has_degree or has_experience)
# print("Elidigible", can_apply)
