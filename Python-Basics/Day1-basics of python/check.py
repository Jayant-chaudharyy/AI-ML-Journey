# student_profile.py

# A dictionary stores data in key-value pairs
ai_student = {
    "name": "Jayant",
    "degree": "MCA (AI/ML)",
    "skills_learned": ["Variables", "Strings", "Floats"], # This is a List
    "target_package_lpa": 12.5,
    "is_ready": False
}

# Adding a new skill to the list inside the dictionary
ai_student["skills_learned"].append("Lists and Dictionaries")

# Printing a formatted string using the dictionary data
print(f"Update: {ai_student['name']} is currently mastering {ai_student['skills_learned'][-1]}.")