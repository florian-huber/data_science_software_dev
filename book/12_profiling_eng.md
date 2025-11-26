# Profiling in Python

In this session, we'll explore how to **measure the performance** of Python code using different profiling tools. Profiling helps us understand *where* our program spends its time so that we can optimize the right parts of the code instead of guessing.

------

## Why Profiling Matters

In many Python and data science projects, we work with **large datasets** or **computationally expensive algorithms**. Sometimes your code is “fast enough”, and sometimes it clearly isn’t. Profiling helps you decide:

- *Where* is my program spending most of the time?
- *Which* functions or lines of code are the real bottlenecks?
- *Which* optimization will actually have an impact?

Common mistakes without profiling:

- You optimize code that is already fast, while the real problem is somewhere else.
- You switch to a more complex algorithm or library “because it should be faster”, without actually measuring it.
- You rely on intuition instead of data.

**Rule of thumb:**
 Don’t guess about performance – **measure first, optimize second**.

------

## Using the `time` Module

The `time` module provides basic timing functions. This is often the first tool you reach for when you just want a rough idea of how long something takes.

A typical pattern is:

```python
import time

def integer_sum(count_to: int):
    total = 0
    for i in range(int(count_to)):
        total += i
    return total

start_time = time.time()
integer_sum(1_000_000)
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
```

**Explanation:**

- `time.perf_counter()` returns a high-precision timer suitable for measuring short durations.
   (It’s usually **better than** `time.time()` for benchmarking because it is more precise and monotonic.)
- We record the time **before** and **after** the function call and subtract the two values.
- The result is a **single measurement** of the runtime.

**Limitations:**

- It only measures one run – which might be noisy if your system is busy.
- It’s easy to accidentally include things in the timing that you don’t want (e.g. printing, data setup).
- Good for quick, rough checks—but not ideal for precise comparisons.

------

## Using the `timeit` Module

The `timeit` module is designed for **reliable micro-benchmarks**. It:

- Runs your code many times,
- Tries to reduce noise,
- Returns the total time so you can compute averages.

Simple example:

```python
import timeit

code_to_test = """
total = 0
for i in range(int(1e5)):
    total += i
"""

execution_time = timeit.timeit(stmt=code_to_test, number=100)
print(f"Average execution time: {execution_time / 100:.6f} seconds")
```

**Explanation:**

- `timeit.timeit(stmt, number)` runs the string `stmt` **`number` times** and returns the *total* time.
- We divide by `number` to get the **average time per run**.
- Using a string is simple for small examples; in larger codebases, you’ll usually benchmark a function directly.

Example using a function instead of a string:

```python
import timeit

def integer_sum(count_to: int = 100_000):
    total = 0
    for i in range(int(count_to)):
        total += i
    return total

execution_time = timeit.timeit(stmt=integer_sum, number=100)
print(f"Average execution time: {execution_time / 100:.6f} seconds")
```

This has the advantage that:

- Your code stays **normal Python code**,
- You get editor support (linting, autocomplete),
- It’s easier to maintain longer examples.

------

## Jupyter Notebook Magics

In Jupyter notebooks, there are convenient **magic commands** that wrap `time` and `timeit` for you:

- `%time` / `%%time` – single measurement,
- `%timeit` / `%%timeit` – multiple measurements, like `timeit.timeit()`.

### Line vs Cell Magics

- `%time` or `%timeit` at the start of a **single line**:

  ```python
  %time
  
  integer_sum(1_000_000)
  ```

- `%%time` or `%%timeit` at the top of a **cell**:

  ```python
  %%time
  
  result = integer_sum(1_000_000)
  result2 = integer_sum(1_000_000)
  ```

`%timeit` (and `%%timeit`) will:

- Run the code multiple times,
- Show the **best** or **mean** runtime,
- Also show the **standard deviation**.

You can control the number of runs, for example:

```python
%%timeit -n 10 -r 5

integer_sum(1000_000)
```

- `-n 10`: 10 loops per run
- `-r 5`: repeat the whole measurement 5 times

So in total, the function is called `10 * 5 = 50` times.

------

