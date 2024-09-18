## Code Testing (2)

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

Pytest is an incredibly versatile and powerful tool for writing and managing tests in Python. Understanding fixtures, parameterization, temporary path utilities, and monkeypatching can significantly enhance the testing process, allowing for more robust and reliable code. 

