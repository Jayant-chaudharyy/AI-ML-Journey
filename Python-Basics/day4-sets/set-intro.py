# set is a datatype that stores the unordered ,indexed and non duplicate value inside it and its declared by set() or {}.
# we use set for ignoring duplicate vlaue entries.

# set is declared by mostly {} or sometimes set()
example_set = {"hello", "jayant"}
print(type(example_set), example_set)

# operation on sets:

# 1. Adding .add("item")
example_set.add("chaudhary")
print(example_set)

# 2. Remove .remove("item") or .discard("item")
example_set.remove("hello")
print(example_set)

example_set.discard("jayant")
print(example_set)

# 3. Membership
print("jayant" in example_set)

# 4. Maths operator
# ---union(|)_____-combine sets and remove duplicate
sets_1 = {1, 2, 4, 5, 6}
sets_2 = {1, 2, 4, 5, 6, 7, 8, 9, 9, 0}

set_union = sets_1 | sets_2
print(set_union)

ex_alpha = {"jayant", "chaudhary"}
ex_2 = {"jayant", "khatri"}
full_set = ex_alpha | ex_2
print(full_set)

# ---intersection(&)______-finds and return item common in sets
common_sets_items = sets_1 & sets_2
print(common_sets_items)

common_items = ex_alpha & ex_2
print(common_items)


# ---difference(-)______-find item in first set that are not in other
diff_sets = ex_alpha - ex_2
print(diff_sets)

diff_sets_2 = ex_2 - ex_alpha
print(diff_sets_2)


