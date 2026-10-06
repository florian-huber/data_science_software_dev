# Why Do We Need Testing?

Testing is an integral part of software development. Even well-written and consistently formatted code is not automatically correct. Tests help us verify that code meets its requirements and keeps doing so after later changes.

## The Need for Testing

### Different kinds of errors

In programming, we encounter different types of errors:

- **Syntax errors:** the code is grammatically invalid and cannot be executed.
- **Exceptions / runtime errors:** the code starts but fails in a specific situation, for example division by zero.
- **Semantic errors:** the program runs without crashing but returns an incorrect result.

Semantic errors are particularly dangerous because they may remain invisible while a program appears to run normally.

## What Is Testing?

Testing compares observed program behavior with expected behavior.

A tiny test can look like this:

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
```

The basic idea is:

```text
Input -> run code -> compare result with expectation
```

## Manual vs. Automated Testing

- **Manual testing:** a person runs the program, tries inputs, and evaluates the result.
- **Automated testing:** test code performs the same checks reproducibly.

Manual testing remains useful, especially for interaction and user interfaces. Automated tests are much more reliable for checks that should be repeated frequently.

## White-Box vs. Black-Box Testing

- **White-box testing:** tests consider the internal structure or implementation.
- **Black-box testing:** tests focus on input, output, and externally observable behavior.

For many unit tests, a black-box perspective is useful: **What should this function do?** rather than **How is it implemented internally?**

## Testing Levels

Typical levels include:

- **unit tests:** small units such as functions or classes,
- **integration tests:** interaction between components,
- **system tests:** larger complete systems,
- **acceptance tests:** validation against user or business requirements.

In this course, we start with unit tests and build from there.

---

## pytest in a Project

We use **pytest** as our test framework.

Add it as a development dependency:

```bash
uv add --dev pytest
```

Run the tests:

```bash
uv run pytest
```

Compact output:

```bash
uv run pytest -q
```

One file:

```bash
uv run pytest tests/test_math.py
```

One test:

```bash
uv run pytest tests/test_math.py::test_add
```

## How Does pytest Discover Tests?

Tests typically live in a dedicated `tests/` directory:

```text
my-project/
├── src/
│   └── my_project/
│       └── math_utils.py
└── tests/
    └── test_math_utils.py
```

pytest discovers files and functions with standard test names, for example:

```python
def test_add():
    ...
```

## A Good Unit Test

A useful mental model is **Arrange – Act – Assert**:

```python
def test_average():
    # Arrange
    values = [2, 4, 6]

    # Act
    result = sum(values) / len(values)

    # Assert
    assert result == 4
```

Not every test needs these comments, but the structure should be clear.

### Properties of good tests

Good tests should ideally be:

- **small** – focused on one clear behavior,
- **understandable** – the expected behavior is visible,
- **reproducible** – same code + same input -> same result,
- **independent** – one test should not depend on another running first,
- **fast enough** to run frequently.

## Test More Than the Happy Path

For a function, consider more than ordinary input:

```text
normal case
boundary case
empty input
invalid input
```

Example:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
```

The failure case is part of the specification too:

```python
import pytest


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

## Tests and Bugs

When a bug is found, a strong workflow is often:

1. write a test that reproduces the bug,
2. verify that the test fails,
3. fix the code,
4. run the full test suite again.

This does not only repair the bug; it also protects against a future regression.

## Tests Are Not a Mathematical Guarantee

A green test run means:

> All **written** tests passed.

It does not mean:

> The program is guaranteed to be bug-free.

The quality of a test suite depends on whether important requirements, edge cases, and failure modes are covered meaningfully.

## Conclusion

Testing makes expected behavior explicit and repeatedly verifiable. This is why it comes **before** formatting/linting and CI in our workflow: first we define what the code should do, then we automate additional quality checks, and finally CI runs all checks for every change.
