# Python-Projekte und Repository-Struktur

Dieses Kapitel zeigt, wie aus einzelnen Python-Dateien ein **sauber strukturiertes Projekt** wird. Wir bleiben dabei nah an den bisherigen Themen `import`, Dependencies und Packages, verwenden aber für das Projektmanagement durchgehend **uv** und `pyproject.toml`.

Ziel ist nicht, möglichst viele Packaging-Details zu lernen. Ziel ist ein Projekt, das auf einem anderen Rechner, in einem Team und später in CI zuverlässig funktioniert.

---

## 1) Wie funktionieren `import`s in Python?

### 1.1 Module und Packages

Ein **Modul** ist zunächst einfach eine Python-Datei:

```text
statistics.py
```

und kann – wenn es auf dem Python-Suchpfad liegt – z. B. mit `import statistics` importiert werden.

Ein **Package** ist ein Verzeichnis mit Python-Modulen. Für den Einstieg verwenden wir reguläre Packages mit `__init__.py`:

```text
my_project/
├── __init__.py
├── analysis.py
└── io.py
```

Dann sind beispielsweise Imports wie diese möglich:

```python
from my_project.analysis import calculate_score
```

> **Merke:** Ob ein Import funktioniert, hängt nicht nur vom Dateinamen ab, sondern auch davon, **welches Projekt bzw. welche Umgebung Python gerade kennt**.

### 1.2 Absolute und relative Imports

Innerhalb eines Packages sind beide Formen möglich:

```python
from my_project.io import load_data   # absolut
from .io import load_data             # relativ innerhalb des Packages
```

Für Einsteiger:innen sind absolute Imports oft leichter nachzuvollziehen, weil sofort sichtbar ist, aus welchem Package etwas stammt.

---

## 2) Warum überhaupt eine Projektstruktur?

Ein einzelnes Notebook oder Skript kann völlig ausreichend sein. Sobald ein Projekt wächst, entstehen aber schnell Fragen:

- Wo liegt der eigentliche Quellcode?
- Wo liegen Tests?
- Welche Abhängigkeiten braucht das Projekt?
- Welche Python-Version ist vorgesehen?
- Welche Dateien gehören ins Repository – und welche nicht?
- Wie startet jemand anderes das Projekt reproduzierbar?

Eine konsistente Struktur beantwortet diese Fragen ohne zusätzliche Erklärung.

## 3) Ein modernes Minimalprojekt mit uv

Ein neues Projekt kann direkt mit uv angelegt werden:

```bash
uv init my-project
cd my-project
```

Aktuelle uv-Versionen erzeugen für reguläre Projekte standardmäßig eine Paketstruktur mit `src/` und einer `pyproject.toml`.

Eine typische Struktur sieht dann so aus:

```text
my-project/
├── .git/
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── src/
    └── my_project/
        └── __init__.py
```

Sobald das Projekt zum ersten Mal synchronisiert oder ausgeführt wird, kommen typischerweise hinzu:

```text
.venv/
uv.lock
```

Für ein Projekt mit Tests sieht unsere Zielstruktur ungefähr so aus:

```text
my-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── analysis.py
│       └── io.py
└── tests/
    ├── test_analysis.py
    └── test_io.py
```

Die Ordner `.venv/`, `.pytest_cache/`, `.ruff_cache/`, `dist/` und `build/` gehören normalerweise **nicht** ins Repository.

---

## 4) Warum `src/`?

Die `src`-Struktur wirkt zunächst wie ein zusätzlicher Ordner ohne Nutzen. Sie hilft aber dabei, einen wichtigen Fehler zu vermeiden: Code soll nicht nur deshalb importierbar sein, weil Python zufällig im Repository-Root gestartet wurde.

Mit `src/` testen wir realistischer, ob unser Projekt tatsächlich korrekt installiert und importiert werden kann.

```text
src/my_project/...   -> eigentlicher Anwendungscode
tests/...            -> Tests
```

Das ist besonders wichtig, sobald Tests und CI ins Spiel kommen.

---

## 5) `pyproject.toml`: Zentrale Projektdatei

Die `pyproject.toml` ist die zentrale Konfigurationsdatei moderner Python-Projekte. Sie enthält Projektmetadaten und Abhängigkeiten und kann zusätzlich Konfigurationen für Tools wie Ruff oder pytest aufnehmen.

Ein bewusst kleines Beispiel:

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "Example project for the course"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "numpy",
    "pandas",
]

