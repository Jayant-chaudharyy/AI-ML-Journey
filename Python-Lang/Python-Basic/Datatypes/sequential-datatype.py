#  Lists

# # question - 1
# programming_lang = ["Python", "Java", "C++", "JavaScript", "SQL"]
# print(programming_lang)
# print(programming_lang[0])
# print(programming_lang[-1])
# print(type(programming_lang))

# # question -2
# fav_foods = [
#     input("Enter food 1: "),
#     input("Enter food 2: "),
#     input("Enter food 3: "),
#     input("Enter food 4: "),
#     input("Enter food 5: ")
# ]

# print(fav_foods, type(fav_foods))
# print(len(fav_foods))
# print(fav_foods[0])
# print(fav_foods[-1])

# #question -3
# numbers = [10, 20, 30, 40, 50, 60, 70]
# print(numbers[0])
# print(numbers[3])
# print(numbers[-1])
# print(numbers[-3])

# # question -4
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# print("The First 4 elements : ", numbers[:4])
# print("Last 3 elements : ", numbers[:3:-1])
# print("Elements from index `2` to `5` : ", numbers[2:6])
# print("Every second element : ", numbers[::2])
# print("The reversed list using slicing : ", numbers[::-1])

# # question -5
# languages = ["Python", "Java", "C++", "SQL"]
# languages[1] = "Javascript"
# languages[3] = "MySQL"
# print(languages)

# # question -6
# skills = ["Python", "SQL"]
# skills.append("Pandas")
# skills.append("Numpy")
# skills.insert(1, "Machine Learning")
# print(skills)

# # question -7
# languages = ["Python", "Java", "C++", "JavaScript", "SQL"]
# languages.remove("Java")
# languages.pop()
# languages.pop(1)
# print(languages)

# #  question -8
# numbers = [10, 20, 10, 30, 40, 10, 50]
# print(numbers.count(10))
# print(numbers.index(30))
# print(len(numbers))

# # question -9
# marks = [78, 45, 92, 61, 88, 55]
# print("original: ",marks)
# marks.sort()
# print("Ascending : ",marks)
# marks.sort(reverse=True)
# print("decending : ",marks)

# # question -10
# languages = ["Python", "Java", "C++", "JavaScript", "SQL"]
# search = input("Enter the language to search : ")
# print("Language exists:", search in languages)
# print("Language does not exist:", search not in languages)

# # question -11
# python_topics = ["Variables", "Strings", "Lists"]
# math_topics = ["Algebra", "Statistics", "Calculus"]
# list_3 = python_topics + math_topics
# print("List 3 : ", list_3)
# print("Length of combined List : ", len(list_3))

# # question -12
# a = [10, 20, 30]
# b = a
# print(a)
# b.append(40)
# print(b)

# # or
# a = [10, 20, 30]
# b = a.copy()
# print(a)
# b.append(40)
# print(b)

# #  Question -13
# marks = [
#     int(input("subject 1 marks : ")),
#     int(input("subject 2 marks : ")),
#     int(input("subject 3 marks : ")),
#     int(input("subject 4 marks : ")),
#     int(input("subject 5 marks : "))
#     ]
# print("Total Marks: ", sum(marks))
# avg = (sum(marks))/5
# print("Average Marks: ", avg)
# print("Highest Marks: ",max(marks))
# print("Highest Marks: ",min(marks))

# # question - 14
# students = [
#     ["Jayant", 85],
#     ["Rahul", 72],
#     ["Aman", 91]
# ]
# print("Jayant`s name: ", students[0][0])
# print("Jayant`s marks: ", students[0][0])
# print("Aman`s marks: ", students[2][0])
# print("Aman`s marks: ", students[2][1])

# students[1][1] = 80
# print(students)

# # qusetion -15
# user_intput = [
#     input("subject 1 marks : "),
#     input("subject 2 marks : "),
#     input("subject 3 marks : "),
#     input("subject 4 marks : "),
#     input("subject 5 marks : ")
#     ]
# print("original list :", user_intput)
# user_intput.append("Python")
# print("Added Python",user_intput)
# user_intput.pop()
# print("Last Skill removed",user_intput)
# user_intput.sort()
# print("Alphabertically Sorted :",user_intput)
# print("Last Skill: ",user_intput[-1])
# print("Last Skill: ",len(user_intput))
# print("Python Present: ", "Python" in user_intput)