## Practical Task: Finding the Minimum Value

Now let’s apply these tools to a simple but realistic task:

> **Find the minimum value in a large list of random integers.**

We’ll implement three methods:

1. A manual **for loop**,
2. The built-in **`min()`** function,
3. A solution based on **NumPy**.

Then we’ll measure and compare their performance.

### Setup: Creating a Large Random List

```python
import random

random.seed(42)  # make the experiment reproducible

random_list = [random.randint(0, 1_000_000) for _ in range(1_000_000)]
```

**Explanation:**

- `random.seed(42)` ensures we always generate the same random numbers – useful for reproducible experiments.
- We create a list of 1,000,000 integers between `0` and `1_000_000`.

------

### Method 1: Using a For Loop

```python
def find_min_loop(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value
```

**Explanation:**

- We initialize `min_value` with the **first element** of the list.
- We iterate once over the list and update `min_value` whenever we find a smaller value.
- Time complexity: **O(n)** (we look at each element exactly once).

------

### Method 2: Using the Built-in `min()` Function

```python
def find_min_builtin(lst):
    return min(lst)
```

**Explanation:**

- Python’s built-in `min()` function also runs in **O(n)** time.
- However, it is implemented in **highly optimized C code**, and usually runs **faster** than our pure Python loop.
- It is also more readable and less error-prone.

------

### Method 3: Using NumPy

```python
import numpy as np

def find_min_numpy(lst):
    np_array = np.array(lst)
    return np.min(np_array)
```

**Explanation:**

- We first convert the Python list into a `numpy.ndarray`.
- Then we use `np.min()` to compute the minimum.
- NumPy operations are implemented in C and are often very fast on large arrays.

However, we must be aware of the **conversion cost**:

- Creating the NumPy array from a list (`np.array(lst)`) already takes time.
- If we only call `find_min_numpy()` once, the conversion overhead might dominate and make this approach *slower* than `min(lst)`.
- NumPy becomes really beneficial when:
  - The data is **already** in a NumPy array,
  - Or we perform many operations on the same array.

------

## Comparing the Performance

We now use `timeit` to measure all three approaches.

> **Note:** In a notebook, you might use `%%timeit` instead. Here we’ll stick to `timeit.timeit()` so the code also works as a script.

Make sure the functions and `random_list` are already defined before you run the timings.

### Timing Method 1: For Loop

```python
import timeit

execution_time_loop = timeit.timeit(
    stmt='find_min_loop(random_list)',
    setup='from __main__ import find_min_loop, random_list',
    number=10,
)

print(f"Average execution time (loop): {execution_time_loop / 10:.6f} seconds")
```

### Timing Method 2: Built-in `min()`

```python
execution_time_builtin = timeit.timeit(
    stmt='find_min_builtin(random_list)',
    setup='from __main__ import find_min_builtin, random_list',
    number=10,
)

print(f"Average execution time (builtin): {execution_time_builtin / 10:.6f} seconds")
```

### Timing Method 3: NumPy

```python
execution_time_numpy = timeit.timeit(
    stmt='find_min_numpy(random_list)',
    setup='from __main__ import find_min_numpy, random_list, np',
    number=10,
)

print(f"Average execution time (NumPy): {execution_time_numpy / 10:.6f} seconds")
```

### Interpreting the Results

Typically, you might see something like:

- Built-in `min()` is the **fastest**,
- The manual loop is **slower**,
- The NumPy version is:
  - very fast if the data is already a NumPy array,
  - but potentially slower than `min()` if we include the cost of creating the NumPy array.

The important lesson:

> All three methods are **O(n)**, but constant factors matter – and C-implemented built-ins are often significantly faster than pure Python loops.

------

## Advanced Profiling with `cProfile` and `snakeviz`

Timing is great when you want to compare *whole* functions or approaches. But what if you have a **larger program** and you want to know *which internal functions* are slow?

For that, we use **profilers** like `cProfile`, which can show:

- How often each function is called,
- How much time each function uses,
- How much time is spent in sub-calls.

`snakeviz` then helps visualize this information.

------

### Understanding the Code

We’ll profile the following script, which simulates:

