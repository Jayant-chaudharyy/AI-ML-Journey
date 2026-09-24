# # question -1
# student_details = {"name": "jayant", "age": 23,
#                    "course": "MCA", "university": "Bennett", "city": "ghaziabad"}
# print(student_details)
# print(student_details.get("name"))
# print(student_details.get("course"))
# print("Datatype: ",type(student_details))

# # question -2
# info = {
#    "Name": input("Enter the name: "),
#     "Age": int(input("Enter the Age: ")),
#     "Email": input("Enter your Email: "),
#     "Course": input("Enter your Course: ")
# }
# print(info, type(info))

# # question -3
# student = {
#     "name": "Jayant",
#     "age": 23,
#     "course": "MCA",
#     "university": "Bennett University"
# }
# print("Name:", student.get("name"))
# print("Age:",student.get("age"))
# print("Course:", student.get("course"))
# print("University:", student.get("university"))

# # question -4
# student = {
#     "name": "Jayant",
#     "age": 23,
#     "course": "MCA"
# }
# student.update({"university":"Bennett university","city":"Ghaziabad"})
# print(student)

# # question -5
# student = {
#     "name": "Jayant",
#     "age": 23,
#     "course": "MCA",
#     "city": "Delhi"
# }
# student["age"] = 24
# student["course"] = "MCA AI/ML"
# student["city"] = "Ghaziabad"
# print(student)

# # question -6
# student = {
#     "name": "Jayant",
#     "age": 23,
#     "course": "MCA",
#     "city": "Ghaziabad"
# }
# print(student.keys())
# print(student.values())
# print(student.items())

# # question -7
# student = {
#     "name": "Jayant",
#     "age": 23,
#     "course": "MCA"
# }
# user_key = input("Enter the key: ")
# print(user_key in student)
# print(user_key not in student)

# # question -8
# student = {
#     "name": "Jayant",
#     "age": 23,
#     "course": "MCA"
# }
# user_key = input("Enter the key: ")
# print(student.get(user_key))

# # question -9
# student = {
#     "name": "Jayant",
#     "age": 23,
#     "course": "MCA",
#     "city": "Ghaziabad"
# }
# city = student.pop("city")
# student["email"] = "fghjk@gmail.com"
# print(student)
# student.popitem()
# print(student)

# # question -10
# marks = {
#     "Python": 85,
#     "SQL": 78,
#     "Math": 72,
#     "AI": 88,
#     "ML": 81
# }
# print(len(marks))
# print(marks)
# marks.clear()
# print(marks)

# question -11 
student_marks = {
    "Python" : input("Enter the python: ")
}