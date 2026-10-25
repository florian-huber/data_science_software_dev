
# Unit Tests in Python

Betrachten wir eine sehr einfache Funktion:

```python
def divide(num_divide, num_divide_by):
    if num_divide_by != 0:
        return num_divide / num_divide_by
```

Auf den ersten Blick sieht die Funktion plausibel aus.

Probieren wir sie aus:

```python
print(divide(10, 5))
print(divide(4, 4))
```

Ergebnis:

```text
2.0
1.0
```

Scheint zu funktionieren.

Wir können diese Überprüfung automatisieren:

```python
def test_divide():
    assert divide(10, 5) == 2
    assert divide(4, 4) == 1
```

Ein `assert` bedeutet:

> Diese Bedingung muss wahr sein.

Falls beispielsweise

```python
divide(10, 5)
```

nicht `2` liefert, schlägt der Test fehl.

---

## Reichen diese Tests?

Unsere beiden Tests zeigen:

```text
10 / 5 → funktioniert
4 / 4  → funktioniert
```

Aber bedeutet das:

> `divide()` funktioniert korrekt?

Noch nicht.

Schauen wir uns den Code genauer an:

```python
def divide(num_divide, num_divide_by):
    if num_divide_by != 0:
        return num_divide / num_divide_by
```

Dort steht eine Bedingung:

```python
if num_divide_by != 0:
```

Wir haben bisher nur Situationen getestet, in denen diese Bedingung wahr ist.

Was passiert bei:

```python
divide(10, 0)
```

Probiert es aus.

Das Ergebnis ist:

```python
None
```

Es erscheint keine Fehlermeldung.

Das Programm tut einfach nichts und liefert implizit `None` zurück.

Das ist besonders unangenehm:

> **Der Fehler wird still verschluckt.**

---

## Black-Box- und White-Box-Testing

Dieses Beispiel zeigt zwei unterschiedliche Möglichkeiten, auf Tests zu kommen.

### Black-Box-Testing

Beim Black-Box-Testing behandeln wir eine Funktion wie eine schwarze Box:

```text
             ┌─────────────┐
Input ──────►│   divide()  │──────► Output
             └─────────────┘
```

Wir interessieren uns zunächst nicht dafür, **wie** die Funktion intern implementiert wurde.

Stattdessen fragen wir:

> Was soll diese Funktion laut Spezifikation tun?

Wenn die Spezifikation lautet:

> `divide(a, b)` dividiert `a` durch `b`.

dann könnten wir beispielsweise aus der Spezifikation folgende Tests ableiten:

```python
assert divide(10, 5) == 2
assert divide(4, 4) == 1
assert divide(0, 5) == 0
```

Die Tests beziehen sich auf das **beobachtbare Verhalten**.

Black-Box-Tests sind deshalb besonders wertvoll, weil sie unabhängig von der konkreten Implementierung sein können.

---

### White-Box-Testing

Beim White-Box-Testing schauen wir zusätzlich in die Implementierung.

Wir sehen dort:

```python
if num_divide_by != 0:
```

Dadurch entsteht sofort eine neue Frage:

> Was passiert eigentlich, wenn `num_divide_by == 0` ist?

Wir schreiben also bewusst einen Test für den anderen Zweig der Bedingung.

Das ist ein typischer White-Box-Gedanke:

> **Welche Teile und Entscheidungen meines Codes habe ich bisher noch nicht ausgeführt?**

Wichtig ist dabei:

Die Idee für den Test kann aus der Implementierung kommen. Der Test sollte anschließend aber möglichst das **gewünschte Verhalten** prüfen und nicht irgendwelche internen Details.

---

## Fehler sollten explizit sein

Unsere erste Implementierung

```python
def divide(num_divide, num_divide_by):
    if num_divide_by != 0:
        return num_divide / num_divide_by
```

hat ein Problem:

```python
divide(10, 0)
```

liefert einfach:

```python
None
```

Das ist schlechter als eine klare Fehlermeldung.

Eine sinnvollere Implementierung wäre:

```python
def divide(num_divide, num_divide_by):
    if num_divide_by == 0:
        raise ValueError("Cannot divide by zero.")

    return num_divide / num_divide_by
```

Jetzt wird ein ungültiger Aufruf explizit:

```python
divide(10, 0)
```

führt zu:

```text
ValueError: Cannot divide by zero.
```

Das ist gewolltes Verhalten.

Eine Exception bedeutet also nicht automatisch:

> „Unser Programm ist kaputt.“

Eine Exception kann Teil der **Spezifikation einer Funktion** sein.

---

## Exceptions testen

Mit `pytest` können wir testen, ob eine erwartete Exception tatsächlich ausgelöst wird.

