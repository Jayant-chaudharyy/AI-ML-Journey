# Question -1
ai_config = (800, 600, 1024)

# Question -2
print(ai_config[1])

# Question -3
# ai_config[0] = "900"
print("""this will give error because tuple are immutable unlike the list where data cant be change after define the data""", ai_config)


# Question -4
model = ("gemini",)
print(model)


# Question -5
ai_config_2 = (2048, 4096)
combine_tuple = ai_config + ai_config_2
print(f"combined tuple is {combine_tuple}")

# Question -6
print(len(ai_config))

# Question -7
ai_models = ("gemini", "chatgpt", "claude")
print(ai_models.index("claude"))

# Question -8
num_tuple = (10, 20, 30)
a, b, c = num_tuple
print(f"a = {a}, b = {b}, and c = {c}")

# Question -9
convert = list(ai_config)
print(type(convert))
convert[0] = "900"
print(convert)

# QUestion - 10
del ai_config_2
print(ai_config_2)
