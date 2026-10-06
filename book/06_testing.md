# Warum brauchen wir Testing?

Testen ist ein integraler Bestandteil der Softwareentwicklung. Selbst gut geschriebener und sauber formatierter Code ist nicht automatisch korrekt. Tests helfen uns zu prüfen, ob Code die festgelegten Anforderungen erfüllt – und ob er dies nach späteren Änderungen immer noch tut.

## Die Notwendigkeit des Testens

### Verschiedene Fehlertypen

In der Programmierung begegnen uns unterschiedliche Arten von Fehlern:

- **Syntaxfehler:** Der Code ist grammatikalisch ungültig und kann nicht ausgeführt werden.
- **Exceptions / Laufzeitfehler:** Der Code startet, scheitert aber in einer bestimmten Situation, z. B. bei einer Division durch Null.
- **Semantische Fehler:** Der Code läuft ohne Absturz, liefert aber ein falsches Ergebnis.

Gerade semantische Fehler sind gefährlich, weil sie nicht automatisch sichtbar werden. Ein Programm kann scheinbar problemlos laufen und trotzdem falsche Resultate produzieren.

## Was ist Testen?

Beim Testen vergleichen wir das beobachtete Verhalten eines Programms mit dem erwarteten Verhalten.

Ein sehr kleiner Test kann so aussehen:

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
```

Die Idee ist einfach:

```text
Input -> Code ausführen -> Ergebnis mit Erwartung vergleichen
```

## Manuelles vs. automatisiertes Testen

- **Manuelles Testen:** Eine Person führt das Programm aus, probiert Eingaben aus und beurteilt das Ergebnis.
- **Automatisiertes Testen:** Testcode führt dieselben Prüfungen reproduzierbar aus.

Manuelles Testen bleibt wichtig, besonders für Interaktion und Benutzeroberflächen. Für häufig wiederholte Prüfungen ist automatisiertes Testen aber wesentlich zuverlässiger.

## White-Box- vs. Black-Box-Testing

- **White-Box-Testing:** Tests berücksichtigen die interne Struktur oder Implementierung.
- **Black-Box-Testing:** Tests betrachten vor allem Ein- und Ausgaben bzw. das beobachtbare Verhalten.

Für viele Unit-Tests ist eine Black-Box-Perspektive hilfreich: **Was soll diese Funktion leisten?** und nicht **Wie genau ist sie intern implementiert?**

## Testebenen

Typische Ebenen sind:

- **Unit Tests:** kleine Einheiten wie Funktionen oder Klassen,
- **Integrationstests:** Zusammenspiel mehrerer Komponenten,
- **Systemtests:** größeres Gesamtsystem,
- **Akzeptanztests:** Prüfung aus Sicht der Anforderungen bzw. Nutzer:innen.

In diesem Kurs beginnen wir mit Unit Tests und bauen darauf auf.

---

## pytest im Projekt

Wir verwenden **pytest** als Testframework.

Als Entwicklungsabhängigkeit hinzufügen:

```bash
uv add --dev pytest
```

Tests ausführen:

```bash
uv run pytest
```

Kurze Ausgabe:

```bash
uv run pytest -q
```

Eine einzelne Datei:

```bash
uv run pytest tests/test_math.py
```

Einen einzelnen Test:

```bash
uv run pytest tests/test_math.py::test_add
```

## Wie findet pytest Tests?

Typischerweise liegen Tests in einem eigenen `tests/`-Ordner:

```text
my-project/
├── src/
│   └── my_project/
│       └── math_utils.py
└── tests/
    └── test_math_utils.py
```

pytest erkennt standardmäßig Dateien und Funktionen mit passenden Testnamen, z. B.:

```python
def test_add():
    ...
```

## Ein guter Unit Test

Ein hilfreiches Denkmuster ist **Arrange – Act – Assert**:

```python
def test_average():
    # Arrange
    values = [2, 4, 6]

    # Act
    result = sum(values) / len(values)

    # Assert
    assert result == 4
```

Nicht jeder Test muss diese Kommentare enthalten. Die Struktur sollte aber erkennbar sein.

### Eigenschaften guter Tests

Gute Tests sind möglichst:

- **klein** – sie prüfen einen klaren Sachverhalt,
- **verständlich** – der erwartete Fall ist erkennbar,
- **reproduzierbar** – gleicher Code + gleiche Eingabe -> gleiches Ergebnis,
- **unabhängig** – ein Test sollte nicht davon abhängen, dass ein anderer vorher lief,
- **schnell genug**, dass man sie häufig ausführen möchte.

## Nicht nur den Happy Path testen

Für eine Funktion sollten wir nicht nur normale Eingaben betrachten:

```text
normaler Fall
Grenzfall
leere Eingabe
ungültige Eingabe
```

Beispiel:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
```

Der Fehlerfall gehört ebenfalls zur Spezifikation:

```python
import pytest


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

## Tests und Bugs

Wenn ein Bug gefunden wurde, ist ein guter Workflow oft:

1. einen Test schreiben, der den Bug reproduziert,
2. prüfen, dass der Test wirklich fehlschlägt,
3. den Code korrigieren,
4. alle Tests erneut ausführen.

Damit bleibt der Bug nicht nur repariert – wir schützen den Code gleichzeitig vor einer späteren Regression.

## Tests sind keine mathematische Garantie

Ein grüner Testlauf bedeutet:

> Alle **geschriebenen** Tests sind erfolgreich.

Er bedeutet nicht:

> Das Programm ist garantiert fehlerfrei.

Die Qualität einer Test-Suite hängt davon ab, ob die wichtigen Anforderungen, Randfälle und Fehlerfälle sinnvoll abgedeckt sind.

## Fazit

Testing macht Verhalten explizit und wiederholbar überprüfbar. Genau deshalb kommt es in unserem Workflow **vor** Formatting/Linting und CI: Zuerst definieren wir, was der Code tun soll. Danach automatisieren wir zusätzliche Qualitätschecks und lassen schließlich alle Checks in der CI laufen.
