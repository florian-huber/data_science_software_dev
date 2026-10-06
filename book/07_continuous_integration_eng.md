# Introduction to Continuous Integration

## 1. Introduction

### What Is Continuous Integration?

Continuous Integration (CI) is the practice of integrating small, frequent code changes into a shared main branch and automatically verifying those changes.

For this course, the central idea is concrete:

> The checks that matter locally should run **automatically and reproducibly** on pushes and pull requests.

We already know the checks:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

CI therefore does not initially invent new quality logic. It automates our existing workflow.

### Purpose and Benefits

The main goal of CI is fast, actionable feedback:

- **Early bug detection** prevents regressions from remaining unnoticed.
- **Automated tests** verify expected behavior.
- **Ruff checks** verify automatable quality and formatting rules.
- **Reproducibility** shows that the project works outside one local machine.
- **Pull-request visibility** provides a shared status signal for the team.

> CI does not replace code review. A green workflow only means that the **automated checks passed**.

---

## 2. GitHub Actions

GitHub Actions is GitHub's built-in automation platform. Workflow files live in:

```text
.github/workflows/
```

For example:

```text
.github/workflows/ci.yml
```

A workflow defines:

1. **When** should it run?
2. **On which runner**?
3. **Which steps** should be executed?

## 3. Minimal Course Workflow with uv

```yaml
name: Python CI

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  quality:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v7

      - name: Install uv
        uses: astral-sh/setup-uv@v10
        with:
          enable-cache: true

      - name: Sync project
        run: uv sync --locked

      - name: Run tests
        run: uv run --locked pytest -q

      - name: Run Ruff linter
        run: uv run --locked ruff check .

      - name: Check formatting
        run: uv run --locked ruff format --check .
```

The workflow intentionally mirrors the local workflow.

### Why `--locked`?

`uv.lock` is committed to the repository. With `--locked`, CI requires the project metadata to match that lockfile instead of silently updating it.

If `pyproject.toml` changes but `uv.lock` is out of date, CI should fail and provide useful feedback.

---

## 4. Understanding the Steps

### Check out the repository

```yaml
- uses: actions/checkout@v7
```

The runner receives the repository contents.

### Install uv

```yaml
- uses: astral-sh/setup-uv@v10
```

The official setup-uv action installs uv and can reuse uv's cache.

Security-sensitive production repositories often pin actions to a concrete commit SHA. For course material, the major-version tag is easier to read; the important idea is that actions are external dependencies too.

### Sync the project

```bash
uv sync --locked
```

This creates the project environment from `pyproject.toml` and `uv.lock`.

### Tests and Ruff

```bash
uv run --locked pytest -q
uv run --locked ruff check .
uv run --locked ruff format --check .
```

CI should not modify the code, so we do **not** use `ruff check --fix` or an in-place `ruff format` command here.

---

## 5. Workflow Triggers

A simple course workflow runs on pushes and pull requests:

```yaml
on:
  push:
  pull_request:
```

Other common events include:

- `workflow_dispatch` – manual execution,
- `schedule` – time-based execution,
- `release` – react to releases.

For the beginning, `push` and `pull_request` are enough.

### Restricting branches

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

Whether CI should run on every feature-branch push is a team decision. Pull requests targeting `main` should always be checked in our course workflow.

---

## 6. What Happens on Failure?

Each step returns an exit code.

```text
0  -> success
!=0 -> failure
```

pytest, Ruff, and uv all follow this convention. This is why the same CLI tools work locally and in CI.

## 7. CI in the Pull-Request Workflow

Our workflow becomes:

```text
Issue
  -> Branch
  -> Commits
  -> Pull Request
  -> CI
  -> Code Review
  -> Merge
```

CI and review have different jobs:

```text
CI:     Do the automated rules pass?
Review: Is the change correct, understandable, and appropriate?
```

## 8. Branch Protection / Rulesets

GitHub can require checks before a pull request may be merged.

Typical rules include:

- pull request required,
- required CI checks,
- review required,
- prevent force pushes to `main`.

This turns a recommended workflow into a technically enforced one.

---

## 9. Matrix Testing: Optional Next Step

If a project supports several Python versions, the same test job can run multiple times:

```yaml
jobs:
  test:
    strategy:
      matrix:
        python-version: ["3.12", "3.13"]
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v7
      - uses: astral-sh/setup-uv@v10
        with:
          python-version: ${{ matrix.python-version }}
      - run: uv sync --locked
      - run: uv run --locked pytest -q
```

A matrix is optional for normal course projects. It is useful when supporting multiple Python versions is an actual project requirement.

---

## 10. Typical Problems

### Green locally, red in CI

Check:

- Was `uv.lock` committed?
- Are all required files in the repository?
- Does code rely on absolute local paths?
- Are environment variables or secrets missing?
- Did you really run the same command locally?

### CI modifies code

Avoid:

```yaml
run: uv run ruff format .
```

Prefer:

```yaml
run: uv run ruff format --check .
```

CI should **verify** the committed state rather than silently rewriting it.

## 11. Minimal Workflow to Remember

Locally:

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

CI:

```text
checkout
-> setup uv
-> uv sync --locked
-> pytest
-> ruff check
-> ruff format --check
```

## Conclusion

CI is not a separate quality universe. It makes the local development workflow reproducible and automatic. This is why testing and Ruff come first, and the pipeline comes **afterwards**: the pipeline reliably executes checks we already understand.
