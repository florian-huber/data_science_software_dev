Hier ist die deutsche Fassung – Struktur, Codeblöcke und Hervorhebungen bleiben erhalten:

# Einführung in Continuous Integration

## 1. Einführung

### Was ist Continuous Integration?

Continuous Integration (CI) bezeichnet die Praxis, kleine, häufige Codeänderungen in einen gemeinsamen Main-Branch zu mergen und diese Änderungen sofort mit automatisierten Builds und Tests zu verifizieren. Anstatt am Ende eines Sprints große, riskante Integrationen vorzunehmen, fördert CI viele sichere, inkrementelle Integrationen – oft mehrmals täglich –, sodass Probleme dort entdeckt werden, wo sie entstanden sind, und solange der Kontext noch frisch ist.

### Zweck und Vorteile

Das primäre Ziel von CI ist schnelles, verwertbares Feedback. Wenn sich ein Defekt einschleicht, informiert uns die Pipeline zügig, damit wir ihn beheben können, bevor er größere Auswirkungen hat. Die Ergebnisse sind greifbar:

* **Frühe Fehlererkennung** senkt die Kosten für Korrekturen und verhindert das Aufstauen von Regressionen.
* **Verbesserte Qualität** durch häufiges Testen und statische Analysen.
* **Automatisierung** von Build-, Lint- und Testschritten spart Entwicklerzeit und reduziert menschliche Fehler.
* **Transparente Zusammenarbeit**: ein gemeinsames Statussignal zu jedem Commit und Pull Request.

> CI konzentriert sich darauf, Änderungen früh zu *verifizieren*; CD (Continuous Delivery/Deployment) baut auf CI auf, um Änderungen *sicher und häufig zu veröffentlichen*.

---

## 2. Ein GitHub-Actions-Workflow einrichten

GitHub Actions ist die integrierte CI/CD-Plattform von GitHub. Ein „Workflow“ beschreibt, **wann** etwas läuft und **was** ausgeführt wird. Für Python-Projekte installiert ein guter Einstiegs-Workflow die Abhängigkeiten, führt Linter aus und startet Tests.

### Eine Workflow-Datei erstellen

Workflows liegen als YAML-Dateien unter `.github/workflows/`. Hier ist ein modernes, minimales Beispiel, das bei Pushes und Pull Requests läuft und eine typische Python-Toolchain zeigt:

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

* `actions/checkout@v4` lädt die Inhalte deines Repos.
* `actions/setup-python@v5` installiert den gewünschten Interpreter und aktiviert `pip`-Caching für schnellere Folgeläufe.
* Im Beispiel kommen **ruff** (schneller Linter/Formatter) und **pytest** zum Einsatz; tausche die Tools bei Bedarf aus (z. B. `flake8`, `black`, `mypy`).

> Tipp: Versioniere Workflow-Dateien wie normalen Code. Behandle die Pipeline als Teil deines Projekts.

---

## 3. Workflow-Auslöser verstehen

Ein Workflow-Auslöser definiert, **wann** deine CI läuft. Auslöser können an die Arbeitsweise deines Teams angepasst werden: bei jedem Push, um Probleme früh zu erkennen, und bei Pull Requests, um Merges mit erforderlichen Checks abzusichern. Für weniger häufige Aufgaben – etwa Abhängigkeits-Updates – kannst du Läufe planen oder manuell auslösen.

Häufige Auslöser, die du sehen wirst:

* **`push`** – läuft, wenn Commits auf bestimmte Branches/Tags gepusht werden.
* **`pull_request`** – läuft beim Erstellen/Aktualisieren eines PR, um Änderungen vor dem Merge zu validieren.
* **`workflow_dispatch`** – manuelles Auslösen in der GitHub-UI (ideal für Wartungsjobs).
* **`schedule`** – läuft nach Cron-Zeitplan (z. B. nachts).
* **`release`/`tag`** – läuft, wenn eine Release veröffentlicht oder ein Tag erstellt wird.

Du kannst Auslöser filtern, um die CI auf relevante Änderungen zu fokussieren (z. B. Tests nur ausführen, wenn sich Python-Dateien ändern, oder nur auf dem Branch `main`).

---

## 4. Events handhaben und konfigurieren

### Event-Typen

* **Push-Event**: Validiert alles, was auf deinen Branches landet; ideal für schnelles Feedback an Contributor.
* **Pull-Request-Event**: Fügt PRs Statuschecks hinzu; kombiniere dies mit Branch-Schutzregeln, um grüne Checks vor dem Merge zu erzwingen.
* **Schedule-Event**: Nützlich für nächtliche Testläufe, Dependency-Scans oder langlaufende Szenarien.
* **Manuell (`workflow_dispatch`)**: Praktisch für Ad-hoc-Aufgaben wie das Neu-Generieren von Doku.

### Event-Auslöser konfigurieren

Mit dem Schlüssel `on` steuerst du, wann der Workflow läuft. Das folgende Beispiel beschränkt CI auf den Branch `main` – sowohl für Push als auch PR – und nur, wenn relevante Pfade geändert wurden:

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

> Pfad-Filter halten CI schnell, indem Läufe für nicht relevante Änderungen übersprungen werden (z. B. nur README-Änderungen).

---

## 5. Die Matrix-Strategie für Tests auf mehreren Umgebungen nutzen

Wenn du mehrere Python-Versionen oder Betriebssysteme unterstützt, führt die **Matrix-Strategie** denselben Job über verschiedene Variationen aus. So bekommst du Sicherheit, dass dein Paket überall funktioniert, wo du es versprichst. Das folgende Beispiel testet alle drei Betriebssysteme jeweils mit Python 3.10 bis 3.13.

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

* `fail-fast: false` sorgt dafür, dass andere Matrix-Jobs weiterlaufen, auch wenn einer fehlschlägt – so erhältst du das vollständige Bild.
* Mit `include`/`exclude` kannst du bestimmte Kombinationen feinsteuern.

---

## 6. Fazit

CI macht Qualität zum Standard, indem jede Änderung automatisch verifiziert wird. Mit GitHub Actions kannst du einfach starten – Linting und Tests bei Push und PR – und dann nach Bedarf Matrizen, Caching, Artefakte und Schutzregeln ergänzen, wenn dein Projekt wächst. Das Ergebnis: schnelleres Feedback, weniger Regressionen und ein Code-Base, die dein Team mit Zuversicht weiterentwickeln kann.
