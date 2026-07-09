# A dictionary stores data in key-value pairs and is mutable.
# It is declared using curly braces: { "key": "value" }
dict_example = {"name": "jayant"}
print(type(dict_example), dict_example)

# Keys must be unique. Values can be any data type (float, boolean, integer, string, list, etc.).
model_profile = {
    "name": "gemini-2.5-flash-lite",       # string value
    "version": 2.5,                        # float
    "is_active": True,                     # boolean
    "supported_languages": ["Python", "TypeScript", "Go"]  # list
}

# ------------------------------------------------------------------------------------------------------------
# Operations on Dictionaries:
# ------------------------------------------------------------------------------------------------------------

# --- Accessing Values ---
# Syntax: variable_name["key_name"]
print(model_profile["version"])

# Safe access / checking existence: .get("key_name") returns None if missing instead of crashing
print(model_profile.get("is_active"))

# ---------------------------------------------------------------------------------------------------------
# --- Adding / Updating ---
# Syntax: variable_name["key_name"] = "value_item"
model_profile["Paid"] = "yes"
print(model_profile)

# ----------------------------------------------------------------------------------------------------------
# --- Removing / Deleting ---

# Option A: Delete entire key:value pair completely
# Syntax: del variable_name["key_name"]
del model_profile["Paid"]
print(model_profile)

# Option B: Delete the key name from the dictionary but extract its value into an independent variable
# Syntax: new_variable_name = dictionary_variable_name.pop("key_name") 
user_profile = {
    "username": "jayant_dev",
    "status": "active"
}

current_status = user_profile.pop("status")
 
print(user_profile)    # Output: {'username': 'jayant_dev'} (The status pair is deleted!)
print(current_status)  # Output: active (The value is safely saved independently here!)

# -----------------------------------------------------------------------------------------------------------
# --- Extracting---

print(model_profile.keys())    # Extract the list of all keys
print(model_profile.values())  # Extract the list of all values
print(model_profile.items())   # Extract tuples of both keys and values together