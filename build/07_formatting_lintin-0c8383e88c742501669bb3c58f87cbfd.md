# Formatting und Linting mit Ruff

**Formatting** und **Linting** lösen unterschiedliche Probleme:

- Ein **Formatter** entscheidet automatisiert, wie Code dargestellt wird.
- Ein **Linter** analysiert Code auf verdächtige Muster, Fehler und ausgewählte Stilregeln.

Für den Kurs verwenden wir für beides **Ruff**. Damit entfällt ein paralleler Tool-Stack aus Black, Flake8, isort und weiteren Einzelwerkzeugen.

## Codebeispiel

Wir verwenden weiterhin ein absichtlich unsauberes Beispiel:

```python
import os
import numpy as np

magic_numbers = [1,2,3,4,5,6,7,8]
magic_dictionary={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",5:"f",7:"g"}

def PowerCompute(a,b,c):
    number1=a**b
    number2=b**a
    max_number=max(number1,number2)
    if max_number<np.max(magic_numbers):
        print(magic_dictionary[max(magic_numbers)])
        return max(magic_numbers)
    else:
        return max_number
```

Hier stecken mehrere unterschiedliche Arten von Problemen:

- Formatierung,
- ungenutzter Import,
- doppelter Dictionary-Key,
- Namenskonventionen,
- möglicherweise unnötige oder unklare Konstruktionen.

Nicht alles davon gehört in dieselbe Kategorie – genau deshalb trennen wir Formatter und Linter gedanklich.

---

## Ruff installieren

Im Projekt:

```bash
uv add --dev ruff
```

Danach verwenden wir Ruff reproduzierbar über:

```bash
uv run ruff ...
```

## Ruff als Linter

Das ganze Projekt prüfen:

```bash
uv run ruff check .
```

Eine einzelne Datei:

```bash
uv run ruff check code_example.py
```

Ruff meldet Fundstellen mit Regelcodes, z. B. `F401` für einen ungenutzten Import.

Zu einer Regel kann direkt Hilfe abgefragt werden:

```bash
uv run ruff rule F401
```

### Automatische Fixes

Viele Befunde kann Ruff sicher automatisiert korrigieren:

```bash
uv run ruff check --fix .
```

Wichtig: Dieser Befehl **verändert Dateien**.

Darum ist ein guter Workflow:

```bash
git status
uv run ruff check --fix .
git diff
```

So bleibt jederzeit sichtbar, was das Tool geändert hat.

> Nicht jeder Lint-Befund ist automatisch fixbar – und das ist gut so. Ein Tool sollte keine semantischen Entscheidungen erfinden, die menschliches Verständnis benötigen.

## Ruff als Formatter

Nur prüfen, ob Dateien korrekt formatiert sind:

```bash
uv run ruff format --check .
```

Anzeigen, was geändert würde:

```bash
uv run ruff format --diff .
```

Tatsächlich formatieren:

```bash
uv run ruff format .
```

Auch hier gilt: Formatierung verändert Dateien. Git macht diese Automatisierung sicher nachvollziehbar.

## Sinnvolle Reihenfolge

Wenn automatische Lint-Fixes verwendet werden, ist dieser Ablauf sinnvoll:

```bash
uv run ruff check --fix .
uv run ruff format .
```

Der Linter kann z. B. Imports ändern; der Formatter formatiert anschließend das endgültige Ergebnis.

Für reine Checks, wie später in CI:

```bash
uv run ruff check .
uv run ruff format --check .
```

CI soll **nicht** ungefragt Dateien reparieren. Sie soll melden, dass der Repository-Stand die Regeln nicht erfüllt.

---

## Was automatisiert der Formatter – und was nicht?

Ein Formatter kann z. B. konsistent entscheiden über:

- Einrückung,
- Leerzeichen,
- Zeilenumbrüche,
- Klammerung,
- viele Aspekte von Quotes und Layout.

Damit werden Diskussionen wie

```python
x=1
```

versus

```python
x = 1
```

praktisch irrelevant: Das Tool entscheidet.

Ein Formatter entscheidet aber nicht, ob ein Variablenname verständlich ist, eine Funktion zu viele Verantwortlichkeiten hat oder ein Algorithmus logisch korrekt ist.

---

## Welche Regeln soll Ruff prüfen?

