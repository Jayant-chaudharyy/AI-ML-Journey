#Task 1
name = input("Enter your full name ")
age = int(input("Enter you age "))
email = input("Enter your mail id ")

student_profile = {
    "Name": name,
    "Age": age,
    "Email": email
}

#Task 2
print("Enter the marks of subjects to calculate the score and percentage")

python_marks = float(input("Enter the marks of the python "))
sql_marks = float(input("Enter the marks of the sql "))
maths_marks = float(input("Enter the marks of the maths "))

score = [python_marks, sql_marks, maths_marks]
total_subjects = len(score)

total_marks = sum(score)
print("Total marks of the student is :", total_marks)

percentage_score = (total_marks / total_subjects)
print("The percentage of marks is : ", percentage_score)

student_profile["Total Marks"] = total_marks
student_profile["Percentage"] = percentage_score

#Task 3
university_info = ("Bennett University", "MCA AI/ML")

#Task 4
required_ai_skills = {"Python", "SQL", "Machine Learning"}
student_skills = set()
for x in range(3):
    student_skills_have = input("Enter the skills you have : ")
    student_skills.add(student_skills_have)


matches_skills = required_ai_skills & student_skills
print(f"the student have matching skill : {matches_skills}", len(matches_skills), " Out of", len(required_ai_skills))

#Task 5
print("         Student Report Card        ")
print(f"Student Name : {student_profile['Name']}")
print(f"Age : {student_profile['Age']}")
print(f"Email : {student_profile['email']}")
print("\n Acedemic Details")
print(f"The Python Marks is : {score[0]}")
print(f"The SQL Marks is : {score[1]}")
print(f"The Maths Marks is : {score[2]}")
print("\n Total score")
print(f"Total score is : {total_marks}")
print(f"Percentage is : {percentage_score}")
print("\n University and course")
print(f"University : {university_info[0]}")
print(f"Course : {university_info[1]}")
print("\n skills")
print(f"Required Skills : {required_ai_skills}")
print(f"Student Skills : {student_skills}")
print(f"Matched Skills : {matches_skills}")

