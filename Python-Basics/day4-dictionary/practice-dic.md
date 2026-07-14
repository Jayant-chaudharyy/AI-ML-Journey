# Python Day 5: Dictionaries Practice

Test your understanding of creating, accessing, modifying, and safely extracting data from dictionaries. Write your Python solutions directly below each question.

### 1. Simple Dictionary Creation
Create a dictionary named `ai_agent` with three keys: `"name"` (a string), `"mode"` (a string), and `"max_tokens"` (an integer). Assign them appropriate values.

### 2. Accessing a Value
Using the `ai_agent` dictionary from Question 1, print only the value associated with the `"max_tokens"` key.

### 3. Adding a New Key-Value Pair
Add a new key called `"temperature"` with a float value of `0.7` to your `ai_agent` dictionary and print the updated dictionary.

### 4. Updating an Existing Key
Update the `"mode"` key inside your `ai_agent` dictionary from its current value to `"coding"`.

### 5. Safe Access with .get()
Use the `.get()` method to look up a key named `"api_key"`. Print the result to observe how it handles a missing key without crashing.

### 6. The pop() Extraction Power Move
Create a dictionary named `db_record` with the keys `{"user_id": 101, "role": "admin", "temp_token": "xyz123"}`. Use the `.pop()` method to delete the `"temp_token"` key from the dictionary while simultaneously saving its value into a brand new independent variable named `active_token`. Print both the updated dictionary and the new variable.

### 7. Complete Deletion
Use the `del` keyword to permanently remove the `"role"` key from your `db_record` dictionary.

### 8. Gathering All Keys
Use the appropriate dictionary method to extract and print a collection of all the **keys** present in your `ai_agent` dictionary.

### 9. Gathering All Values
Use the appropriate dictionary method to extract and print a collection of all the **values** present in your `ai_agent` dictionary.

### 10. Checking Key Existence
Write a line of code using the `in` keyword to check if the key `"version"` exists inside your `ai_agent` dictionary, printing the resulting boolean (`True` or `False`).

### 11. Dictionary with a List Value
Create a dictionary named `course_info` with keys for `"title"` (`"Python for AI"`) and `"topics"`. The value for `"topics"` must be a list containing three strings: `"Variables"`, `"Lists"`, and `"Dictionaries"`. Print the entire dictionary.

### 12. Accessing Data Inside a Nested List
Using the `course_info` dictionary from Question 11, write a print statement that targets the dictionary key and list index to print only the word `"Dictionaries"` from that internal list.

### 13. Deeply Nested Dictionaries (API Style)
Create a dictionary named `api_response` that mimics data from a web server. Give it two keys: `"status"` (integer `200`) and `"data"`. The value of `"data"` must be another dictionary containing `{"model_id": "gemini-flash", "latency_ms": 120}`. Print the complete structure.

### 14. Extracting from a Nested Dictionary
Using the `api_response` dictionary from Question 13, write a single line of code to dig into the nested structure and print only the value of `"latency_ms"`.

### 15. The Items Collection
Use the `.items()` method on your `ai_agent` dictionary to extract its content. Look closely at the print output—what two data collection types combined does Python use under the hood to display these pairs?