Ruff bringt bereits ein sinnvolles Standard-Regelset mit. Für den Einstieg ist es besser, **nicht sofort `ALL` zu aktivieren**.

Zusätzliche Regeln können projektweise aktiviert werden. Ein moderates Kursbeispiel:

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
extend-select = [
    "I",   # Import sorting
    "B",   # flake8-bugbear
    "UP",  # modern Python syntax
]
```

Diese Konfiguration gehört direkt in `pyproject.toml`.

Ruff kann alternativ auch über `ruff.toml` oder `.ruff.toml` konfiguriert werden. Da unser Projekt ohnehin eine `pyproject.toml` besitzt, ist eine gemeinsame zentrale Datei im Kurs meistens am einfachsten.

### Warum nicht hunderte Regeln sofort einschalten?

Ein Linter soll Feedback verbessern und nicht in Warnungen ertränken.

Ein guter Weg ist:

1. mit dem Standard-Regelset starten,
2. verstehen, welche Probleme häufig auftreten,
3. gezielt zusätzliche Regelgruppen aktivieren,
4. Konfiguration im Team versionieren.

---

## Regeln gezielt auswählen

Nur eine Regel:

```bash
uv run ruff check . --select F401
```

Eine Gruppe, z. B. Importregeln:

```bash
uv run ruff check . --select I
```

Für die normale Projektarbeit gehört die Auswahl aber in die Konfiguration – nicht jedes Mal in lange CLI-Befehle.

## `# noqa`: Ausnahme statt Ausschalten

Manchmal ist ein Lint-Befund bewusst akzeptiert. Dann kann eine einzelne Regel lokal unterdrückt werden:

```python
import legacy_module  # noqa: F401
```

Das sollte eine **gezielte Ausnahme** sein, kein Reflex auf unbequeme Warnungen.

---

## Ruff im Editor

Ruff lässt sich in moderne Editoren integrieren. Dadurch können Probleme beim Schreiben markiert und Formatierungen auf Wunsch beim Speichern ausgeführt werden.

Für den Kurs bleibt die Kommandozeile trotzdem wichtig:

```bash
uv run ruff check .
uv run ruff format --check .
```

Denn genau dieselben Kommandos können lokal, im Praktikum und in CI verwendet werden.

---

## Automatisierung: lokal vs. CI

### Lokal darf repariert werden

```bash
uv run ruff check --fix .
uv run ruff format .
```

### CI soll prüfen

```bash
uv run ruff check .
uv run ruff format --check .
```

Das ist eine wichtige Trennung:

```text
lokal:  Feedback + automatische Reparatur
CI:     reproduzierbare Prüfung des committed Codes
```

---

## Zusammenhang mit Testing

Testing und Linting beantworten unterschiedliche Fragen:

```text
pytest: Funktioniert der Code entsprechend unserer Erwartungen?
Ruff:   Erfüllt der Code automatisierbare Qualitäts- und Stilregeln?
```

Ein grüner Ruff-Lauf beweist nicht, dass der Code korrekt ist. Ein grüner pytest-Lauf beweist nicht, dass der Code gut strukturiert oder formatiert ist.

Beides ergänzt sich.

---

## Minimaler Qualitäts-Workflow

Vor einem Commit oder Pull Request:

```bash
uv run pytest
uv run ruff check --fix .
uv run ruff format .
uv run pytest
git diff
```

Warum pytest am Ende noch einmal? Automatische Änderungen sollten ebenfalls durch die Tests abgesichert werden.

Für einen reinen Check:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

Diese drei Befehle bilden anschließend den Kern unserer CI-Pipeline.

---

## Cheat Sheet

| Ziel | Befehl |
|---|---|
| Ruff hinzufügen | `uv add --dev ruff` |
| Lint prüfen | `uv run ruff check .` |
| sichere Fixes anwenden | `uv run ruff check --fix .` |
| Regel erklären | `uv run ruff rule F401` |
| Format prüfen | `uv run ruff format --check .` |
| Format-Diff anzeigen | `uv run ruff format --diff .` |
| Dateien formatieren | `uv run ruff format .` |
| eine Regel auswählen | `uv run ruff check . --select F401` |

> **Merke:** Ruff automatisiert viel – aber weder Tests noch Code Review noch verständliches Design werden dadurch überflüssig.
