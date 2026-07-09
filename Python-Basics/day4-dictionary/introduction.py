# its the datatype that stores the data in key value pair and it is mutable.
# its declared using the { "key":"value"}
# example
dict_example = {"name": "jayant"}
print(type(dict_example), dict_example)

# In this key should be unique and not repeating and its value can be any datatype like float, boolean, integer, string etc.

# A dictionary representing an AI model configuration
model_profile = {
    "name": "gemini-2.5-flash-lite",  # string value
    "version": 2.5,  # float
    "is_active": True,  # boolean
    "supported_languages": ["Python", "TypeScript", "Go"]  # list
}


# Operation on Dictionary :
# ---Accesing value ---:
#  variable_name["key_name"] --- syntax
print(model_profile["version"])
# to check whether key exist or not use .get("key_name")
print(model_profile.get("is_active"))


# ---Adding/Updating----:
#  variable_name["key_name"]="value_item" --- syntax
model_profile["Paid"] = "yes"
print(model_profile)


# ---Removing/Delete---:
# To Delete entire key:value pair --- del variable_name["key_name"]
del model_profile["Paid"]
print(model_profile)

# To delete the key and return its value --- variable_name.pop("key_name")
model_profile.pop("is_active")
print(model_profile)


# ---Extract----
# extract the list of keys
print(model_profile.keys())
# extract the list of value
print(model_profile.values())
# extract list of key and value
print(model_profile.items())
