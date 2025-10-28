## Live Coding - Testing (part 2)

Last time we developed the first pieces of a simple blackjack game.

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


Last time we developed the function `count_cards()`. Here is a simple variant of a `play_game()` function that now uses the CardDeck and the existing function to build a minimal version of a blackjack game.


```python
from main_classes import CardDeck


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
import pytest
from blackjack import count_cards


def test_count_cards():
    assert count_cards(["2", "3", "4"]) == 9

@pytest.mark.parametrize("cards, score", 
                         [(["A", "Q"], 21),
                          (["A", "5", "5"], 21),
                          (["A", "9"], 20),
                          (["A", "A", "7"], 19)
                          ]
                         )
def test_count_cards_with_aces(cards, score):
    assert count_cards(cards) == score

def test_more_than_21():
    assert count_cards(["10", "J", "Q"]) > 21

def test_unknown_cards():
    with pytest.raises(ValueError) as error:
        count_cards(["X"])
    assert "Invalid card: X" in str(error.value)
```



## Instructor-task: 

Create a repository and place those files in respective folders and push.

--> Everyone can then fork this and clone it to have a local copy.





### Trouble with folders

We now place those files in separate folders, which is good practice. So, for instance, a `casino` folder with `blackjack.py` and `main_classes.py` and a seperate `tests` folder.

The structure of our projects is now
project/
│
├── casino/
│   ├── __init__.py
│   ├── blackjack.py
│   ├── main_classes.py
│
├── tests/
│   ├── __init__.py
│   ├── test_blackjack.py
│
└── README.md


Try: `pytest`

This no longer works.
At this point we have to add an empty `__init__.py` file in both the tests and the `casino` folder. This indicates to the Python interpreter that those folders are "modules" from which we can also import. Do do so, we can adjust the imports to `from casino.blackjack import count_cards` in our test file. 

Does this work now?

Not fully, we also have to change the import in the blackjack game to `from casino.main_classes import CardDeck`. Then, the test should work (hopefully).

There is **more trouble coming** though.
Try now to execute the `blackjack.py` file. This will probably give you an error saying `ModuleNotFoundError: No module named 'casino'" error.`. 

There are some workarounds for this, but none of them is really nice (IMHO). So it's better to avoid such execution directly from a .py-file once we build a Python package. But you can still run the code with the following command from the project root folder:
```bash
python -m casino.blackjack
```



### Coding part:
It is now time to also add tests for the `CardDeck` class which I placed in the file `main_classes.py`. So we will start with a new file called `test_main_classes.py`:

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
from casino.blackjack import play_game
from casino.main_classes import CardDeck
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


### Task:
By the way: what happens if all players exceed 21 points? Ever tested this?









## Continuous Integration

Here a pipeline to use:

```yaml
name: Our first Python CI
on:
  push:
    branches: [ "main" ] 

jobs:
  My-first-CI:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: 3.12
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install ruff pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi 
    - name: Linting with Ruff
      run: ruff check .
    - name: Test with pytest
      run: pytest

```

A good tool to check your yaml file is: https://yamlchecker.com/