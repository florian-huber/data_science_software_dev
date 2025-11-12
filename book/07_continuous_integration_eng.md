# Introduction to Continuous Integration

## 1. Introduction

### What is Continuous Integration?

Continuous Integration (CI) is the practice of merging small, frequent code changes into a shared main branch and immediately verifying those changes using automated builds and tests. Instead of large, risky integrations at the end of a sprint, CI encourages many safe, incremental integrations—often multiple times per day—so issues are discovered where they started and while the context is still fresh.

### Purpose and Benefits

The primary goal of CI is fast, actionable feedback. When a defect slips in, the pipeline tells us quickly, so we can fix it before it spreads. The outcomes are tangible:

* **Early bug detection** lowers the cost of fixes and prevents regressions from piling up.
* **Improved quality** through frequent testing and static analysis.
* **Automation** of build, lint, and test steps saves developer time and reduces human error.
* **Transparent collaboration**: a shared status signal on every commit and pull request.

> CI focuses on *verifying* changes early; CD (Continuous Delivery/Deployment) builds on CI to *release* changes safely and frequently.

---

## 2. Setting up a GitHub Actions Workflow

GitHub Actions is GitHub’s built-in CI/CD platform. A "workflow" describes **when** to run and **what** to run. For Python projects, a good starter workflow installs dependencies, runs linters, and executes tests.

### Creating a Workflow File

Workflows live in `.github/workflows/` as YAML files. Here’s a modern minimal example that runs on push and pull requests and shows a typical Python toolchain:

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ruff pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Lint with ruff
        run: |
          ruff check .
          ruff format --check .

      - name: Test with pytest
        run: pytest -q
```

* `actions/checkout@v4` retrieves your repository contents.
* `actions/setup-python@v5` installs the requested interpreter and enables `pip` caching to speed up repeat runs.
* The example uses **ruff** (fast linter/formatter) and **pytest**; swap tools as needed (e.g., `flake8`, `black`, `mypy`).

> Tip: Keep workflow files in version control like any other code. Treat the pipeline as part of your project.

---

## 3. Understanding Workflow Triggers

A workflow trigger defines **when** your CI should run. Triggers can follow your team’s habits: run on every push to catch issues early, and on pull requests to gate merges with required checks. For less frequent tasks—like dependency updates—you can schedule runs or trigger them manually.

Common triggers you’ll see:

* **`push`** – run when commits are pushed to specific branches/tags.
* **`pull_request`** – run on PR creation/update to validate changes before merging.
* **`workflow_dispatch`** – run manually from the GitHub UI (great for maintenance jobs).
* **`schedule`** – run on a cron schedule (e.g., nightly).
* **`release`/`tag`** – run when a release is published or a tag is created.

You can filter triggers to focus CI on the changes that matter (e.g., only run tests when Python files change, or only on the `main` branch).

---

## 4. Handling and Setting Events

### Event Types

* **Push event**: Validates everything that lands on your branches; great for quick feedback to contributors.
* **Pull request event**: Adds status checks to PRs; pair with branch protection to require green checks before merging.
* **Schedule event**: Useful for nightly test runs, dependency scans, or long-running scenarios.
* **Manual (`workflow_dispatch`)**: Handy for ad hoc tasks like regenerating docs.

### Configuring Event Triggers

Use the `on` key to tailor when the workflow runs. The following example limits CI to the `main` branch for both push and PR, and only when relevant paths change:

```yaml
on:
  push:
    branches: [ main ]
    paths:
      - '**.py'
      - 'pyproject.toml'
      - '.github/workflows/python-ci.yml'
  pull_request:
    branches: [ main ]
    paths:
      - '**.py'
      - 'pyproject.toml'
```

> Path filters keep CI fast by skipping runs for unrelated changes (e.g., README-only edits).

---

## 5. Using the Matrix Strategy for Testing Multiple Environments

When you support multiple Python versions or OSes, the **matrix strategy** runs the same job across variations, giving you confidence that your package works everywhere you claim. The following example will test all three operating systems and each with Python 3.10 to 3.13.

```yaml
jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ["3.10", "3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'
      - run: |
          python -m pip install --upgrade pip
          pip install ruff pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - run: ruff check .
      - run: pytest -q
```

* `fail-fast: false` lets other matrix jobs keep running even if one fails, so you see the full picture.
* Add `include`/`exclude` to fine-tune specific combinations.

---

## 6. Conclusion

CI makes quality the default by verifying every change automatically. With GitHub Actions, you can start simple—lint and test on push and PR—and then layer in matrices, caching, artifacts, and protection rules as your project grows. The result is faster feedback, fewer regressions, and a codebase your team can change confidently.
