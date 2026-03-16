## Live Coding Einführung in das Testen von Code

Testen ist ein wichtiger Teil der Softwareentwicklung, der sicherstellt, dass sich Ihr Code wie erwartet verhält. In dieser Sitzung geht es darum, wie wir Code mit Python effektiv testen können.

### Wir beginnen mit einem einfachen Funktionstest

Betrachten wir zunächst eine einfache Funktion und testen sie:

```python
def meine_funktion(x):
    return x + x/2

def test_meine_funktion():
    assert my_function(10) == 15 # Du kannst den Wert ändern, um verschiedene Ergebnisse zu sehen.

if __name__ == „__main__“:
    test_my_function()
```

Dies ist ein einfacher Ansatz, hat aber seine Grenzen, insbesondere bei größeren Projekten:

- Der Code und seine Tests befinden sich in derselben Datei.
- Die Verwaltung der Tests wird bei Projekten mit mehreren Dateien umständlich.

### Trennung von Code und Tests

Für eine bessere Organisation können wir den Code und die Tests in separate Dateien aufteilen:

- `functions.py` enthält die eigentliche Funktion.
- `test_functions.py` enthält Tests für die Funktion.

Beispiel:

```python
# functions.py
def meine_funktion(x):
    „„“Das ist eine seltsame kleine Berechnung...„““
    return x + x/2

# test_functions.py
from functions import my_function

def test_my_function():
    assert my_function(10) == 15
```

Die Ausführung dieser Tests kann mit `python test_my_function.py` oder durch Ausführen der Codedatei in Ihrer IDE erfolgen. Wenn dein Softwareprojekt jedoch wächst, wirst du wahrscheinlich viele verschiedene Dateien mit Tests haben, so dass es keine gute Option ist, all diese Tests manuell auszuführen. Der richtige Weg, um alle Tests auszuführen, ist die Verwendung der Bibliothek `pytest`!

### Verwendung von pytest zum Testen

`pytest` vereinfacht den Testprozess, besonders für Projekte mit mehreren Testdateien. Es erkennt automatisch Dateien und Funktionen, die dem Muster `test_*` entsprechen. Deshalb sollten die Tests in eigenen Dateien gespeichert werden, die mit `test_` beginnen und auch die einzelnen Funktionsnamen mit `test_` beginnen lassen. Um alle Ihre Testfunktionen in einem Ordner (und allen Unterordnern) auszuführen, können wir einfach folgendes ausführen
``bash
pytest

```
aus dem Hauptverzeichnis des Projekts.

## Erstellen einer Python-Bibliothek mit Tests

Nun wollen wir uns ein wenig im Programmieren üben und ein einfaches Blackjack-Spiel erstellen, für das wir dann geeignete Tests schreiben können.

### Entwicklung des Spiels
Blackjack ist ein recht einfaches Kartenspiel. (KURZE BESCHREIBUNG HINZUFÜGEN)


Wir werden den Codeentwurf vorerst einfach halten und mit zwei Hauptfunktionen beginnen:

1. `Karten_zählen(Karten)`
2. play_game(names)`

Erstellen wir zuerst eine lokale blackjack.py Datei wie folgt:

```python
# blackjack.py
def count_cards(cards):
„„“Zählt die Kartenwerte in Blackjack.„““
# Details zur Implementierung...

def play_game(names):
„„“Spiellogik für Blackjack.„““
# Platzhalter für die Spiellogik
```

Eine erste Version von `count_cards()` könnte wie folgt aussehen:

```python
# Vorsicht: der folgende Code enthält einen semantischen Fehler

def count_cards(cards):
    „„“Berechnet den Gesamtwert der gegebenen Karten in einem Blackjack-Spiel.

    Bildkarten (J, Q, K) zählen als 10, nummerierte Karten zählen als ihr Wert,
    und Asse zählen als 11 oder 1, wobei der Wert so angepasst wird, dass 21 nicht überschritten wird.

    Args:
        cards (list of str): Eine Liste von Kartenwerten, z. B. ['A', '7', 'K'].
	„"“
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    gesamt = 0
    Asse = 0
    for card in cards:
        if card not in card_values:
            raise ValueError(f „Ungültige Karte: {Karte}“)

        # Kartenwert zu Summe addieren
        gesamt += karten_werte[karte]
        wenn Karte == 'A':
            Asse += 1

    # Asse berücksichtigen, wenn Summe über 21 ist
    while Gesamt >= 21 und Asse:
        Summe -= 10
        Asse -= 1

    Gesamtbetrag zurückgeben

def play_game(names):
    „„“Spiellogik für Blackjack.„““
    # Platzhalter für Spiellogik
```

