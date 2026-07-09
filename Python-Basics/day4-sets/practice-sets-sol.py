# Question -1
tech_stack = {"typescript", "next.js", "firebase"}

# Question -2
tech_stack = {"typescript", "next.js", "firebase", "next.js"}
print(tech_stack)

# Question -3
tech_stack.add("python")
print(tech_stack)

# Question -4
tech_stack.remove("firebase")
# or tech_stack.discart("firebase")

# Question -5
print("typescript" in tech_stack)

# Question -6
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b
print(f"The union of  set a and b is :{union_set}")

#Question -7
intersection_set = set_a & set_b
print(f"the intersection of set a and b is : {intersection_set}")

#Question -8
diff = set_a - set_b
print(f"this will find and return the items which are present in seta but absent in set b {diff}")

#Question -9
list_1 = [10,20,20,30,30]
list_set = set(list_1)
print(type(list_set),list_set)

#Question -10
print(tech_stack[0],"this will give error because sets doesnt have index so item cant be accesse through there index value")