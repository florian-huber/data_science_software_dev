# Virtuelle Python-Umgebungen mit uv

Eine **virtuelle Umgebung** kapselt Python und installierte Pakete für ein bestimmtes Projekt. Dadurch können verschiedene Projekte unterschiedliche Abhängigkeiten verwenden, ohne sich gegenseitig zu beeinflussen.

Für diesen Kurs verwenden wir dafür konsequent **uv**. Wir brauchen damit keinen parallelen Zoo aus `venv`, Conda, Mamba, Poetry und verschiedenen `pip`-Workflows.

---

## Warum brauchen wir virtuelle Umgebungen?

Die zentralen Gründe bleiben dieselben:

- **Isolation:** Projekt A kann andere Paketversionen verwenden als Projekt B.
- **Reproduzierbarkeit:** Ein Team kann denselben Dependency-Stand wiederherstellen.
- **Stabilität:** Projektabhängigkeiten verändern nicht das System-Python.
- **Portabilität:** Lokaler Rechner und CI können aus denselben Projektdateien arbeiten.

> **Faustregel:** Ein Projekt -> eine Projektumgebung.

## Was ist `.venv/`?

In unseren Projekten liegt die virtuelle Umgebung normalerweise direkt im Repository-Ordner:

```text
my-project/
├── .venv/
├── pyproject.toml
├── uv.lock
├── src/
└── tests/
```

`.venv/` enthält installierte Pakete und einen Python-Interpreter bzw. Verweise darauf. Dieser Ordner ist **lokal erzeugt** und wird nicht committed.

```gitignore
.venv/
```

## Zwei sinnvolle uv-Workflows

### 1) Projekt-Workflow: der Standard im Kurs

Wenn bereits eine `pyproject.toml` existiert, ist der normale Weg:

```bash
uv sync
```

Falls `.venv/` noch nicht existiert, wird sie dabei angelegt. Gleichzeitig installiert uv die in `uv.lock` festgehaltenen Projektabhängigkeiten.

Befehle starten wir dann mit:

```bash
uv run python --version
uv run pytest
uv run ruff check .
```

`uv run` stellt sicher, dass der Befehl in der zum Projekt gehörenden Umgebung läuft und synchronisiert das Projekt bei Bedarf.

### 2) Eine reine virtuelle Umgebung mit `uv venv`

Manchmal möchten wir unabhängig von einem vollständigen uv-Projekt nur eine virtuelle Umgebung erzeugen:

```bash
uv venv
```

Standardmäßig entsteht ebenfalls `.venv/`.

Eine bestimmte Python-Version kann angefordert werden:

```bash
uv venv --python 3.13
```

Falls diese Python-Version noch nicht verfügbar ist, kann uv sie verwalten bzw. installieren.

## Muss ich die Umgebung aktivieren?

Nicht unbedingt.

Der Kursworkflow bevorzugt:

```bash
uv run pytest
```

anstatt erst die Umgebung zu aktivieren und danach `pytest` aufzurufen.

Aktivierung ist trotzdem möglich und manchmal für Editor- oder interaktive Workflows praktisch.

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Danach zeigen:

```bash
python --version
```

und

```bash
which python
```

bzw. unter PowerShell:

```powershell
Get-Command python
```

welcher Interpreter verwendet wird.

Deaktivieren:

```bash
deactivate
```

> Für normale Kursbefehle ist Aktivierung optional. `uv run ...` ist meist eindeutiger und plattformübergreifend leichter zu dokumentieren.

---

## Pakete: `uv add` statt zufälliger Installationen

In einem uv-Projekt sollten Projektabhängigkeiten über `uv add` eingetragen werden:

```bash
uv add numpy pandas
```

Entwicklungswerkzeuge:

```bash
uv add --dev pytest ruff
```

Dadurch werden `pyproject.toml` und `uv.lock` aktualisiert.

Ein direktes

```bash
uv pip install some-package
```

kann für Experimente sinnvoll sein, verändert aber nicht automatisch die Projektabhängigkeiten in `pyproject.toml`. Für dauerhafte Projektabhängigkeiten ist daher `uv add` der bessere Kursstandard.

---

## `pyproject.toml` und `uv.lock`

Die beiden Dateien haben unterschiedliche Aufgaben:

```text
pyproject.toml  -> direkte Anforderungen und Projektkonfiguration
uv.lock         -> vollständig aufgelöster Dependency-Stand
```

Beide gehören ins Git-Repository.

`.venv/` dagegen nicht:

```text
.venv/          -> lokale Installation, jederzeit neu erzeugbar
```

## Umgebung reproduzieren

Nach einem frischen Clone:

```bash
git clone <repository-url>
cd <repository>
uv sync
```

Danach können die Projektbefehle direkt laufen:

```bash
uv run pytest
uv run ruff check .
```

Das ist genau derselbe Grundgedanke, den wir später in der CI-Pipeline verwenden.

---

## Python-Versionen mit uv

uv kann auch Python-Versionen verwalten.

Verfügbare Interpreter anzeigen:

```bash
uv python list
```

Eine Python-Version installieren:

```bash
uv python install 3.13
```

In Projekten kann `.python-version` festhalten, welche Version standardmäßig verwendet werden soll.

Wichtig bleibt zusätzlich die Angabe in `pyproject.toml`:

```toml
[project]
requires-python = ">=3.12"
```

`.python-version` ist eine konkrete lokale/default Auswahl; `requires-python` beschreibt, welche Python-Versionen das Projekt unterstützt.

---

## Jupyter / VS Code

Wenn Notebooks Teil des Projekts sind, kann `ipykernel` als Dev-Abhängigkeit hinzugefügt werden:

```bash
uv add --dev ipykernel
```

In VS Code kann anschließend der Python-Interpreter aus `.venv/` als Kernel ausgewählt werden.

Dadurch verwendet das Notebook dieselben Projektabhängigkeiten wie Skripte, Tests und CI.

---

## Best Practices

- **Ein Projekt -> eine `.venv/`.**
- `.venv/` nicht committen.
- `pyproject.toml` und `uv.lock` committen.
- Projektabhängigkeiten mit `uv add` verwalten.
- Nach einem Clone `uv sync` ausführen.
- Projektkommandos bevorzugt mit `uv run ...` starten.
- Nicht gleichzeitig mehrere Environment-Manager im selben Projekt mischen, wenn es keinen konkreten Grund dafür gibt.

---

## Cheat Sheet

| Ziel | Befehl |
|---|---|
| Projektumgebung erstellen/aktualisieren | `uv sync` |
| Nur eine virtuelle Umgebung erstellen | `uv venv` |
| venv mit bestimmtem Python | `uv venv --python 3.13` |
| Befehl in Projektumgebung | `uv run <command>` |
| Dependency hinzufügen | `uv add <package>` |
| Dev-Dependency hinzufügen | `uv add --dev <package>` |
| Python-Versionen anzeigen | `uv python list` |
| Python installieren | `uv python install 3.13` |
| Umgebung aktivieren (Linux/macOS) | `source .venv/bin/activate` |
| Umgebung aktivieren (PowerShell) | `.venv\\Scripts\\Activate.ps1` |
| Aktivierung beenden | `deactivate` |

> **Merke:** Für den Kurs reicht meistens: `uv sync` und danach `uv run ...`.
