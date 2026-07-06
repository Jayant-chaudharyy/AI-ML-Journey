# Question -1
ai_models = ["gemini", "chatgpt", "claude"]
print(ai_models)

# Question -2
print(ai_models[1])

# Question -3
ai_models.append("meta_ai")

# Question -4
ai_models[0] = "gemini-pro"
print("new lsit : ", ai_models)

# Question -5
print(len(ai_models))

# Question -6
ai_models.pop()
print(ai_models)

# Question -7
print("GPT-4" in ai_models)

# Question -8
other_models = ["perplexity", "grok"]
all_models = ai_models + other_models
print(all_models)

# Question -9
ai_models.sort()
print(ai_models)

# Question -10
ai_models.sort(reverse=True)
print(ai_models)

# Question -11
ai_models.insert(1, "Deepseek")
print(ai_models)

# Question -12
ai_models.clear()
print(ai_models)

# Question -13
num_list = [10,20,30,40,50]
sum_list = sum(num_list)
print(sum_list)

# Question -14
print(num_list[1:3])

# Question -15
list_2 = [20, 10, 20, 30, 20] 
print(list_2.count(20))