# 🐍 Python Loops — Assessment

**Total Questions:** 15  
**Difficulty:** Beginner → Intermediate  
**Topics:** `for`, `while`, `range()`, `break`, `continue`, nested loops

---

# 🟢 Part A — Basic `for` Loops

### Q1. Print Numbers

Use a `for` loop and `range()` to print numbers from **1 to 10**.

Expected output:

```text
1
2
3
4
5
6
7
8
9
10
```

### Q2. Even Numbers

Use a `for` loop and `range()` to print all even numbers from **2 to 50**, including 50.

### Q3. Sum of Numbers

Take an integer `n` from the user.

Calculate the sum of all numbers from **1 to n** using a loop.

Example:

```text
Enter n: 5
Sum: 15
```

### Q4. Multiplication Table

Take a number from the user and print its multiplication table from **1 to 10**.

Example:

```text
Enter a number: 5

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

### Q5. Iterate Through a String

Take a string from the user.

Use a `for` loop to:

1. Print each character on a separate line.
2. Count the number of vowels (`a, e, i, o, u`), ignoring case.

---

# 🟡 Part B — `while` Loops

### Q6. Countdown

Use a `while` loop to print numbers from **10 down to 1**, followed by:

```text
Blast off!
```

### Q7. Sum Until Zero

Keep asking the user to enter an integer.

- Add each number to a running total.
- Stop when the user enters `0`.
- Do not include anything after the stopping `0` in the total.

Example:

```text
Enter a number: 10
Enter a number: 20
Enter a number: 5
Enter a number: 0

Total: 35
```

### Q8. Guess the Number

Set a secret number in your code, for example:

```python
secret_number = 7
```

Keep asking the user to guess the number using a `while` loop.

- If the guess is too low, print `"Too low!"`
- If the guess is too high, print `"Too high!"`
- If correct, print `"Correct guess!"` and stop the loop.

### Q9. Count Digits

Take a positive integer from the user.

Count how many digits it contains using a `while` loop.

Example:

```text
Enter a number: 58321
Number of digits: 5
```

Challenge: Make sure your program also handles `0` correctly.

---

# 🟠 Part C — Loop Control & Sequences

### Q10. `break` — Stop at a Number

Take an integer `n` from the user.

Use a `for` loop to print numbers from 1 to `n`, but stop immediately when the loop reaches **7**.

If `n` is less than 7, print all numbers from 1 to `n`.

Use `break`.

### Q11. `continue` — Skip Multiples of 3

Use a `for` loop to print numbers from **1 to 30**, skipping all numbers divisible by 3.

Use `continue`.

### Q12. List Processing

Given:

```python
numbers = [12, 7, 20, 3, 18, 5, 30, 11]
```

Use a loop to:

1. Print every number.
2. Calculate the sum of all numbers.
3. Count how many numbers are even.
4. Print only the numbers greater than 10.

Do not use `sum()` or list comprehensions for this question.

---

# 🔴 Part D — Intermediate Challenges

### Q13. Factorial

Take a non-negative integer `n` from the user.

Calculate its factorial using a loop.

Factorial means multiplying all positive integers from 1 through `n`.

Example:

```text
Enter a number: 5
Factorial: 120
```

Remember:

- `5! = 5 × 4 × 3 × 2 × 1 = 120`
- `0! = 1`

### Q14. Nested Loops — Star Pattern

Take an integer `n` from the user.

Use **nested `for` loops** to print this pattern when `n = 5`:

```text
*
**
***
****
*****
```

Do not manually print each row. Use loops to build the pattern.

### Q15. 🔥 Final Challenge — Number Analysis System

Take a positive integer `n` from the user.

Using loops and conditionals, analyze every number from **1 to n**.

Your program must:

1. Print all numbers from 1 to `n`.
2. Calculate their sum.
3. Count the even numbers.
4. Count the odd numbers.
5. Print all numbers divisible by both 3 and 5.
6. Calculate the factorial of `n` if `n` is between 0 and 10 inclusive.

Example for `n = 10`:

```text
Numbers: 1 2 3 4 5 6 7 8 9 10
Sum: 55
Even count: 5
Odd count: 5
Numbers divisible by both 3 and 5: None
Factorial: 3628800
```

For this challenge, try to use loops rather than relying on built-in shortcuts.

---

# 🎯 Loop Concepts Checklist

After completing the assessment, you should understand:

```python
for
while
range(stop)
range(start, stop)
range(start, stop, step)
break
continue
nested loops
loop counters
running totals
accumulators
loop conditions
```

You should also understand the difference between:

- **`for` loop:** useful when iterating over a sequence or a known range.
- **`while` loop:** useful when repeating an operation until a condition changes.
- **`break`:** exits the loop immediately.
- **`continue`:** skips the rest of the current iteration and proceeds to the next one.
- **Nested loops:** a loop running inside another loop.
