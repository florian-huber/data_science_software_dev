## Live Coding Introduction to Code Testing

Testing is a crucial part of software development that ensures your code behaves as expected. In this session, we'll explore how to test code effectively using Python.

### Starting with a Simple Function Test

First, let's consider a basic function and test it:

```python
def my_function(x):
    return x + x/2

def test_my_function():
    assert my_function(10) == 15  # You can change the value to see different outcomes.

if __name__ == "__main__":
    test_my_function()
```

This is a straightforward approach but has limitations, especially for larger projects:

- The code and its tests are in the same file.
- Managing tests becomes cumbersome for multi-file projects.

### Separating Code and Tests

For better organization, we can split the code and its tests into separate files:

- `functions.py` contains the actual function.
- `test_functions.py` includes tests for the function.

Example:

```python
# functions.py
def my_function(x):
    """It is a weird little computation..."""
    return x + x/2

# test_functions.py
from functions import my_function

def test_my_function():
    assert my_function(10) == 15
```

Running these tests can be done using `python test_my_function.py` or by running the code file from your IDE. However, when your software project grows you will likely get to many different files with tests so that running all those tests manually is not a good option. The proper way to run all tests is by using the library `pytest`!

### Using pytest for Testing

`pytest` simplifies the testing process, especially for projects with multiple test files. It automatically detects files and functions that match the `test_*` pattern. This is why you should keep your tests in files that start with `test_` and also have the individual function names starte with `test_`. To run all your tests function in a folder (and all subfolders) you can simply run:
```bash
pytest
```
from the project's root directory.

## Building a Python Library with Tests

Now let's exercise some coding and create a simple blackjack game for which we can then write proper tests.

### Developing the Game
Blackjack is a fairly simple card game.


We will keep the code design simple for now and start with two main functions:

1. `count_cards(cards)`
2. `play_game(names)`

Let's first create a local blackjack.py file like this:

```python
# blackjack.py
def count_cards(cards):
"""Counts card values in blackjack."""
# Implementation details...

def play_game(names):
"""Game logic for blackjack."""
# Placeholder for game logic
```

A first version of `count_cards()` could look like this:

```python
# Careful: the following code contains one semantic error

def count_cards(cards):
    """Calculates the total value of the given cards in a blackjack game.

    Face cards (J, Q, K) count as 10, numbered cards count as their value,
    and Aces count as 11 or 1, adjusting to avoid going over 21.

    Args:
        cards (list of str): A list of card values, e.g., ['A', '7', 'K'].
	"""
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    total = 0
    aces = 0
    for card in cards:
        if card not in card_values:
            raise ValueError(f"Invalid card: {card}")

        # Add card value to total
        total += card_values[card]
        if card == 'A':
            aces += 1

    # Adjust for Aces if total is over 21
    while total >= 21 and aces:
        total -= 10
        aces -= 1

    return total

def play_game(names):
    """Game logic for blackjack."""
    # Placeholder for game logic
```

### Writing Tests for the Game
Now we want to make sure that this code runs as intended, now and in the future. To achieve this we will write some meaningful test functions ensuring our code is robust and behaves as expected.
The tests are written in a separate file, `test_blackjack.py`. For now we can just have this file in the same folder as `blackjack.py`. Later, for bigger projects code and test files are usually kept in different folders. 

```python
# test_blackjack.py
from blackjack import count_cards

def test_count_cards():
    # Multiple assertions to test different scenarios.
```

Running these tests with `pytest` will help identify any issues in the game's logic.

### Improving Test Structure

- It's beneficial to break down tests into smaller, more focused functions.
- This allows for more precise testing and easier identification of issues.
- It is best to define multiple smaller test function rather than one huge test function, because if one test fails it is much easier to identify where the issue originates.

Example:

```python
def test_count_cards_no_aces():
    assert count_cards(['2', '3', '4']) == 9

def test_count_cards_with_aces():
    assert count_cards(['A', '3', '4']) == 18
    assert count_cards(["A", "A"]) == 12
    assert count_cards(["Q", "A"]) == 21
    assert count_cards(["5", "5", "A"]) == 21

def test_more_than_21():
    assert count_cards(["5", "10", "K", "7"]) > 21
```
If you now run `pytest` you should see that not all tests pass for the `count_cards()` function given above.

What is wrong with the code? Please find the bug and fix it! Then, the tests should all pass.

### Using Decorators for Efficient Testing

In the test functions example above we have already implemented one important best practice for unit tests. Instead of simply writing all asserts into one function, it was divided into several different functions with different things to test. This later helps to see where things go wrong (if they go wrong).

One problem that remains, though, is that whenever one `assert` fails, the following lines of code in the same function will not be executed. Replace the first line in the second function by `assert count_cards(['A', '3', '4']) == 999` and then run `pytest` to see what I mean.

We could write each `assert` into a seperate function, but that is too complicated. A much better solution comes with a special pytest decotrator: `pytest.mark.parametrize`. This allows for testing multiple scenarios with a single test function.

Example:

```python
import pytest

@pytest.mark.parametrize(
    "cards, score", 
    [(['A', '3', '4'], 18),
     (['A', 'A', '9'], 21), ...]
)
def test_count_cards_with_aces(cards, score):
    assert count_cards(cards) == score
```
By the way: For the `count_cards()` function written above the input could also be `"A34"` instead of `['A', '3', '4']`. That's Python. (do you understand why this works?)

### Some Things Better Fail
With pytest, we cannot only test things that work as intended, for example using assert as above. We can also test if things fail where they are supposed to fail. This can be done with a `pytest.raises` contstruction.

Here is an example:
```python
def test_unknown_cards():
    with pytest.raises(ValueError) as error:
        count_cards(["X"])
    assert "Invalid card: X" in str(error.value)
```
This will test if the function correctly raises an ValueError and if the expected message is returned. Some things *should* fail, and then it is good to test those cases as well.