### Schreiben von Tests für das Spiel
Nun wollen wir sicherstellen, dass dieser Code wie vorgesehen läuft, jetzt und in Zukunft. Um dies zu erreichen, werden wir einige aussagekräftige Testfunktionen schreiben, die sicherstellen, dass unser Code robust ist und sich wie erwartet verhält.
Die Tests werden in einer separaten Datei geschrieben, `test_blackjack.py`. Für den Moment können wir diese Datei einfach im selben Ordner wie `blackjack.py` haben. Später, bei größeren Projekten, werden Code und Testdateien normalerweise in verschiedenen Ordnern aufbewahrt. 

```python
# test_blackjack.py
from blackjack import count_cards

def test_count_cards():
    # Mehrere Assertions, um verschiedene Szenarien zu testen.
```

Das Ausführen dieser Tests mit `pytest` wird helfen, jegliche Probleme in der Spiellogik zu identifizieren.

### Verbessern der Teststruktur

- Es ist von Vorteil, Tests in kleinere, gezieltere Funktionen zu unterteilen.
- Dies ermöglicht präzisere Tests und eine leichtere Identifizierung von Problemen.
- Es ist besser, mehrere kleinere Testfunktionen zu definieren als eine große Testfunktion, denn wenn ein Test fehlschlägt, ist es viel einfacher herauszufinden, woher das Problem kommt.

Beispiel:

```python
def test_count_cards_no_aces():
    assert count_cards(['2', '3', '4']) == 9

def test_count_cards_with_aces():
    assert count_cards(['A', '3', '4']) == 18
    assert count_cards([„A“, „A“]) == 12
    assert count_cards([„Q“, „A“]) == 21
    assert count_cards([„5“, „5“, „A“]) == 21

def test_mehr_als_21():
    assert count_cards([„5“, „10“, „K“, „7“]) > 21
```
Wenn wir nun `pytest` ausführen, sollten wir sehen, dass nicht alle Tests für die oben angegebene Funktion `count_cards()` erfolgreich sind.

Was ist mit dem Code falsch? Bitte finde den Fehler und behebe ihn! Dann sollten die Tests alle erfolgreich sein.

### Dekoratoren für effizientes Testen verwenden

Im obigen Beispiel der Testfunktionen haben wir bereits eine wichtige Best Practice für Unit-Tests umgesetzt. Anstatt einfach alle Asserts in eine Funktion zu schreiben, wurde sie in mehrere verschiedene Funktionen mit unterschiedlichen zu testenden Dingen aufgeteilt. Das hilft später dabei, zu sehen, wo etwas schief läuft (wenn es schief läuft).

Ein Problem bleibt jedoch, dass immer dann, wenn ein `assert` fehlschlägt, die folgenden Codezeilen in derselben Funktion nicht ausgeführt werden. Ersetze die erste Zeile in der zweiten Funktion durch `assert count_cards(['A', '3', '4']) == 999` und führe dann `pytest` aus, um zu sehen, was ich meine.

Wir könnten jedes `assert` in eine eigene Funktion schreiben, aber das ist zu kompliziert. Eine viel bessere Lösung bietet ein spezieller pytest-Dekotrator: `pytest.mark.parametrize`. Dieser erlaubt es, mehrere Szenarien mit einer einzigen Testfunktion zu testen.

Beispiel:

```python
import pytest

@pytest.mark.parametrize(„cards, score“, 
                        [(['A', '3', '4'], 18),
                        (['A', 'A', '9'], 21), ...]
                        )
def test_count_cards_with_aces(cards, score):
    assert count_cards(cards) == score
```
Nebenbei bemerkt: Für die oben geschriebene Funktion `count_cards()` könnte die Eingabe auch `„A34“` anstelle von `['A', '3', '4']` sein. Das ist Python. (Apropos: warum funktioniert das eigentlich?)

### Manche Dinge gehen besser schief

Mit pytest können wir nicht nur Dinge testen, die wie vorgesehen funktionieren, zum Beispiel mit assert wie oben. Wir können auch testen, ob Dinge dort fehlschlagen, wo sie fehlschlagen sollen. Das kann mit einer `pytest.raises`-Konstruktion gemacht werden.

Hier ist ein Beispiel:
```python
def test_unbekannte_Karten():
    with pytest.raises(ValueError) as error:
        count_cards([„X“])
    assert „Ungültige Karte: X“ in str(error.value)
```
Damit wird getestet, ob die Funktion korrekt einen ValueError auslöst und ob die erwartete Meldung zurückgegeben wird. Einige Dinge *sollten* fehlschlagen, und dann ist es gut, auch diese Fälle zu testen.