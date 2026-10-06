# Live Coding: Einführung in das Testen mit pytest

Dieses Live Coding baut bewusst auf dem bisherigen Beispiel mit einem kleinen Blackjack-Modul auf. Ziel ist nicht, ein vollständiges Spiel zu entwickeln, sondern Schritt für Schritt zu zeigen, **warum** wir automatisierte Tests brauchen und wie pytest uns dabei unterstützt.

> **Für Tutor:innen:** Die zentrale Geschichte der Session ist ein semantischer Fehler, den Python nicht meldet, pytest aber zuverlässig sichtbar macht.

## 1. Projekt anlegen

```bash
uv init blackjack-demo
cd blackjack-demo
uv add --dev pytest
```

Wir arbeiten mit der von uv erzeugten `src/`-Struktur und legen zusätzlich einen Testordner an:

```bash
mkdir tests
touch src/blackjack_demo/blackjack.py
touch tests/test_blackjack.py
```

Zwischendurch ruhig zeigen:

```bash
ls
```

und erklären:

```text
src/    -> eigentlicher Anwendungscode
tests/  -> automatisierte Tests
```

## 2. Eine erste Funktion

In `src/blackjack_demo/blackjack.py`:

```python
def count_cards(cards):
    """Return the blackjack value of a sequence of cards."""
    card_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }

    total = 0
    aces = 0

    for card in cards:
        if card not in card_values:
            raise ValueError(f"Invalid card: {card}")
        total += card_values[card]
        if card == "A":
            aces += 1

    # Careful: this condition contains a semantic bug.
    while total >= 21 and aces:
        total -= 10
        aces -= 1

    return total
```

Die Funktion ist syntaktisch korrekt. Sie läuft. Genau deshalb eignet sie sich gut für die Frage:

> **Woher wissen wir eigentlich, dass sie korrekt ist?**

## 3. Ein erster Test

In `tests/test_blackjack.py`:

```python
from blackjack_demo.blackjack import count_cards


def test_count_cards_without_aces():
    assert count_cards(["2", "3", "4"]) == 9
```

Tests ausführen:

```bash
uv run pytest
```

Erwartung: Der Test ist grün.

### Leitfrage

Bedeutet das, dass `count_cards()` korrekt ist?

**Nein.** Es bedeutet nur, dass der von uns getestete Fall funktioniert.

## 4. Mehrere Fälle testen

Wir ergänzen:

```python
def test_count_cards_blackjack():
    assert count_cards(["A", "Q"]) == 21
```

Dann:

```bash
uv run pytest
```

Jetzt sollte der zweite Test fehlschlagen.

### Gemeinsam analysieren

Für `A + Q` erhalten wir zunächst 21. Die Schleife lautet aber:

```python
while total >= 21 and aces:
```

Damit wird das Ass bereits bei exakt 21 von 11 auf 1 reduziert.

Korrektur:

```python
while total > 21 and aces:
```

Danach erneut:

```bash
uv run pytest
```

> **Kernbotschaft:** Ein semantischer Fehler kann völlig gültiger Python-Code sein. Ein guter Test macht die falsche Annahme sichtbar.

## 5. Tests sinnvoll aufteilen

Weitere Fälle:

```python
def test_count_cards_one_ace_reduced():
    assert count_cards(["A", "5", "9"]) == 15


def test_count_cards_two_aces():
    assert count_cards(["A", "A", "9"]) == 21


def test_count_cards_bust():
    assert count_cards(["10", "J", "Q"]) > 21
```

Hier kann diskutiert werden:

- Warum mehrere kleine Tests statt einer riesigen Testfunktion?
- Welche Namen helfen beim Lesen einer fehlgeschlagenen Testausgabe?
- Welche Randfälle fehlen noch?

## 6. Parametrisierung

Mehrere sehr ähnliche Fälle lassen sich mit `pytest.mark.parametrize` übersichtlich bündeln:

```python
import pytest

from blackjack_demo.blackjack import count_cards


@pytest.mark.parametrize(
    "cards, expected",
    [
        (["A", "Q"], 21),
        (["A", "5", "5"], 21),
        (["A", "9"], 20),
        (["A", "A", "7"], 19),
    ],
)
def test_count_cards_with_aces(cards, expected):
    assert count_cards(cards) == expected
```

Ausführen:

```bash
uv run pytest -q
```

### Tutor:innen-Hinweis

Hier lohnt es sich, absichtlich einen erwarteten Wert falsch zu setzen. pytest meldet dann genau, welcher Parametersatz fehlgeschlagen ist.

## 7. Manche Dinge sollen fehlschlagen

Ungültige Karten sollen eine `ValueError` auslösen. Genau dieses Verhalten können wir testen:

```python
def test_unknown_card_raises_value_error():
    with pytest.raises(ValueError, match="Invalid card: X"):
        count_cards(["X"])
```

Das ist ein wichtiger Perspektivwechsel:

> Ein Fehler ist nicht immer ein Bug. Manchmal ist das **Auslösen einer Exception** das korrekte Verhalten.

## 8. Regressionstest demonstrieren

Jetzt kann eine bereits getestete Codezeile absichtlich kaputt gemacht werden, z. B.:

```python
"K": 9,
```

Danach:

```bash
uv run pytest
```

Die Suite sollte den Fehler finden.

Das ist der Kern eines Regressionstests: Verhalten, das einmal korrekt war, wird nach späteren Änderungen automatisch erneut geprüft.

## 9. Schnelle pytest-Kommandos

```bash
uv run pytest
uv run pytest -q
uv run pytest tests/test_blackjack.py
uv run pytest -k ace
uv run pytest -x
```

- `-q`: kompaktere Ausgabe
- `-k ace`: nur Tests, deren Name auf den Ausdruck passt
- `-x`: nach dem ersten Fehler abbrechen

## 10. Abschlussfragen

Die Studierenden sollten danach erklären können:

1. Warum ein Programm trotz fehlerfreiem Start semantisch falsch sein kann.
2. Was ein `assert` in einem Test ausdrückt.
3. Warum Tests in eigenen Dateien liegen.
4. Wie `uv run pytest` Tests startet.
5. Warum Rand- und Fehlerfälle wichtig sind.
6. Wann `pytest.mark.parametrize` sinnvoll ist.
7. Warum ein Test auf eine erwartete Exception ein sinnvoller Test ist.

## Mini-Übung

Erweitert `count_cards()` bzw. die Tests um mindestens zwei zusätzliche Fälle, z. B.:

- leere Kartenliste,
- mehrere Asse,
- eine einzelne Karte,
- ungültige Karte,
- genau 21 Punkte,
- mehr als 21 Punkte.

Dabei gilt: **Erst überlegen, welches Verhalten erwartet wird; dann den Test formulieren.**
