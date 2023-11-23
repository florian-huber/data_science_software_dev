## Live Coding Introduction to Code Testing (2)

Now to a few more sophisticated options we get from `pytest`, which can be really useful for testing more complex cases or for streamlining and improving the code of tests for larger software projects (e.g., by making them more readable).

## Fixtures

### What is a Fixture?

A fixture is a function that sets up a specific test environment. It can provide a fixed baseline upon which tests can reliably and repeatedly execute. Fixtures are used to initialize test functions, which can include setting up database connections, paths, or any specific system state required for testing.

### Usage and Example

To declare a fixture, use the `@pytest.fixture` decorator. Test functions can then use this fixture by including it as an argument. Pytest handles the setup and teardown of the fixture.

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15
```

## pytest.mark.parametrize

### Purpose

`pytest.mark.parametrize` is used for parameterized testing in Pytest. It allows a test function to be called with different arguments, facilitating the testing of various input scenarios with a single test function.

### Example

```python
import pytest

@pytest.mark.parametrize("test_input,expected", [(3, 9), (5, 25), (10, 100)])
def test_square(test_input, expected):
    assert test_input**2 == expected
```

In this example, `test_square` is run three times with different values of `test_input` and `expected`.

## tmp_path

### Usage

The `tmp_path` fixture provides a temporary file system path where files and directories can be created for testing purposes. These files are unique to the test and are cleaned up after the test finishes.

### Example

```python
def test_create_file(tmp_path):
    temp_dir = tmp_path / "sub"
    temp_dir.mkdir()
    temp_file = temp_dir / "hello.txt"
    temp_file.write_text("hello, world")
    
   
    # Test if the file exists  
    assert temp_file.is_file()  
  
    # Check the file's contents  
    assert temp_file.read_text() == "Hello, pytest!"
```

## Monkeypatch

### What is Monkeypatch? What is Mocking?

Monkeypatching in testing refers to dynamic (or runtime) modifications of a class or module during test execution. Mocking is a broader concept used in unit testing to simulate the behavior of complex, real (non-mock) objects.

### Monkeypatch in Pytest

Pytest's `monkeypatch` fixture allows you to replace and modify objects, functions, dictionaries, and environment variables easily.

### Example: Mimicking a Class

```python
class MyClass:
    def method(self):
        return "original"

def test_myclass_method(monkeypatch):
    def mock_method(self):
        return "mocked"

    monkeypatch.setattr(MyClass, "method", mock_method)

    my_object = MyClass()
    assert my_object.method() == "mocked"
```

### Example: Mimicking User Input

```python
def get_username():
    return input("Enter username: ")

def test_get_username(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "pytest")
    assert get_username() == "pytest"
```

This can also be used to mimick multiple user inputs in a row. For instance:

```python
import pytest

def user_input():
    x = input("say something: ")
    if x.lower() == "hello":
        print("hello")
    y = input("something else?")
    return x, y

def test_user_input(monkeypatch):
    user_input_generator = iter(["Hello", "Bye"])
    monkeypatch.setattr('builtins.input', lambda _: next(user_input_generator))
    user_x, user_y = user_input()
    assert user_x == "Hello"
    assert user_y == "Bye"
```





## Summary

Pytest is an incredibly versatile and powerful tool for writing and managing tests in Python. Understanding fixtures, parameterization, temporary path utilities, and monkeypatching can significantly enhance the testing process, allowing for more robust and reliable code. These features make Pytest an excellent choice for both simple and complex testing scenarios in Python development.









Last time we developed the first pieces of a simple blackjack game.

This included two main functions:

1. `count_cards(cards)`, which we already developed
2. `play_game(names)`, which we develop in this session

```python
def count_cards(cards):
    """Counts the total value of the given cards in a blackjack game."""
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    total = 0
    aces = 0
    for card in cards:
        total += card_values[card]
        if card == 'A':
            aces += 1

    while total >= 21 and aces:
        total -= 10
        aces -= 1

    return total

def play_game(names):
    """Game logic for blackjack."""
    # Placeholder for game logic
```

A simple realization of a the play_game() function could look like this:

```python
def play_game():
    """A game of Blackjack with multiple players."""
    num_players = int(input("Enter the number of players: "))
    players = [{'name': f"Player {i+1}", 'cards': [], 'score': 0} for i in range(num_players)]

    card_deck = CardDeck(num_copies=4)
    card_deck.shuffle()

    # Initial dealing of two cards
    for player in players:
        player['cards'] = card_deck.draw_cards(2)

    # Each player's turn
    for player in players:
        while True:
            print(f"{player['name']}, your cards: {', '.join(player['cards'])}")
            player['score'] = count_cards(player['cards'])
            print(f"You have {player['score']} points.")

            if player['score'] >= 21:
                break

            answer = input("Do you want another card? (y/n): ")
            if answer.lower() == 'n':
                break

            player['cards'] += card_deck.draw_cards(1)

    # Determine winner
    winning_score = max(player['score'] for player in players if player['score'] <= 21)
    winners = [player['name'] for player in players if player['score'] == winning_score]

    # Final scores and winner announcement
    print("\nFinal Scores:")
    for player in players:
        print(f"{player['name']}: {player['score']} points")
    
    if winners:
        print(f"Winner(s): {', '.join(winners)}")
    else:
        print("No winners this round.")

if __name__ == "__main__":
    play_game()
```

There is a lot of room for improvements, but it is enough to illustrate how such a game could work.

Now to the testing. We already implemented tests for the `count_cards()` function last week.

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

To practice Object-Oriented Programming (OOP) and further modularize our code, we introduced a `CardDeck` class which we will write into a new file, e.g., `main_classes.py`.

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

### How to test the `play_game()` function?

This function is a bit more tricky to test, because in a real game there are multiple user inputs. And there is a lot of random events (card shuffling etc.), so that in reality each game looks different.

This is where **mocking** comes into play. In principle we replace objects (or functions/methods) in our code by fake versions which we can better control. For this we here use pytest and its `monkeypatch` module.

One such test could look like:

```python
import pytest
from main_functions import play_game
from main_classes import CardDeck
from io import StringIO

def test_single_player_blackjack(monkeypatch):
    """Simulate a single player getting Blackjack."""
    def mock_user_input():
        # This simulates the user input
        def fake_input(prompt):
            if "number of players" in prompt:
                return "1"
            return "n"
        return fake_input
    
    def mock_draw_cards(self, n):
        # This simulates the drawing of cards.
        return ["A", "10"]

    # Mock single player game
    monkeypatch.setattr('builtins.input', mock_user_input())

    # Mock CardDeck to deal a Blackjack hand
    monkeypatch.setattr(CardDeck, 'draw_cards', mock_draw_cards)

    # Capture output
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)

    play_game()

    assert "Player 1, your cards: A, 10" in output.getvalue()
    assert "You have 21 points." in output.getvalue()
    assert "Winner(s): Player 1" in output.getvalue()
```