- Data generation,
- Validation,
- Searching for target values,
- Rendering a result slowly in the terminal.

```python
import random
import time

def generate():
    data = [random.randint(0, 99) for _ in range(1, 100000)]
    data = validate(data)
    return data

def validate(data, chance_percent=50):
    data = [x for x in data if random.randint(1, 100) > chance_percent]
    return data

def search_function(data, targets=[42, 17]):
    counter = 0
    for value in data:
        if value in targets:
            counter += 1
    return counter

def ascii_renderer(result):
    message = f"I found the targets {result} times!"
    for char in message:
        time.sleep(0.01)
        print(char, end="")
    print()  # For newline after the message.

def main():
    data = generate()
    result = search_function(data)
    ascii_renderer(result)

if __name__ == "__main__":
    main()
```

What do the functions do?

- `generate()`
   Creates a list of random integers and calls `validate()` to filter it.
- `validate(data, chance_percent)`
   Keeps each element with a probability of `(100 - chance_percent)%`.
   For `chance_percent=50`, roughly half of the values are kept.
- `search_function(data, targets)`
   Counts how many elements of `data` are equal to any of the `targets`.
- `ascii_renderer(result)`
   Prints a message character by character, with a small delay (`sleep`) between characters.
   This simulates a slow output operation.

------

### Adding Docstrings and Cleaning the Code

Let’s add docstrings and make the code a bit clearer and more maintainable:

```python
import random
import time

def generate():
    """
    Generate a list of random integers between 0 and 99, validate it, and return the data.

    Returns:
        list[int]: A validated list of random integers.
    """
    data = [random.randint(0, 99) for _ in range(1, 100000)]
    data = validate(data)
    return data

def validate(data, chance_percent=50):
    """
    Filter the data list based on a random chance.

    Args:
        data (list[int]): The list of integers to validate.
        chance_percent (int, optional): Percentage chance to filter out elements.
            Higher values remove more elements. Defaults to 50.

    Returns:
        list[int]: The filtered list of integers.
    """
    data = [x for x in data if random.randint(1, 100) > chance_percent]
    return data

def search_function(data, targets=[42, 17]):
    """
    Count how many times target values appear in the data list.

    Args:
        data (list[int]): The list of integers to search.
        targets (list[int], optional): Target integers to search for.
            Defaults to [42, 17].

    Returns:
        int: The count of target values found in the data.
    """
    counter = 0
    for value in data:
        if value in targets:
            counter += 1
    return counter

def ascii_renderer(result):
    """
    Print a message character by character with a delay.

    Args:
        result (int): The result count to include in the message.
    """
    message = f"I found the targets {result} times!"
    for char in message:
        time.sleep(0.01)
        print(char, end="")
    print()  # For newline after the message.

def main():
    """
    Orchestrate the program: generate data, search, and render the result.
    """
    data = generate()
    result = search_function(data)
    ascii_renderer(result)

if __name__ == "__main__":
    main()
```

**Why bother with this before profiling?**

- Profiling tells you which function is slow – so your function names and docstrings should be clear enough that you immediately understand what’s going on.
- Clean code makes it easier to interpret and act on profiling results.

------

### Profiling with `cProfile`

`cProfile` is a built-in profiler that measures function call statistics.

#### Running `cProfile` from the Command Line

Save the script as `profile_example.py`, then in the terminal:

```bash
python -m cProfile profile_example.py
```

This runs your script under the profiler and prints a table of profiling results.

#### Output Interpretation

A typical output looks like:

```text
         50007 function calls in 1.215 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    1.215    1.215 profile_example.py:42(main)
        1    0.197    0.197    1.210    1.210 profile_example.py:8(generate)
        1    0.167    0.167    1.013    1.013 profile_example.py:15(validate)
    99999    0.846    0.000    0.846    0.000 profile_example.py:16(<listcomp>)
        1    0.001    0.001    0.004    0.004 profile_example.py:22(search_function)
    49996    0.004    0.000    0.004    0.000 profile_example.py:24(<listcomp>)
        1    0.000    0.000    0.000    0.000 profile_example.py:33(ascii_renderer)
       32    0.000    0.000    0.000    0.000 {built-in method time.sleep}
```

