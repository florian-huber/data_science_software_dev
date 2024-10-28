# Code Smells

**Quote:** “You know you are working on clean code when each routine you read turns out to be pretty much what you expected. You can call it beautiful code when the code also makes it look like the language was made for the problem.”

- **Ward Cunningham**

------

### **What is a Code Smell?**

Code smells, or "Codegeruch" in German, are symptoms in the codebase that indicate deeper issues in the software's design or structure. Although the code might function correctly, these "smells" often make it less readable and can pose risks when changes are needed in the future.

From a high-level perspective, issues in code can range from overtly critical (such as syntax errors and bugs) to more subtle but potentially damaging ones in the long term, like formatting inconsistencies and code smells.

------

#### **Example & Live Coding Exercise:**

**Task:** Identify the problems or non-ideal patterns in the following code and then discuss and improve it with your fellow students.

```python
print("How good do you feel today? (from 1=horrible to 10=perfect)?")
user_input1 = input("Your answer:")
if user_input1 == "":
    print("I got no input...")
try:
    int(user_input1)
    if int(user_input1) not in range(1, 11):
        raise ValueError("Only numbers between 1 and 10 are allowed.")
except:
    print("You need to enter a number from 1 to 10.")

print("How do you like this course? (from 1=hate it to 10=love it)?")
user_input2 = input("Your answer:")
if user_input2 == "":
    print("I got no input...")
try:
    int(user_input2)
    if int(user_input1) not in range(1, 11):
        raise ValueError("Only numbers between 1 and 10 are allowed.")
except:
    print("You need to enter a number from 1 to 10.")
```

------

### **Common Code Smells**

1. **Duplicated Code**

   A prominent smell in the provided code was duplication. The principle of **DRY (Don't Repeat Yourself)** emphasizes that each piece of your application should have a single representation in the codebase.

   **Refactored Solution:**

```python
def get_user_input(prompt_message):
    print(prompt_message)
    user_input = input("Your answer:")
    if user_input == "":
        print("I got no input...")
        return None
    try:
        value = int(user_input)
        if value not in range(1, 11):
            raise ValueError("Only numbers between 1 and 10 are allowed.")
        return value
    except:
        print("You need to enter a number from 1 to 10.")
        return None

feeling_today = get_user_input("How good do you feel today? (from 1=horrible to 10=perfect)?")
course_opinion = get_user_input("How do you like this course? (from 1=hate it to 10=love it)?")
```

**Why Avoid Duplicated Code?**

- Increases code size unnecessarily
- Introduces more spots for potential bugs
- Makes the code harder to maintain

**When Should We Refactor?**

A general rule of thumb is the **Rule of Three**: If you are writing similar code for the third time, it's an indication that refactoring might be in order.

**Magic Numbers**

These are numbers directly used in the code without any explanatory name or context. Using named constants can make the code more readable and maintainable.

**Example:**

```python
sensor_signal = sensor_signal - 181.247
```

**Better:**

```python
MEASURED_SENSOR_OFFSET = 181.247  # last calibrated: 17.4.2022
...
sensor_signal = sensor_signal - MEASURED_SENSOR_OFFSET
```

**Dead Code / Redundant Code**

Code that is no longer used or can never be executed is just cluttering the codebase, making it harder to read and maintain.

**Example:**

```python
import random
def coin_flip():
    if random.randint(0, 1):
        return "Heads!"
    else:
        return "Tails!"
    return "The coin landed on its edge!"
```

The last return statement is unreachable and hence redundant.

### Common smell: code too complex to read

Complexity in code is not just about how many lines of code you have or how big your functions are. It's about how difficult it is to understand, maintain, and extend the code. This complexity is often introduced through various coding patterns that might seem harmless or even "efficient" at first glance but can lead to maintenance nightmares in the long run.

------

#### **Deeply Nested Code**

One major source of complexity is code that is nested too deeply. Deeply nested code is hard to read and understand because you have to keep track of which conditions or loops each line of code is part of.

**Example:**

```python
while True:
    if input_lst is None:
        break
    elif len(input_lst) > 1:
        for element in input_lst:
            if isinstance(element, str) or isinstance(element, int):
                if element != "stop" and element != "Stop":
                    try:
                        got_number = int(element)
                    except:
                        got_number = False
                    else:
                        print("OK. Stop!")
                        break
                else:
                    print("Let's see what we got:", element)
```

**Step-by-step fix:**

1. Flatten the code by returning early or breaking out of loops early.
2. Use built-in functions and libraries where possible.
3. Avoid redundant checks.

**Improved Code:**

```python
def process_elements(input_lst):
    if not input_lst:
        return

    for element in input_lst:
        if element in ["stop", "Stop"]:
            print("OK. Stop!")
            break

        if isinstance(element, (str, int)):
            try:
                _ = int(element)
                print("Let's see what we got:", element)
            except ValueError:
                pass

process_elements(input_lst)
```

------

#### **Cryptic Logic and Negations**

Code with unclear logic, especially involving negations, can be very challenging to understand.

**Example:**

```python
if not my_number != 6 or not my_number != 66:
    print ("Oh oh!")
else:
    print("All good.")
```

**Fix:** Avoid double negatives and try to make the condition as clear as possible.

**Improved Code:**

```python
if my_number == 6 or my_number == 66:
    print("Oh oh!")
else:
    print("All good.")
```

------

#### **Proper Use of `return` and `break`**

Using `return` and `break` judiciously can help you avoid unnecessary `elif` and `else` blocks, making the code clearer.

For instance, instead of having multiple `elif` or `else` blocks, you can simply `return` from a function or `break` out of a loop once you know that no further processing is needed.

------

#### **Lengthy Functions**

Functions that are too long are hard to understand, debug, and test. A function should ideally do one thing and do it well.

**Tips to handle long functions:**

1. **Break down the function**: If a function is doing multiple things, try to split it into multiple smaller functions, each with a clear purpose.
2. **Use helper functions**: If there are repetitive tasks within a function, consider using helper functions.
3. **Keep related code together**: Ensure that related lines of code are grouped together, making it easier to understand the function's flow.