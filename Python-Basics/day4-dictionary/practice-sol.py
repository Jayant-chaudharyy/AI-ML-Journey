
# Question - 1
ai_agents = {
    "name": "Gemini",
    "mode": "code",
    "max_tokens": 100
}
print(ai_agents)

# Question - 2
print(ai_agents["max_tokens"])

# Question - 3
ai_agents["temperature"] = 0.7
print(ai_agents)

# Question - 4
ai_agents["mode"] = "coding"
print(ai_agents)

# Question - 5
print(ai_agents.get("api_key"))

# Question - 6
db_records = {
    "user_id": 101, "role": "admin", "temp_token": "xyz123"
}
print(db_records)

active_token = db_records.pop("temp_token")
print(f"active_token is : {active_token}")
print(db_records)

# Question - 7
del db_records["role"]
print(db_records)

# Question - 8
print("Keys are : ", ai_agents.keys())

# Question - 9
print(ai_agents.values())

# Question - 10
print("version" in ai_agents)

# Question - 11
course_info = {
    "title": "Ai for python",
    "topics": ["variable", "List", "Dictionaryes"]
}
print(course_info)

# Question - 12
print(course_info["topics"][-1])

# Question - 13
api_response = {
    "status": 200, "data": {"model_id": "gemini-flash", "latency_ms": 120}
}
print(api_response)

# Question - 14
print(api_response["data"]["latency_ms"])

# Question - 15
print(ai_agents.items())