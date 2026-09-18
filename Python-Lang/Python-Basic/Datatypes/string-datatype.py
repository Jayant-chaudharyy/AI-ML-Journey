# question -1

name = "jayant chaudhary"
print(f"My name is {name}", type(name))

# question -2
name = "Jayant"
course = "MCA AI/ML"
university = "Bennett university"

print(f"Name: {name}")
print(f"Course: {course}")
print(f"University: {university}")

# question -3
first_name = "Jayant"
last_name = "Chaudhary"
full_name = first_name + " " + last_name
print(full_name)

# question -4
word = "python"
print(word*3)

# question -5
a = str(input("Enter the text here: "))
print(f"The user string is {a}")
print("The length of string is ", len(a))

# question -6
text = "python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# question -7
text = "PROGRAMMING"
print(text[-1])
print(text[-2])
print(text[-3])

# question -8
text = "PYTHON"
print(text[0])
print(text[2])
print(text[-1])
print(text[-2])

# question -9
text = "PROGRAMMING"
print(text[:4])
print(text[-4:])
print(text[2:7])

# question -10
str_a = str(input("ENTER THE TEXT :"))
print(str_a[::-1])

# question -11
b = str(input("Enter the text: "))
print(b)
print(b.upper())
print(b.lower())
print(b.capitalize())
print(b.swapcase())

# question -12
text = "   Python is Amazing   "
print(text.strip())

# question -13
text = "I love Java"
print(text.replace("Java", "Python"))

# Question -14
text = "Python is easy to learn and Python is powerful"
print(text.find("Python"))
print(text.find("powerful"))

# question -15
a = str(input("Enter the text: "))
b = str(input("Enter the character: "))
print(a.count(b))

# question -16
sent_1 = str(input("Enter the sentance: "))
word_1 = str(input("enter the word: "))
print(f"The {word_1} is present in the sentence: ", word_1 in sent_1)
print(f"The {word_1} is not present in the sentence: ", word_1 not in sent_1)

# question -17
file_name_user = input("Enter the file name: ")
print("The file name starts with the Word Data:",file_name_user.startswith("data"))
print("The file name ends with the .csv:",file_name_user.endswith(".csv"))

# question -18
sent_user = input("Enter the sentance: ")
words = sent_user.split()
print(words, len(words))

# question -19
first_name = str(input("Enter the First Name: "))
last_name = str(input("Enter the Last Name: "))
birth_year = int(input("Enter the Birth Year: "))
birth_year_str = str(birth_year)

user_name = first_name + "." + last_name + birth_year_str
print("Username: ", user_name.lower())

# question -20
full_name = str(input("Enter the Full Name: "))
clg_name = str(input("Enter the college Name: "))
course_name = str(input("Enter the course Name: "))
city_name = str(input("Enter the city Name: "))
e_mail = str(input("Enter the E Mail: "))

# part -1
print("====================================")
print("Student Profile")
print("====================================")
print(f"Name: {full_name}")
print(f"College Name: {clg_name}")
print(f"Course Name: {course_name}")
print(f"City Name: {city_name}")
print(f"E Mail: {e_mail}")
print("====================================")

# Part -2
print(f"Name: {full_name.upper()}")
print(f"Name: {full_name.lower()}")
print("Name Length: ", len(full_name))
print("First Character: ", full_name[0])
print("Last Character: ", full_name[-1])
print("E Mail Conatain @: ", '@' in e_mail)
print("E Mail Ends with .com: {e_mail}", e_mail.endswith(".com"))
user_name = full_name.replace(" ", "_")
print(f"UserName: {user_name}")