```python
import pytest


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

Der Test ist erfolgreich, **wenn** `divide(10, 0)` einen `ValueError` auslöst.

Falls kein Fehler auftritt, schlägt der Test fehl.

Wir können sogar die Fehlermeldung prüfen:

```python
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

Damit testen wir nicht nur:

```text
Es tritt irgendein Fehler auf.
```

sondern:

```text
Es tritt der erwartete Fehler auf.
```

---

## Welche Fälle sollten wir testen?

Beim Nachdenken über Tests helfen einige typische Kategorien:

```text
normaler Fall
Grenzfall
leere Eingabe
ungültige Eingabe
```

Diese Kategorien sind keine Checkliste, die für jede Funktion zwangsläufig vollständig abgearbeitet werden muss.

Sie sind vielmehr Fragen, die uns helfen, interessante Testfälle zu finden.

---

### 1. Normaler Fall

Ein typischer Aufruf:

```python
assert divide(10, 5) == 2
```

oder:

```python
assert divide(9, 3) == 3
```

Solche Tests werden häufig auch als **Happy Path** bezeichnet.

Sie sind wichtig – aber meistens nicht ausreichend.

---

### 2. Grenzfall

Grenzfälle liegen an interessanten Grenzen des erlaubten Wertebereichs.

Bei unserer Division können wir beispielsweise fragen:

> Was passiert, wenn der Zähler genau `0` ist?

```python
assert divide(0, 5) == 0
```

`0` ist hier interessant, weil sie die Grenze zwischen positiven und negativen Zahlen bildet.

Auch negative Zahlen können sinnvoll sein:

```python
assert divide(-10, 5) == -2
assert divide(10, -5) == -2
```

Und direkt an der Grenze des **nicht erlaubten Falls** steht:

```python
divide(10, 0)
```

Hier erwarten wir keine Zahl, sondern einen definierten Fehler.

---

### 3. Leere Eingabe

Eine leere Eingabe ist für unsere `divide()`-Funktion eigentlich kein sinnvoller Testfall.

Die Funktion erwartet zwei Zahlen.

Es gibt hier keine Liste, die leer sein könnte.

Das ist eine wichtige Erkenntnis:

> **Nicht jede Testkategorie passt zu jeder Funktion.**

Bei einer Funktion wie

```python
def average(values):
    ...
```

wäre dagegen

```python
average([])
```

ein sehr wichtiger Fall.

Was soll der Mittelwert einer leeren Liste sein?

- `0`?
- `None`?
- `NaN`?
- eine Exception?

Das kann ein Test erst beantworten, wenn wir vorher festgelegt haben, welches Verhalten wir erwarten.

---

### 4. Ungültige Eingaben

Was passiert bei:

```python
divide("10", 5)
```

oder:

```python
divide(10, "5")
```

Unsere Funktion soll mit Zahlen arbeiten.

Wir könnten deshalb in der Spezifikation festlegen:

> Beide Argumente müssen Zahlen sein. Für andere Datentypen wird ein `TypeError` ausgelöst.

Dann können wir genau dieses Verhalten testen:

```python
def test_divide_rejects_strings():
    with pytest.raises(TypeError):
        divide("10", 5)
```

Wenn wir eine eindeutige Fehlermeldung wünschen, können wir die Eingabe explizit prüfen:

```python
def divide(num_divide, num_divide_by):
    if not isinstance(num_divide, (int, float)):
        raise TypeError("Both arguments must be numbers.")

    if not isinstance(num_divide_by, (int, float)):
        raise TypeError("Both arguments must be numbers.")

    if num_divide_by == 0:
        raise ValueError("Cannot divide by zero.")

    return num_divide / num_divide_by
```

Dann können wir auch die Nachricht testen:

```python
def test_divide_rejects_strings():
    with pytest.raises(TypeError, match="must be numbers"):
        divide("10", 5)
```

Jetzt haben wir aus einer ursprünglich sehr einfachen Funktion bereits mehrere Anforderungen abgeleitet:

```text
10 / 5      → 2
0 / 5       → 0
-10 / 5     → -2
10 / 0      → ValueError
"10" / 5    → TypeError
```

Genau hier beginnt systematisches Testing.

---

## Von der Spezifikation zu Testfällen

Bevor wir Tests schreiben, sollten wir deshalb fragen:

> **Was genau soll die Funktion tun?**

Eine kleine Spezifikation könnte beispielsweise lauten:

### `divide(num_divide, num_divide_by)`

- beide Argumente müssen `int` oder `float` sein,
- positive, negative und `0` als Zähler sind erlaubt,
- der Divisor darf nicht `0` sein,
- bei Division durch `0` wird `ValueError` ausgelöst,
- bei ungültigen Datentypen wird `TypeError` ausgelöst.

Erst daraus können wir systematisch Testfälle entwickeln.