Column meanings:

- **ncalls** – how many times the function was called.
- **tottime** – total time spent in this function **excluding** sub-function calls.
- **percall** (tottime) – `tottime / ncalls`.
- **cumtime** – cumulative time spent in this function **including** sub-function calls.
- **percall** (cumtime) – `cumtime / ncalls`.
- **filename:lineno(function)** – where the function is defined.

#### Interpreting the Result – Which Parts Take the Longest?

Look at the lines with the **largest `cumtime`** and/or `tottime`:

- `main` has `cumtime ~ 1.215s` – that’s the *total* runtime of the program.
- `generate` has a large `cumtime` – most time is spent inside this function and what it calls.
- Our list comprehension inside `validate` (`<listcomp>`) has a high `tottime` – this is where a lot of CPU work is happening (filtering the data).
- In this particular output, `ascii_renderer` and `time.sleep` appear cheap (near 0), but that depends on the numbers and timer resolution. If we increased `time.sleep(0.01)` to, say, `time.sleep(0.1)`, then `time.sleep` would suddenly become the dominating cost.

Typical teaching question at this point:

> **Which function or line should we optimize first?**

From the example above, possible answers:

- The **list comprehension in `validate`** – it is called many times and takes a lot of time.
- If `time.sleep` were more significant, we might decide to reduce the delay or remove it entirely in production code.

The key lesson:

> Profiling tells you *exactly* where the time goes.
>  You don’t need to guess which function is slow – you can **read it off the table**.

------

### Visualizing with `snakeviz`

Text tables are powerful, but sometimes it’s easier to see performance data **as a graphic**.

`snakeviz` is a tool that reads profile data and displays it as an **interactive visualization**.

#### Installation

```bash
pip install snakeviz
```

#### Generating Profile Data

Instead of printing the stats directly, let’s write them to a file:

```bash
python -m cProfile -o profile_data.prof profile_example.py
```

- The `-o profile_data.prof` option tells `cProfile` to store the profiling data in a file.

#### Visualizing the Profile

Now launch snakeviz:

```bash
snakeviz profile_data.prof
```

This should open a web browser window (or a tab) with:

- A **sunburst diagram** or **icicle plot**,
- A table with function statistics.

#### Interpreting the Visualization

In the sunburst diagram:

- The **center** is typically the starting function (e.g. `main`).
- Each ring segment represents a function call.
- The **size** of a segment corresponds to how much time was spent there.
  - Larger segments = more time = more important to look at.
- Clicking on a segment zooms in and shows more details.

You can ask yourself:

- Which segment is the **largest**?
- Is most of the time spent in:
  - Data generation?
  - Validation/filtering?
  - Searching?
  - Rendering / printing?

Then you can decide where to try optimizations:

- Change an algorithm,
- Use a more efficient data structure,
- Avoid unnecessary work,
- Move slow I/O off the hot path, etc.

------

## Conclusion

By now, we’ve seen different levels of performance analysis in Python:

- **Basic timing**
  - `time.perf_counter()` for quick, manual measurements.
  - `timeit` for more reliable micro-benchmarks.
  - Jupyter magics `%time` and `%timeit` for convenience in notebooks.
- **Advanced profiling**
  - `cProfile` gives function-level statistics: calls, total time, cumulative time.
  - `snakeviz` visualizes profiling data and makes bottlenecks easier to spot.
- **Optimization workflow**
  1. **Measure** – use timing/profiling to find the real bottleneck.
  2. **Reason** – understand *why* that part is slow (algorithm, data structure, I/O, etc.).
  3. **Change** – try an improved implementation.
  4. **Measure again** – verify that things actually improved and that you didn’t just move the bottleneck.

**Key Takeaways:**

- Don’t optimize blindly – **profile first**.
- Built-in functions and well-optimized libraries (like NumPy) are often faster than hand-written loops.
- Clean, well-documented code makes interpreting profiling results much easier.
- Profiling and optimization are **iterative** – you repeat the cycle as your code and data evolve.