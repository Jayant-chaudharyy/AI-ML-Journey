# Range is ordered sequencially collection of intergers value which is most efficent
# because it doesnt generate all value at once it generate on request.


# declaration is range(value)
range_example = range(20)
print(range_example)

# The syntax follows three parameters: range(start, stop, step)
# common pattern for range
# Single stop only method
for i in range(10):
    print(i)

# start and stop method
for x in range(1, 11):
    print("X in :", x)

# start, stop , step method
for y in range(0, 20, 2):
    print("Y in :", y)

 # its will step every 2 elements