[dependency-groups]
dev = [
    "pytest",
    "ruff",
]
```

Die genaue Datei, die `uv init` erzeugt, kann je nach uv-Version etwas anders aussehen. Wichtig sind für uns zunächst:

- `[project]`: Name, Python-Version und Laufzeitabhängigkeiten,
- `[dependency-groups]`: Entwicklungswerkzeuge wie pytest und Ruff,
- optional später `[tool.ruff]` oder andere Tool-Konfigurationen.

## 6) Dependencies mit uv verwalten

Laufzeitabhängigkeit hinzufügen:

```bash
uv add pandas
```

Entwicklungsabhängigkeit hinzufügen:

```bash
uv add --dev pytest
uv add --dev ruff
```

Entfernen:

```bash
uv remove pandas
```

uv aktualisiert dabei `pyproject.toml`, löst passende Versionen auf und führt das Projekt-Lockfile `uv.lock`.

### `uv.lock` gehört ins Repository

Die `pyproject.toml` beschreibt, **welche Versionen erlaubt sind**. `uv.lock` hält den tatsächlich aufgelösten, reproduzierbaren Stand fest.

Für unsere Kursprojekte gilt deshalb:

```text
pyproject.toml  -> committen
uv.lock         -> committen
.venv/          -> NICHT committen
```

---

## 7) Projekt synchronisieren und ausführen

```bash
uv sync
```

legt bzw. aktualisiert die Projektumgebung unter `.venv/` und installiert die in `uv.lock` festgehaltenen Abhängigkeiten.

Befehle innerhalb der Projektumgebung führen wir bevorzugt über `uv run` aus:

```bash
uv run python --version
uv run python -m my_project
uv run pytest
uv run ruff check .
```

Dadurch müssen Studierende die virtuelle Umgebung für normale Kursarbeit nicht ständig manuell aktivieren.

---

## 8) Eigene CLI-Kommandos

Für Anwendungen kann ein Kommando in `pyproject.toml` definiert werden:

```toml
[project.scripts]
my-project = "my_project:main"
```

Danach kann es im Projekt ausgeführt werden mit:

```bash
uv run my-project
```

Das ist sauberer und reproduzierbarer als sich darauf zu verlassen, dass ein bestimmtes Skript aus einem bestimmten Arbeitsverzeichnis gestartet wird.

---

## 9) Bauen und Installieren

Wenn das Projekt als Package konfiguriert ist, kann uv Distributionen bauen:

```bash
uv build
```

Dadurch entstehen typischerweise Wheel und Source Distribution unter `dist/`.

Für den Kurs ist das zunächst weniger wichtig als das lokale Entwickeln, Testen und Ausführen. Es zeigt aber, warum eine saubere Package-Struktur mehr ist als reine Ordnerkosmetik.

---

## 10) `.gitignore`

Ein sinnvoller Ausschnitt:

```gitignore
# Environment / caches
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/

# Build artifacts
dist/
build/
*.egg-info/

# Editors / OS
.DS_Store
.vscode/
.idea/
```

Ob Editor-Konfigurationen wie `.vscode/` ignoriert oder bewusst geteilt werden, kann ein Team gemeinsam entscheiden.

---

## 11) Typischer Start eines Kursprojekts

```bash
uv init my-project
cd my-project

uv add numpy pandas
uv add --dev pytest ruff
uv sync

uv run pytest
uv run ruff check .
```

Danach wird das Projekt normal mit Git versioniert und über GitHub geteilt.

## 12) Häufige Stolpersteine

### `ModuleNotFoundError`

Prüfe zuerst:

```bash
pwd
uv run python -c "import my_project; print(my_project)"
```

Wenn `uv run` funktioniert, ein direktes `python ...` aber nicht, wird wahrscheinlich nicht die Projektumgebung verwendet.

### Dependency direkt mit `pip` installiert

Wenn eine Bibliothek zum Projekt gehört, sollte sie nicht nur irgendwie in `.venv` landen, sondern als Projektabhängigkeit festgehalten werden:

```bash
uv add package-name
```

### `.venv` committed

Nicht die komplette Umgebung versionieren. Sie kann aus `pyproject.toml` und `uv.lock` reproduziert werden.

---

## Cheat Sheet

| Ziel | Befehl |
|---|---|
| Neues Projekt | `uv init my-project` |
| Abhängigkeit hinzufügen | `uv add pandas` |
| Dev-Abhängigkeit hinzufügen | `uv add --dev pytest` |
| Abhängigkeit entfernen | `uv remove pandas` |
| Umgebung synchronisieren | `uv sync` |
| Kommando im Projekt ausführen | `uv run <command>` |
| Lockfile explizit aktualisieren | `uv lock` |
| Dependency-Baum anzeigen | `uv tree` |
| Distribution bauen | `uv build` |

> **Kursstandard:** `pyproject.toml` + `uv.lock` beschreiben das Projekt; `.venv/` ist nur eine lokal erzeugte Arbeitsumgebung.