| Kategorie | Eingabe | Erwartung |
|---|---|---|
| normal | `divide(10, 5)` | `2` |
| normal | `divide(4, 4)` | `1` |
| Grenzfall | `divide(0, 5)` | `0` |
| negative Werte | `divide(-10, 5)` | `-2` |
| ungültig | `divide(10, 0)` | `ValueError` |
| ungültig | `divide("10", 5)` | `TypeError` |

Tests entstehen also idealerweise nicht dadurch, dass wir zufällig irgendwelche Zahlen ausprobieren.

Sie entstehen aus:

```text
Anforderung
    ↓
interessanter Fall
    ↓
erwartetes Verhalten
    ↓
automatisierter Test
```

---

## pytest im Python-Projekt

Für unsere automatisierten Tests verwenden wir **pytest**.

In einem `uv`-Projekt fügen wir pytest als Entwicklungsabhängigkeit hinzu:

```bash
uv add --dev pytest
```

Dadurch wird `pytest` in `pyproject.toml` eingetragen und das `uv.lock` entsprechend aktualisiert.

Tests starten wir mit:

```bash
uv run pytest
```

Für eine kompaktere Ausgabe:

```bash
uv run pytest -q
```

---

## Projektstruktur

Typischerweise trennen wir Produktionscode und Testcode:

```text
my-project/
├── pyproject.toml
├── uv.lock
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── math_utils.py
└── tests/
    └── test_math_utils.py
```

Unsere Funktion könnte beispielsweise in

```text
src/my_project/math_utils.py
```

liegen:

```python
def divide(num_divide, num_divide_by):
    if not isinstance(num_divide, (int, float)):
        raise TypeError("Both arguments must be numbers.")

    if not isinstance(num_divide_by, (int, float)):
        raise TypeError("Both arguments must be numbers.")

    if num_divide_by == 0:
        raise ValueError("Cannot divide by zero.")

    return num_divide / num_divide_by
```

Die Tests liegen dagegen in:

```text
tests/test_math_utils.py
```

Zum Beispiel:

```python
import pytest

from my_project.math_utils import divide


def test_divide_normal_numbers():
    assert divide(10, 5) == 2
    assert divide(4, 4) == 1


def test_divide_zero_numerator():
    assert divide(0, 5) == 0


def test_divide_negative_number():
    assert divide(-10, 5) == -2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_rejects_string():
    with pytest.raises(TypeError):
        divide("10", 5)
```

---

## Wie findet pytest unsere Tests?

pytest sucht automatisch nach typischen Testnamen.

Testdateien heißen beispielsweise:

```text
test_math_utils.py
```

und Testfunktionen beginnen mit:

```python
def test_...
```

Beispiel:

```python
def test_divide_by_zero():
    ...
```

Damit kann pytest sie automatisch finden und ausführen.

Alle Tests:

```bash
uv run pytest
```

Nur eine Datei:

```bash
uv run pytest tests/test_math_utils.py
```

Nur ein bestimmter Test:

```bash
uv run pytest tests/test_math_utils.py::test_divide_by_zero
```

---

## Arrange – Act – Assert

Eine hilfreiche Struktur für Unit Tests ist:

```text
Arrange
Act
Assert
```

### Arrange

Bereite die Eingaben vor.

### Act

Führe die getestete Funktion aus.

### Assert

Prüfe das Ergebnis.

Beispiel:

```python
def test_divide_normal_numbers():
    # Arrange
    numerator = 10
    denominator = 5

    # Act
    result = divide(numerator, denominator)

    # Assert
    assert result == 2
```

Bei kleinen Tests ist es nicht notwendig, diese Kommentare immer hinzuschreiben:

```python
def test_divide_normal_numbers():
    result = divide(10, 5)
    assert result == 2
```

Entscheidend ist, dass der Test schnell verständlich bleibt.

---

## Eigenschaften guter Unit Tests

Ein guter Unit Test sollte möglichst:

- **klein** sein – er prüft einen klaren Sachverhalt,
- **verständlich** sein – man erkennt schnell, was erwartet wird,
- **reproduzierbar** sein – gleiche Ausgangslage ergibt dasselbe Ergebnis,
- **unabhängig** sein – er benötigt keinen vorher ausgeführten Test,
- **schnell** sein – wir möchten die Tests häufig ausführen können.

Auch der Name sollte möglichst deutlich machen, was getestet wird:

```python
def test_divide():
    ...
```

ist weniger aussagekräftig als:

```python
def test_divide_by_zero_raises_value_error():
    ...
```

Wenn dieser Test später fehlschlägt, erkennen wir schon am Namen, welches Verhalten betroffen ist.

---

## Automatisiertes und manuelles Testen

Automatisierte Tests ersetzen nicht jede Form des manuellen Testens.

