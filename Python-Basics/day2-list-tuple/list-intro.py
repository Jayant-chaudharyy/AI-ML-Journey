# creating a list
example_list = ["this", "is", "the", "example", "list"]
print(example_list)

# we can also create multi datatype list
multi_type_list = [1, "two", 2.5, True]
print(multi_type_list)

# we can perform the string operation on list as well
# len()
print(len(multi_type_list))

# type()
print(type(multi_type_list))

# indexing/accesing
print(multi_type_list[1])
print(multi_type_list[:4])
print(multi_type_list[1:3])

# list are mutable so we can add, update and delete the data
# add
multi_type_list.append(False)  # add element in last
multi_type_list.insert(2, "new")  # add element at specified index
print(multi_type_list)

# delete
multi_type_list.pop() #delete last element in list
multi_type_list.remove(2.5) #remove the specified element from the list

print(multi_type_list)

#calculation the length of list
print(len(multi_type_list))

# combining the lists
new_list = multi_type_list + example_list
print(new_list) 
