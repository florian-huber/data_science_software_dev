# Code Testing (2)

In this part we’ll level up with a few powerful `pytest` features. These tools help you express intent clearly, avoid duplication, and keep test suites fast and maintainable—especially as projects grow. We’ll look at **fixtures**, **parameterization**, **temporary paths**, and **monkeypatching**. Each solves a common testing problem: *setup/teardown*, *covering many inputs*, *isolating the filesystem*, and *controlling behavior of dependencies*.

## Fixtures

### What is a Fixture?

A **fixture** is a function that prepares state for tests. Think of it as reusable setup: data objects, temporary directories, configuration, connections—anything a test needs to run reliably and repeatedly. Pytest discovers fixtures by name and injects them into tests via function arguments. It also takes care of teardown when needed.

### Usage and Example

Declare a fixture with `@pytest.fixture`. Any test that lists the fixture name as a parameter receives its return value. Pytest handles the lifecycle automatically.

```python
import pytest

@pytest.fixture
def sample_data():
    # Arrange: provide a stable baseline for tests
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    # Act & Assert
    assert sum(sample_data) == 15
```

**Scopes & organization (briefly):** By default, fixtures are **function-scoped** (fresh per test). You can set `scope="class" | "module" | "session"` for reuse across tests. Place broadly used fixtures in `conftest.py` to make them available across a test package—no imports required.

> Tip: Prefer fixtures over manual setup inside tests. Your tests become shorter, clearer, and less fragile.

---

## `pytest.mark.parametrize`

### Purpose

When the same behavior should hold for many inputs, **parameterization** lets you write a single test that runs multiple times with different arguments. This keeps test code DRY and highlights what varies: the data, not the logic.

### Example

```python
import pytest

@pytest.mark.parametrize("test_input,expected", [(3, 9), (5, 25), (10, 100)])
def test_square(test_input, expected):
    assert test_input ** 2 == expected
```

Pytest executes `test_square` three times—once per (input, expected) pair. For readability, you can add `ids=` to name the cases:

```python
@pytest.mark.parametrize(
    "test_input,expected",
    [(3, 9), (5, 25), (10, 100)],
    ids=["3^2", "5^2", "10^2"]
)
def test_square(test_input, expected):
    assert test_input ** 2 == expected
```

> Tip: Use parameterization instead of loops in tests. If a case fails, pytest reports the failing parameter, making triage much easier.

---

## `tmp_path`

### Usage

The built-in `tmp_path` fixture gives you an isolated temporary directory for each test. It’s ideal for testing code that reads/writes files without touching your real workspace. Paths are `pathlib.Path` objects and are automatically cleaned up after the test.

### Example

```python
def test_create_file(tmp_path):
    temp_dir = tmp_path / "sub"
    temp_dir.mkdir()
    temp_file = temp_dir / "hello.txt"
    temp_file.write_text("Hello, pytest!")

    # Test if the file exists
    assert temp_file.is_file()

    # Check the file's contents
    assert temp_file.read_text() == "Hello, pytest!"
```

> Tip: Prefer `tmp_path` over hard-coded paths or working in the repository root. It prevents flaky tests and accidental file pollution.

---

## Monkeypatch

### What are Monkeypatching and Mocking?

**Monkeypatching** means changing objects at runtime (e.g., swapping a function or attribute) for the duration of a test. **Mocking** is the broader practice of replacing real dependencies with controllable stand-ins. In pytest, the `monkeypatch` fixture makes this easy—without extra libraries.

### Monkeypatch in Pytest

You can replace attributes, environment variables, and dictionary items. This is useful when code interacts with the OS, user input, or third-party services.

#### Example: Replacing a class method

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

#### Example: Mimicking user input

```python
def get_username():
    return input("Enter username: ")

def test_get_username(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "pytest")
    assert get_username() == "pytest"
```

You can also simulate multiple inputs in sequence:

```python
def user_input():
    x = input("say something: ")
    if x.lower() == "hello":
        print("hello")
    y = input("something else?")
    return x, y

def test_user_input(monkeypatch):
    user_input_generator = iter(["Hello", "Bye"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_input_generator))
    user_x, user_y = user_input()
    assert user_x == "Hello"
    assert user_y == "Bye"
```

#### Example: Environment variables

```python
import os

def get_api_key():
    return os.environ.get("API_KEY", "")

def test_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "secret-123")
    assert get_api_key() == "secret-123"
```

> Tip: For heavy mocking needs, the `pytest-mock` plugin offers a `mocker` fixture (a wrapper around `unittest.mock`). But for many cases, `monkeypatch` is perfectly sufficient and very readable.

---

## Summary

Pytest’s **fixtures** keep setup tidy and reusable, **parameterization** scales a single test across many inputs, **`tmp_path`** isolates filesystem interactions, and **monkeypatching** lets you control external behavior. Together, these features make tests clearer, faster to write, and more robust—exactly what you need as your project grows.

---