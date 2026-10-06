# Linting

**Was ist Linting?**
Linting ist der Prozess des Überprüfens des Quellcodes auf programmatische und stilistische Fehler. Ein "Linter" ist ein Tool, das den Code automatisch überprüft und häufige Fehler oder Abweichungen von Stilrichtlinien meldet. In Python gibt es verschiedene Linter, z.B. `pylint` oder `flake8`, aber zunehmend v.a. `black` und `ruff`. Hier konzentrieren wir uns auch auf die zwei etwas neueren Linter `ruff` und `black` die zunehmend Einzug halten und vielen Entwickler*innen als moderner und leistungsfähiger gelten.

**Code Beispiel**

Um die Linter zu testen, nehmen wir das folgende (nonsense) Code Beispiel:

```python
import os
import numpy as np

magic_numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]
magic_dictionary={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",5:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l"}

def PowerCompute(a, b, c):
    number1 = a**b
    number2=b**a
    max_number = max(number1,number2)
    if max_number<np.max(magic_numbers):
        print(magic_dictionary[max(magic_numbers)])
        return max(magic_numbers)
    else:
        return max_number
    return 11

class power_computer:
    def __init__(self) -> None:
        self.a = 11
        self.b = 12
        self.c = 13

    def computeSomething(self):
        print(PowerCompute(self.a, self.b, self.b))

#Run code for testing
MyComputer = power_computer()
MyComputer.computeSomething()
```

## Ruff

Ruff ist ein äußerst schneller Python-Linter und Code-Formatter, der sich zunehmender Beliebtheit erfreut. Er hilft uns dabei sauberen, wartbaren und fehlerfreien Code zu schreiben.

### Installation von Ruff

Die Installation von Ruff ist unkompliziert, und das Tool funktioniert „out of the box“, ohne dass komplizierte Konfigurationen erforderlich sind. Hier sind die wichtigsten Installationsmethoden für verschiedene Systeme:

- Mit **Pip** (Standard für Python-Projekte):
```bash
python -m pip install ruff
```
- Oder mit **Conda**:
```bash
conda install -c conda-forge ruff
```

### Linting mit Ruff
Ruff ermöglicht es dir, deinen Python-Code schnell auf Fehler und Inkonsistenzen zu überprüfen. Während Linting zwar keine Bugs garantiert entdeckt, hilft es dir dabei, stilistische Probleme und potenzielle Fehler im Code zu identifizieren.

Mit dem folgenden Befehl überprüft Ruff alle Code-Dateien im aktuellen Ordner
```bash
ruff check
```

Es könnnen auch nur einzelne Dateien oder Ordner überprüft werden. In unserem Fall z.B. nur der oben angezeigte Code (nehmen wir mal an dieser befindet sich in der Datei `code_example_for_linting.py`):
```bash
ruff check code_example_for_linting.py
```

Daraufhin gibt uns Ruff eine umfangreiche Meldung zurück (hier das Ergebnis mit Ruff in der Version 0.6.7):
```bash
code_for_linting.py:1:8: F401 [*] `os` imported but unused
  |
1 | import os
  |        ^^ F401
2 | import numpy as np
  |
  = help: Remove unused import: `os`

code_for_linting.py:14:55: F601 Dictionary key literal `5` repeated
   |
12 |     8
13 | ]
14 | magic_dictionary={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",5:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l"}
   |                                                       ^ F601
15 |
16 | def PowerCompute(a, b, c):
   |
   = help: Remove repeated key literal `5`

Found 2 errors.
[*] 1 fixable with the `--fix` option.
```

In diesem Beispiel findet Ruff zwei Fehler und sagt das einer davon automatisch behoben werden kann und zwar mit:
```bash
ruff check --fix code_example_for_linting.py
```

```{warning}
**Achtung!** Wenn ihr `ruff` mit der Option `--fix` (oder, wie wir gleich sehen werden: `--format`) ausführt, werden direkt eure Dateien entsprechend angepasst. Das kann sehr praktisch sein, ist aber oft gar nicht direkt gewünscht. Wenn ihr also nur "testen" wollt, ob der Code die Linter-Regeln einhält dann sollte Ruff erst ohne diese Optionen ausgeführt werden.
```

### Welche Regeln soll Ruff überprüfen?

In dem Fall den wir gerade gesehen haben wurde Ruff mit den Standardeinstellungen verwendet. Hier wird erstmal nur auf gröbere Fehler geachtet.
Mit Ruff lassen sich aber sehr viele etablierte Regeln im Bezug auf Code Style überprüfen.

