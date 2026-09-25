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

# # question -11
# student_marks = {
#     "Python" : float(input("Enter the python: ")),
#     "SQL" : float(input("Enter the SQL: ")),
#     "Math" : float(input("Enter the Math: ")),
#     "AI" : float(input("Enter the AI: ")),
#     "ML" : float(input("Enter the ML: "))
# }
# marks = student_marks.values()
# total_marks = sum(marks)
# print("Total Marks ",total_marks)
# avg_marks = total_marks /5
# print("Average Marks ",avg_marks)
# print("Higest Marks ", max(marks))
# print("Higest Marks ", min(marks))

# # question -12
# student = {
#     "name": "Jayant",
#     "course": "MCA",
#     "skills": ["Python", "SQL", "Git"]
# }
# student["skills"].extend(["Pandas", "Numpy"])
# print("Skills :", student["skills"])
# print(student)

# # quuestion -13
# student_skills = {
#     input("Enter the skills-1: "),
#     input("Enter the Skills-2: "),
#     input("Enter the skills-3: "),
#     input("Enter the skills-4: "),
#     input("Enter the skills-5: ")
# }

# student = {
#     "name" : input("enter the name: "),
#     "course" : input("enter the course: "),
#     "skills" : student_skills
# }

# print(student)
# student_skills.pop()
# print(student)
# print("Python exist :", "Python" in student_skills)
# print(student)

# # question -14
# students = {
#     "student1": {
#         "name": "Jayant",
#         "age": 23,
#         "course": "MCA"
#     },
#     "student2": {
#         "name": "Rahul",
#         "age": 22,
#         "course": "BCA"
#     }
# }

# print(students["student1"]["name"])
# print(students["student1"]["course"])
# print(students["student2"]["name"])
# print(students["student2"]["course"])

# students["student2"]["course"] = "MCA"
# print(students)

# question -15
student_skills = {
    input("Enter the skills-1: "),
    input("Enter the Skills-2: "),
    input("Enter the skills-3: "),
    input("Enter the skills-4: "),
    input("Enter the skills-5: ")
}
student = {
    "name": input("enter the name: "),
    "age": int(input("enter the age: ")),
    "mail": input("enter Email: "),
    "course": input("enter the course: "),
    "university": input("enter the university: "),
    "city": input("enter the city: "),
    "skills": student_skills
}

print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student["name"])
print(student["skills"])
student_skills.add("Rust")
print("Added Skills: ", student_skills)
student_skills.discard("Rust")
print("Remove skills :", student_skills)
print("Python exist", "Python" in student_skills)
student["city"] = "meerut"
student["key"] = "0"
print(student)
