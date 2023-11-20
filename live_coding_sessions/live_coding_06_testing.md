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

Running these tests can be done using `python test_my_function.py`. However, for multiple test files, a more robust solution like `pytest` is recommended.

### Using pytest for Testing

- `pytest` simplifies the testing process, especially for projects with multiple test files.
- It automatically detects files and functions that match the `test_*` pattern.
- To run tests, execute `pytest` in the project's root directory.

## Building a Python Library with Tests

Let's create a simple blackjack game and write tests for it.

### Developing the Game

We start with two main functions:

1. `count_cards(cards)`
2. `play_game(names)`

```python
# blackjack.py
def count_cards(cards):
    """Counts card values in blackjack."""
    # Implementation details...

def play_game(names):
    """Game logic for blackjack."""
    # Placeholder for game logic
```

### Writing Tests for the Game

Tests are written in a separate file, ensuring our code is robust and behaves as expected.

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

### Using Decorators for Efficient Testing

Decorators in Python can be used to streamline tests, particularly with `pytest.mark.parametrize`. This allows for testing multiple scenarios with a single test function.

Example:

```python
import pytest

@pytest.mark.parametrize("cards, score", [("A34", 18), ("AA9", 21), ...])
def test_count_cards_with_aces(cards, score):
    assert count_cards(cards) == score
```

### Expanding the Game: Adding a CardDeck Class

To practice Object-Oriented Programming (OOP) and further modularize our code, we introduce a `CardDeck` class which we will write into a new file, e.g., `main_classes.py`.

A class is useful to handle the cards in our game, because it has internal state (the attributes) that allow "memorize" the current state. In our case this can be used to describe the available number and order of cards in the deck.

```python
import random

class CardDeck:
    def __init__(self, num_copies=4):
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * num_copies
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw_cards(self, num_cards):
        cards = []
        for _ in range(num_cards):
            cards.append(self.cards.pop())
        return cards
```

Once this class is designed or even written, we can start to add tests. This time in a new, separate file that we can name `test_main_classes.py`:

```python
import pytest
from main_classes import CardDeck

def test_card_deck():
	"""First, very simple test."""
    deck = CardDeck()
    assert len(deck.cards) == 52
    deck = CardDeck(num_copies=2)
    assert len(deck.cards) == 26

def test_draw_cards():
    """Test if drawing cards works as intended."""
    deck = CardDeck()
    cards = deck.draw_cards(3)
    assert cards == ["A", "K", "Q"]
    # Test if cards were removed
    assert len(deck.cards) == 49

def test_card_deck_shuffle():
    """Test if shuffling works."""
    deck = CardDeck(num_copies=10)
    before_shuffle = deck.cards.copy()
    deck.shuffle()
    after_shuffle = deck.cards.copy()
    assert before_shuffle != after_shuffle

def test_card_deck_empty():
    """Test, if expected exception is indeed raised."""
    deck = CardDeck()
    deck.draw_cards(52)
    with pytest.raises(IndexError) as exc:
        deck.draw_cards(1)
    assert "pop from empty list" in str(exc.value)
```

We can again run all our tests by simply executing `pytest` in the terminal (from our project folder). 