Bei einer Benutzeroberfläche kann es beispielsweise sinnvoll sein, selbst zu überprüfen:

- Ist die Darstellung verständlich?
- Fühlt sich die Bedienung sinnvoll an?
- Ist eine Fehlermeldung hilfreich?

Solche Fragen lassen sich nicht immer sinnvoll mit einem kleinen Unit Test beantworten.

Automatisierte Tests sind dagegen besonders wertvoll für Verhalten, das wir immer wieder überprüfen möchten:

```text
Code ändern
    ↓
Tests ausführen
    ↓
sofort erkennen, ob bekanntes Verhalten kaputtgegangen ist
```

---

# Tests und Bugs: Regression Tests

Angenommen, wir entdecken später einen Fehler:

```python
divide(10, 0)
```

verhält sich nicht wie erwartet.

Ein sehr guter Workflow ist dann:

### 1. Einen Test schreiben, der den Bug reproduziert

```python
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

### 2. Test ausführen

Er sollte zunächst **fehlschlagen**.

Das ist wichtig.

Damit zeigen wir, dass unser Test den Bug tatsächlich erkennen kann.

### 3. Implementierung korrigieren

```python
if num_divide_by == 0:
    raise ValueError("Cannot divide by zero.")
```

### 4. Tests erneut ausführen

```bash
uv run pytest
```

Jetzt sollte der neue Test erfolgreich sein.

Der entscheidende Vorteil:

> Der Bug ist nicht nur heute repariert. Wir haben jetzt gleichzeitig einen automatischen Schutz dagegen, dass derselbe Fehler später unbemerkt wieder auftaucht.

Das bezeichnet man als **Regression Test**.

---

## Was bedeutet ein grüner Testlauf?

Angenommen pytest meldet:

```text
5 passed
```

Was können wir daraus schließen?

Wir können sagen:

> Alle fünf geschriebenen Tests waren erfolgreich.

Wir können **nicht** sagen:

> Das Programm ist garantiert korrekt.

Vielleicht haben wir schlicht einen wichtigen Fall vergessen.

Zum Beispiel könnten wir testen:

```python
assert divide(10, 5) == 2
assert divide(20, 5) == 4
assert divide(100, 5) == 20
```

und alle Tests wären grün.

Trotzdem hätten wir noch immer nie Division durch `0`, negative Zahlen oder ungültige Datentypen geprüft.

Deshalb gilt:

> **Die Qualität einer Test-Suite hängt nicht nur von der Anzahl der Tests ab, sondern vor allem davon, welche Fragen diese Tests stellen.**

---

## Black Box + White Box zusammen denken

Für unsere spätere Arbeit ist es hilfreich, beide Perspektiven zu kombinieren.

### Black Box

Frage:

> Welche Fälle ergeben sich aus den Anforderungen?

Zum Beispiel:

```text
normale Zahlen
negative Zahlen
Zähler = 0
Divisor = 0
falscher Datentyp
```

### White Box

Frage:

> Welche interessanten Entscheidungen oder Pfade sehe ich im Code?

Zum Beispiel:

```python
if num_divide_by == 0:
```

führt zur Frage:

> Habe ich sowohl `== 0` als auch `!= 0` getestet?

Beide Perspektiven ergänzen sich.

Die Spezifikation verhindert, dass wir nur testen, wie der aktuelle Code zufällig funktioniert.

Die Implementierung kann uns gleichzeitig auf Fälle aufmerksam machen, die wir beim Schreiben der Spezifikation übersehen haben.

---

## Fazit

Testing beginnt nicht mit pytest.

Testing beginnt mit der Frage:

> **Was soll mein Code eigentlich tun?**

Erst danach können wir überlegen:

```text
Anforderungen
      ↓
interessante Testfälle
      ↓
erwartetes Verhalten
      ↓
automatisierte Tests
      ↓
Implementierung überprüfen
```

Unit Tests helfen uns dabei, kleine Teile unseres Programms systematisch und reproduzierbar zu überprüfen.

Besonders wichtig sind dabei nicht nur die offensichtlichen Happy-Path-Beispiele, sondern Fragen wie:

```text
Was passiert an einer Grenze?
Was passiert bei ungültigen Eingaben?
Welche Fehler sollen explizit auftreten?
Welche Annahmen macht mein Code?
Welchen Fall habe ich bisher noch nicht getestet?
```

Und trotzdem bleibt:

> **Ein grüner Testlauf beweist nicht, dass ein Programm korrekt ist.**

Er zeigt nur, dass der Code die Tests bestanden hat, die wir geschrieben haben.

Die zentrale Kompetenz besteht deshalb nicht darin, möglichst viele `assert`-Statements zu schreiben.

Sie besteht darin, **gute Testfälle zu finden**.