Es können z.B. einzelne Regeln ausgewählt werden über `rule`, eine Übersicht der mehr als 800 Möglichkeiten [findet ihr hier](https://docs.astral.sh/ruff/rules/).

Falls du mehr über einen bestimmten Fehler wissen möchtest, kannst du den Fehlercode mit dem Befehl `ruff rule` näher untersuchen. Zum Beispiel:

```bash
ruff check code_example_for_linting.py --select F601
```

In den meisten Fällen interessiert uns aber nicht nur eine einzige Regel sondern wir möchten viele gleichzeitig testen. Dafür können auch ganze in der [Ruff Dokumentation der `Rules`](https://docs.astral.sh/ruff/rules/) angegebene Gruppen genutzt werden, z.B.

```bash
ruff check code_example_for_linting.py --select F
```
Das nutzt dann die "Pyflakes" Regeln. Oder für den "pydocstyle":
```bash
ruff check code_example_for_linting.py --select D
```
Auch möglich wäre sogar `ALL` um alle Regeln auszuwählen:
```bash
ruff check code_example_for_linting.py --select ALL
```
```{note}
Am besten an dieser Stelle einfach mal selbst die hier angegebenen Optionen (bzw. gerne auch noch weitere) ausprobieren um ein Gefühl dafür zu bekommen wie unterschiedlich das Feedback des Ruff-Linters ausfällt.
```

### Konfiguration von Ruff

Bei größeren Python-Softwareprojekten macht es oft sogar Sinn, die für das Projekt verbindlichen Regeln einmal gemeinsam festzulegen. Diese können dann für Ruff in einer Konfigurationsdatei hinterlegt werden. Die Konfigurationsdatei kann entweder `ruff.toml`, `.ruff.toml` oder `pyproject.toml` heißen. Hier ein einfaches Beispiel für eine `ruff.toml`-Datei:
```toml
line-length = 120

[lint]
select = ["E501", "I"]
```
Mit dieser Konfiguration wird Ruff auf eine maximale Zeilenlänge von 120 Zeichen prüfen und spezifische Regeln für Importe (I-Regeln) und Zeilenlängen (E501) anwenden.
Wenn die entsprechende `.toml` im selben Ordner oder einem der Unterordner liegt, wird Ruff dies erkennen und die entsprechenden Einstellungen übernehmen wenn wir `ruff check` ausführen.


### Ruff als Formatter
Ruff ist ein sehr schneller und umfangreicher **Linter** und kann uns sehr gut dabei unterstützen bestimmte Code Styles konsistent in unseren Projekten umzusetzen. Wir haben schon gesehen, dass gröbere Fehler bereits mit `--fix` behoben werden können. Alle anderen Hinweise, typischerweise zu Aussehen und Formatierung des Codes, werden nur als Text-Feedback zurückgegeben.

Es ist allerdings auch möglich Ruff zusätzlich als **Formatter** einzusetzen, d.h. als ein Tool das automatisiert bestimmte Formatierungsregeln umsetzt so dass wir dies nicht mehr manuel machen müssen.
Wir vorhin schon gewarnt, bedeutet dies aber auch, dass Ruff direkt unsere Dateien entsprechend verändert.

Die Formatierungsoption können wir nutzen über
```bash
ruff format
```



### Weitere Informationen zu `ruff`

- [Real Python Tutorial](https://realpython.com/ruff-python/)
- [Ruff Tutorial](https://docs.astral.sh/ruff/tutorial/)

## Black

Genau wir Ruff (aber anders als Pylint und Flake8) ist `Black` nicht nur ein Linter, sondern auch ein Code-Formatter. Anstatt nur stilistische Probleme und Fehler im Code zu melden, formatiert Black den Code automatisch gemäß seinem eigenen Stil, der eng an PEP 8 angelehnt ist.

**Hauptmerkmale:**

- Automatische Codeformatierung.
- Hat eine strikte und unveränderliche Stilrichtlinie, die es "The Blackened" nennt.

**Vorteile:**

- Keine Entscheidungen bezüglich des Stils: Black entscheidet für euch.
- Spart Zeit, da keine Diskussionen über Codierungsstil mehr erforderlich sind.
- Sehr schnell und kann leicht in CI-Workflows integriert werden.

**Nachteile:**

- Macht keine Kompromisse: Black macht keine Ausnahmen und dies kann für manche Teams zu streng sein.
- Kann nicht angepasst werden, um bestimmte Stilpräferenzen zu berücksichtigen.
- Ersetzt oft nicht ausreichend ein strengeres Linting (wie z.B. von `pylint` oder `ruff`)

### Anwendung

Zuerst soll `black` als *Linter* eingesetzt werden.

```bash
black code_example_for_linting.py --check
```

Die Ausgabe die wir bekommen ist aber noch nicht sehr informativ. Darum besser:

```bash
black code_example_for_linting.py --check --diff
```

Als nächstes einmal ausprobieren wie `black` als *Formatter* funktioniert (was eigentlich auch der Standard-Modus von `black` ist). Um die Datei nicht zu überschreiben, bitte einmal vorher die Datei kopieren und umbenennen (z.B. in bash mit `cp code_example_for_linting.py code_example_before_black.py`).

Dann

```bash
black code_example_before_black.py
```

### Mehr Informationen zu `black`

- https://black.readthedocs.io/en/stable/index.html
- https://calmcode.io/black/introduction.html



## Ausblick & Weitere Quellen

Es gibt noch viele weitere Linter, sowie auch umfangreichere Tools um automatisiert die Code Qualität zu überprüfen bzw. zu verbessern. Zwei erwähnenswerte:

- `mypy` wird genutzt um die korrekte/konsistente Verwendung von Datentypen zu überprüfen
- `SonarCloud` ist ein **sehr** umfangreiches Tool um Code zu beurteilen und potentielle Schachstellen aufzudecken.


Wir haben hier die sehr verbreiteten Linter `pylint` und `flake8` ausgelassen. Zu beiden gibt es aber zum Glück online viele Tutorials.
Zum Beispiel:

- [Flake8 Dokumentation](https://flake8.pycqa.org/en/latest/)
- [Calmcode Tutorial](https://calmcode.io/flake8/introduction.html)
- [Pylint Dokumentation](https://docs.pylint.org/tutorial.html)
