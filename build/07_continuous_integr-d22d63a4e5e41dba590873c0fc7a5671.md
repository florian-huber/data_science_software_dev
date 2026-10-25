# Einführung in Continuous Integration

## 1. Einführung

### Was ist Continuous Integration?

Continuous Integration (CI) bezeichnet die Praxis, kleine, häufige Codeänderungen in einen gemeinsamen Hauptbranch zu integrieren und diese Änderungen automatisch zu verifizieren.

Für unseren Kurs ist der wichtigste Gedanke sehr konkret:

> Die Checks, die lokal wichtig sind, sollen bei Pushes und Pull Requests **automatisch und reproduzierbar** erneut laufen.

Wir haben diese Checks bereits kennengelernt:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

CI erfindet also zunächst keine neue Qualitätslogik. Sie automatisiert unseren bestehenden Workflow.

### Zweck und Vorteile

Das primäre Ziel von CI ist schnelles, verwertbares Feedback:

- **Frühe Fehlererkennung** verhindert, dass Regressionen lange unbemerkt bleiben.
- **Automatische Tests** prüfen erwartetes Verhalten.
- **Ruff-Checks** prüfen automatisierbare Codequalität und Formatierung.
- **Reproduzierbarkeit** zeigt, dass das Projekt nicht nur in einer einzelnen lokalen Umgebung funktioniert.
- **Transparenz im Pull Request** gibt dem Team ein gemeinsames Statussignal.

> CI ersetzt kein Code Review. Ein grüner Workflow bedeutet nur: **Die automatisierten Checks sind erfolgreich.**

---

## 2. GitHub Actions

GitHub Actions ist die integrierte Automatisierungsplattform von GitHub. Workflows liegen im Repository unter:

```text
.github/workflows/
```

Zum Beispiel:

```text
.github/workflows/ci.yml
```

Ein Workflow definiert:

1. **Wann** soll er laufen?
2. **Auf welchem Runner**?
3. **Welche Schritte** werden ausgeführt?

## 3. Minimaler Kurs-Workflow mit uv

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

Dieser Workflow entspricht absichtlich fast genau dem lokalen Workflow.

### Warum `--locked`?

`uv.lock` liegt im Repository. Mit `--locked` verlangen wir, dass CI genau zu diesem Lockfile passt und es nicht still aktualisiert.

Wenn `pyproject.toml` geändert wurde, aber `uv.lock` nicht dazu passt, soll CI fehlschlagen. Das ist hilfreiches Feedback.

---

## 4. Die Schritte verstehen

### Repository auschecken

```yaml
- uses: actions/checkout@v7
```

Der Runner erhält dadurch den Code des Repositories.

### uv installieren

```yaml
- uses: astral-sh/setup-uv@v10
```

Die offizielle setup-uv-Action installiert uv und kann den uv-Cache verwenden.

Für besonders sicherheitskritische Produktions-Repositories werden Actions häufig auf einen konkreten Commit-SHA gepinnt. Für den Kurs ist die Major-Version deutlich lesbarer; wichtig ist, zu verstehen, dass Actions ebenfalls externe Dependencies sind.

### Projekt synchronisieren

```bash
uv sync --locked
```

Damit wird die Projektumgebung auf Basis von `pyproject.toml` und `uv.lock` aufgebaut.

### Tests und Ruff

```bash
uv run --locked pytest -q
uv run --locked ruff check .
uv run --locked ruff format --check .
```

CI verändert den Code nicht. Deshalb verwenden wir hier **kein** `ruff check --fix` und **kein** `ruff format` ohne `--check`.

---

## 5. Workflow-Auslöser

Ein einfacher Kursworkflow läuft bei Pushes und Pull Requests:

```yaml
on:
  push:
  pull_request:
```

Häufige weitere Events sind:

- `workflow_dispatch` – manueller Start,
- `schedule` – zeitgesteuerte Ausführung,
- `release` – Reaktion auf Releases.

Für den Einstieg reichen `push` und `pull_request`.

### Nur bestimmte Branches

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

Ob CI nur auf `main` oder auch auf Feature-Branches bei Pushes laufen soll, ist eine Teamentscheidung. Pull Requests gegen `main` sollten in unserem Kurs immer geprüft werden.

---

## 6. Was passiert bei einem Fehler?

Jeder Step liefert einen Exit-Code.

```text
0  -> erfolgreich
!=0 -> Fehler
```

pytest, Ruff und uv nutzen genau dieses Prinzip. Darum können dieselben CLI-Tools lokal und in CI verwendet werden.

Wenn z. B. ein Test fehlschlägt:

```bash
uv run pytest -q
```

endet dieser Step mit Fehlerstatus und der Job wird rot.

## 7. CI im Pull Request

Der Kursworkflow wird damit:

```text
Issue
  -> Branch
  -> Commits
  -> Pull Request
  -> CI
  -> Code Review
  -> Merge
```

CI und Review haben unterschiedliche Rollen:

```text
CI:     Sind die automatisierten Regeln erfüllt?
Review: Ist die Änderung fachlich, verständlich und angemessen?
```

## 8. Branch Protection / Rulesets

GitHub kann so konfiguriert werden, dass ein Pull Request erst gemerged werden darf, wenn bestimmte Checks erfolgreich sind.

Typische Regeln:

- Pull Request erforderlich,
- CI-Check erforderlich,
- Review erforderlich,
- Force Push auf `main` verhindern.

Damit wird aus einer Empfehlung ein technisch unterstützter Teamworkflow.

---

## 9. Matrix-Tests: optionaler nächster Schritt

Wenn ein Projekt mehrere Python-Versionen unterstützen soll, kann derselbe Testjob mehrfach ausgeführt werden:

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

Für normale Kursprojekte ist eine Matrix nicht zwingend notwendig. Sie ist sinnvoll, wenn mehrere Python-Versionen tatsächlich Teil der unterstützten Plattform sind.

---

## 10. Typische Fehler

### Lokal grün, CI rot

Prüfen:

- Wurde `uv.lock` committed?
- Sind alle benötigten Dateien im Repository?
- Verlässt sich Code auf absolute lokale Pfade?
- Fehlen Umgebungsvariablen oder Secrets?
- Wurde lokal wirklich derselbe Befehl ausgeführt?

### CI repariert Code

Vermeiden:

```yaml
run: uv run ruff format .
```

Besser:

```yaml
run: uv run ruff format --check .
```

CI soll den committed Zustand **prüfen**, nicht heimlich umschreiben.

### Tests hängen von Reihenfolge oder lokalen Daten ab

Dann ist das ein Testdesign-Problem. Gute Tests sollten reproduzierbar und möglichst isoliert sein.

---

## 11. Minimaler Workflow zum Merken

Lokal:

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

## Fazit

CI ist kein eigenes Qualitätsuniversum. Sie macht unseren lokalen Entwicklungsworkflow reproduzierbar und automatisch. Genau deshalb haben wir zuerst Testing und Ruff eingeführt und bauen **danach** die Pipeline: Die Pipeline führt bekannte Checks zuverlässig für jede Änderung aus.
