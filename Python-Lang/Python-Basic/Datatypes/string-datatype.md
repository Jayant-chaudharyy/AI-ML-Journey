# Day 1 Practice Lab: Python Numeric Data Types & Operations

---

### Phase 1: Basic Arithmetic & Division Rules (Questions 1–6)

1. Calculate the result of dividing `17` by `4` using standard division (`/`). What data type is the result?
2. Perform floor division (`//`) with `17` and `4`. What is the output?
3. Calculate the modulus (`%`) of `17` and `4` to find the remaining value.
4. Evaluate the expression `2 ** 4`. What does this calculate?
5. Predict and calculate the output of `10 / 2` versus `10 // 2`. Explain the data type difference.
6. Calculate `-11 // 3` and `-11 % 3`. (Pay attention to how floor division rounds down for negative numbers!)

---

### Phase 2: Assignment Operators (Questions 7–11)

7. Set `x = 15`. Use the `+=` operator to add `5` to `x`. Print `x`.
8. Set `y = 20`. Use the `/=` operator to divide `y` by `4`. What is the final data type of `y`?
9. Set `z = 7`. Use the `**=` operator to raise `z` to the power of `2`. Print `z`.
10. Set `count = 25`. Use the `%=` operator to find `count %= 6`. What is stored in `count`?
11. Set `val = 18`. Perform `val //= 4`. Print the updated value.

---

### Phase 3: Comparison Operators (Questions 12–16)

12. Write a line of code using `==` to check if `5 + 5` equals `10.0`. What boolean value does it return?
13. Compare `15` and `20` using the `<=` operator. Print the output.
14. Check if `8 != 8.0` using the inequality operator.
15. Evaluate `(10 // 3) == (10 % 3)`. Is the result `True` or `False`?
16. Write a statement checking if `5 ** 2` is greater than or equal to (`>=`) `24`.

---

### Phase 4: Built-in Math Functions (Questions 17–22)

17. Use `abs()` to find the absolute value of `-42.8`.
18. Compute $3^4$ using the built-in `pow()` function instead of the `**` operator.
19. Round the number `7.8654` to `2` decimal places using `round()`.
20. Round `12.49` without specifying decimal places. What is the output?
21. Find the maximum and minimum values among `(14, -2, 89, 0, 42)` using `max()` and `min()`.
22. Use `pow()` with three arguments: `pow(2, 3, 5)`. *(Hint: This calculates `(2 ** 3) % 5`!)*

---

### Phase 5: Type Casting & Complex Numbers (Questions 23–27)

23. Convert the float `9.99` into an integer using `int()`. Does it round or truncate?
24. Convert the integer `42` into a float using `float()`.
25. Create a complex number representing $5 + 3j$ using the `complex()` function.
26. Given the complex number `c = 4 + 7j`, extract and print its real part (`.real`) and imaginary part (`.imag`) separately.
27. Try converting `int(3 + 4j)`. What happens, and why?

---

### Phase 6: Medium Mixed-Logic Challenges (Questions 28–30)

28. Create a variable `num = 12.678`. Round it to `1` decimal place, convert that rounded result to an `int`, and check if it is equal to `13`.
29. Calculate the hypotenuse $c$ of a right triangle where $a = 3$ and $b = 4$ using the formula $c = \sqrt{a^2 + b^2}$. Use `pow()` or `**` to compute it without importing the `math` module.
30. Given a total of `125` minutes, use floor division (`//`) and modulus (`%`) to convert it into `hours` and `remaining_minutes`. Print the result in the format: `"125 minutes = X hours and Y minutes"`.