# Cleaner Code, Better Code

**Eingangsfrage 1:**
*Was bedeutet „besser“?*

**Antworten:**

- „Besser“ definiert eine Richtung, aber keinen festen Endpunkt.
- Perfektion ist nicht das Endziel, da es im wirklichen Leben selten erreichbar ist.
- Ziel ist, einen Code zu schreiben, der beständig, wiederholbar und zuverlässig arbeitet.
- Die kommenden Wochen werden tiefer in diese Prinzipien eintauchen.

------

**Eingangsfrage 2:**
*Brauche ich das?*

**Antworten:**

1. Ja! Schon aus pragmatischen Gründen:
   - Ohne solide (Python-)Programmierkenntnisse ist ein Abschluss in DAISY kaum machbar.
   - Firmen haben Erwartungen, wenn "Data Science / KI" im Lebenslauf steht. Und sie prüfen diese!

2. Solide Programmierfähigkeiten öffnen in der Data Science/KI Welt viele Türen. Es geht nicht nur ums Programmieren, sondern auch um das Verstehen und Leiten von Projekten.

------

In der Welt der Programmierung geht es nicht nur darum, dass der Code funktioniert. Die Art und Weise, wie der Code geschrieben, organisiert und präsentiert wird, kann einen großen Unterschied in der Produktivität, Zusammenarbeit und Wartungsfähigkeit machen. In diesem Teil werden wir uns mit den Prinzipien des "Clean Code" und den Best Practices für besseres Programmieren in Data Science und KI vertiefend beschäftigen.

## 1. Die Bedeutung von „besserem“ Code

### 1.1. Was ist „besser“?
„Besser“ ist ein relatives Konzept. In der Programmierung bezieht es sich oft darauf, wie effizient, lesbar und wartbar ein Code ist. Es ist wichtig zu betonen, dass "besser" nicht immer "perfekt" bedeutet. In der echten Welt ist es oft nicht möglich oder sogar notwendig, einen perfekten Code zu schreiben. Stattdessen sollte das Ziel sein, ständig zu verbessern und einen Code zu erstellen, der wiederholbar und zuverlässig funktioniert.

### 1.2. Warum besserer Code wichtig ist

Besserer Code ist aus mehreren Gründen wichtig:

- **Zuverlässigkeit:** Code, der den Best Practices folgt, hat tendenziell weniger Fehler und ist vorhersehbarer.
- **Wartbarkeit:** Es ist einfacher, Code zu aktualisieren und zu verbessern, wenn er gut organisiert und dokumentiert ist.
- **Zusammenarbeit:** In Teams ist es wesentlich einfacher, mit Code zu arbeiten, der den gemeinsamen Standards folgt.

### 1.3. Der Weg zu „besserem“ Code: Clean Code

Während es viele Methoden gibt, um Code zu verbessern, ist eine der effektivsten und anerkanntesten Methoden die Anwendung von "Clean Code" Prinzipien. "Clean Code" bietet nicht nur eine klare Struktur und Lesbarkeit, sondern stellt auch sicher, dass der Code nachhaltig, wartbar und effizient bleibt. Im nächsten Abschnitt werden wir uns genauer mit der Definition, den Vorteilen und den Prinzipien von Clean Code beschäftigen und wie diese in der Python-Programmierung umgesetzt werden können.

## 2. Clean Code - Grundlagen

#### Was ist Clean Code?
Clean Code ist ein Code, der leicht zu lesen, zu verstehen und zu warten ist. Es geht nicht nur darum, wie der Code aussieht, sondern auch darum, wie er strukturiert ist.

Clean Code ist aber nicht nur ein Ziel, sondern auch eine Methode. Es gibt  bestimmte Prinzipien und Best Practices, die Entwickler befolgen können, um ihren Code sauberer und effizienter zu gestalten.

#### Weshalb Clean Code?

- **Lesbarkeit:** Ein sauberer Code ist einfacher zu lesen und zu verstehen.
- **Wartbarkeit:** Ein sauberer Code ist einfacher zu warten und zu erweitern.
- **Produktivität:** Mit sauberem Code können Entwickler schneller und effizienter arbeiten.

**Eingangsbeispiele und ihre Bedeutung**
Zur Verdeutlichung der Prinzipien von Clean Code werden im Laufe des Kapitels verschiedene Codebeispiele analysiert und diskutiert.

```python
animals = ['dog', 'cat', 'elephant']
# vs
animals= [    'dog',   'cat',"elephant"   ]
```

**Fragen zum Nachdenken:**

- Wer legt fest, wie Code aussehen sollte?
- Warum nicht individuell entscheiden?

**Antworten:**

- Für den Python-Interpreter ist der Stil nebensächlich, aber Menschen lesen den Code!
- Ziel 1: Der Stil soll die Lesbarkeit unterstützen.
- Ziel 2: Code sollte global verständlich sein, nicht nur für den Autor.

### **Style Guides und ihre Bedeutung**

Style Guides sind Sammlungen von Konventionen und Best Practices für eine bestimmte Programmiersprache oder ein bestimmtes Framework. Sie definieren einen Standard, wie Code geschrieben und formatiert werden sollte, um Konsistenz, Lesbarkeit und Wartbarkeit zu gewährleisten.

In der Welt von Python ist PEP 8 der bekannteste und am weitesten verbreitete Style Guide, und viele der Konzepte und Prinzipien, die er enthält, sind nicht nur für Python, sondern auch für andere Sprachen relevant.

#### PEP 8 - Der Python Style Guide
PEP 8, das für "Python Enhancement Proposal 8" steht, ist der offizielle Style Guide für Python-Code. Entwickelt wurde er von der Python-Community, um Best Practices und Stilkonventionen zu definieren, die die Lesbarkeit von Python-Code fördern. Es behandelt Themen wie  Namenskonventionen, Kommentarstile, Zeilenlänge und viele andere Aspekte des Python-Codes.

**Aufgabe:**

- Eine sinnvolle Regel aus PEP 8 finden.
- Eine Regel aus PEP 8 finden, die als überflüssig betrachtet wird.

**Beispiel:**

> “One of Guide’s key insights is that code is read much more often than it is written.”

> “Consistency with this style guide is important. However, use judgment if a guideline seems inapplicable.”



Einige wichtigsten Punkte aus PEP 8 sind:

**a) Namenskonventionen**

- **Variablen:** Sollten in `snake_case` benannt werden, das bedeutet, alle Buchstaben in Kleinbuchstaben und Worte durch Unterstriche getrennt. Beispiel: `user_input`, `load_data_function`.
- **Funktionen und Methoden:** Verwenden ebenfalls `snake_case`. Beispiel: `def calculate_average()`.
- **Klassen:** Sollten in `PascalCase` benannt werden, wobei jedes Wort großgeschrieben wird und ohne Unterstriche. Beispiel: `CarFactory`, `UserDatabase`.
- **Konstanten:** Werden in Großbuchstaben mit Unterstrichen geschrieben, z.B. `MAX_LENGTH`, `DEFAULT_COLOR`.

**b) Leerzeichen**

Leerzeichen spielen eine entscheidende Rolle in Python, insbesondere wegen seiner Einrückungssyntax. Einige der PEP 8-Richtlinien für Leerzeichen sind:

- Verwenden von 4 Leerzeichen pro Einrückungslevel.
- Keine Leerzeichen rund um Funktions- und Methodenparameter: `func(x, y)` nicht `func( x, y )`.
- Leerzeichen um Operatoren herum: `x = 1` und nicht `x=1`.
- Keine Leerzeichen am Ende von Zeilen.

**c) Zeilenlänge**

- Traditionell wurde empfohlen, die Zeilen auf maximal 79 Zeichen für Code und 72 für Kommentare zu beschränken. Dies war historisch bedingt durch die Breite von Displays und die Lesbarkeit.
- In modernen Entwicklungsumgebungen ist jedoch eine Zeilenlänge von bis zu 100 oder 120 Zeichen oft akzeptabel, da die Bildschirme heute in der Regel breiter sind. Trotzdem sollte der Code so formatiert sein, dass er ohne horizontales Scrollen leicht lesbar ist.

**d) Zeilenumbrüche**

In Fällen, in denen ein Ausdruck oder eine Anweisung zu lang wird, sollte ein Zeilenumbruch verwendet werden, um die Lesbarkeit zu erhöhen. PEP 8 bietet mehrere Methoden, um dies elegant zu tun, einschließlich:

- Bei Verwendung von Klammern (`()`, `{}`, `[]`) kann der Code nach der Klammer umgebrochen werden.
  ```python
  # Gut:
  total_sum = sum(
      item_1, item_2, item_3, 
      item_4, item_5
  )
  
  # Schlecht:
  total_sum = sum(item_1, item_2, item_3, item_4, item_5)
  ```
- Bei langen Bedingungen kann `and` oder `or` zum Umbruch verwendet werden.
  ```python
  # Gut:
  if (condition_1 and condition_2 and 
      condition_3 and condition_4):
      do_something()
  
  # Schlecht:
  if condition_1 and condition_2 and condition_3 and condition_4:
      do_something()
  ```

  

**e) Importieren von Modulen**

Importe sollten immer am Anfang einer Datei stehen und in folgender Reihenfolge organisiert werden:

1. Standardbibliotheken
2. Drittanbieterbibliotheken
3. Lokale Anwendungs-/Bibliotheks-spezifische Importe

Außerdem sollte man einen Abstand zwischen den verschiedenen Import-Gruppen lassen.

**Beispiel:**

```python
import os  # Standardbibliothek
import sys  # Standardbibliothek

from flask import Flask  # Drittanbieterbibliothek

from .models import User  # Lokale Anwendung
```

**f) Kommentare**

Kommentare sind wichtig, um den Code verständlicher zu machen, insbesondere wenn er komplex ist. Es sollten jedoch keine offensichtlichen Dinge kommentiert werden. Außerdem sollte der Code so klar und lesbar wie möglich geschrieben werden, sodass er von sich aus selbsterklärend ist.

**Beispiel:**

```python
# Gut:
def add(a, b):
    return a + b

# Schlecht:
def add(a, b):
    # Addiere a zu b
    return a + b
```

**g) Vermeidung von globalen Variablen**

PEP 8 empfiehlt, die Verwendung von globalen Variablen zu vermeiden, da sie den Code schwerer verständlich und wartbar machen können. Wenn sie unvermeidlich sind, sollten sie jedoch klar kommentiert werden.

**Beispiel:**

```python
# Vermeiden:
global_variable = "I am global"

def print_global():
    print(global_variable)

# Besser:
def print_value(value):
    print(value)
```

**h) Fehlertypen nicht allgemein fangen**

Es sollte vermieden werden, allgemeine Exception-Blöcke zu verwenden, da dies zu unerwarteten Fehlern führen kann.

**Beispiel:**

```python
# Schlecht:
try:
    value = int(input())
except:
    print("Ein Fehler ist aufgetreten!")

# Gut:
try:
    value = int(input())
except ValueError:
    print("Bitte geben Sie eine gültige Zahl ein!")
```

Durch das Beachten dieser und anderer Richtlinien aus PEP 8 kann man sicherstellen, dass der Python-Code nicht nur funktionsfähig, sondern auch gut lesbar und wartbar ist. Es lohnt sich, regelmäßig auf PEP 8 zurückzugreifen und den eigenen Code danach zu überprüfen

## 3. Linting

**Was ist Linting?**
Linting ist der Prozess des Überprüfens des Quellcodes auf programmatische und stilistische Fehler. Ein "Linter" ist ein Tool, das den Code automatisch überprüft und häufige Fehler oder Abweichungen von Stilrichtlinien meldet. In Python gibt es verschiedene Linter, wobei einige der bekanntesten `pylint`, `flake8` und `black` sind.
Und, relativ neu aber (nach meiner Einschätzung) zukünftig häufig genutzt, ist `ruff`.

### Code Beispiel

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



### pylint

(Falls noch nicht vorhanden, installieren mit `pip install pylint`.)

Pylint ist ein äußerst umfangreicher Python-Linter, der darauf abzielt, fehlerhaften Code und stilistische Inkonsistenzen in Python-Programmen aufzudecken. Er verwendet eine Vielzahl von Heuristiken, um potenzielle Fehler und schlechte Praktiken im Code zu identifizieren.

**Hauptmerkmale:**

- Überprüft, ob Module und Klassen den vorgegebenen Codierungsstandards entsprechen.
- Erkennt Fehler oder Probleme, die bei der Ausführung auftreten könnten.
- Bietet detaillierte Berichte über die Codequalität.
- Erlaubt die Anpassung der Regeln durch Konfigurationsdateien und Inline-Kommentare.

`pylint` lässt sich einfach über die Kommandozeile ausführen mit:

```bash
pylint code_example_for_linting.py
```

Am besten die Datei kopieren und umbenennen (z.B. in bash mit `mv code_example_for_linting.py code_example_pylint.py`). Anschließend versuche, den *Linter* zufrieden zu stellen...



### flake8

Flake8 ist ein Wrapper-Tool, das mehrere andere Python-Linting-Tools kombiniert. Insbesondere verknüpft es PyFlakes, pycodestyle (früher bekannt als pep8) und McCabe zu einem einzigen, einfach zu verwendenden Tool.

**Hauptmerkmale:**

- Überprüft den Code auf syntaktische Fehler mit PyFlakes.
- Überprüft den Code auf PEP 8-Konformität mit pycodestyle.
- Bewertet die Komplexität des Codes mit McCabe.

**Vorteile:**

- Etwas Schneller und effizienter (als z.B. pylint).
- Kombiniert die Stärken mehrerer Linter.
- Einfache Integration in Entwicklungsworkflows.

### Anwendung

`flake8` lässt sich einfach über die Kommandozeile ausführen mit:

```bash
flake8 code_example_for_linting.py
```

Am besten die Datei kopieren und umbenennen (z.B. in bash mit `mv code_example_for_linting.py code_example_flake8.py`). Anschließend versuche, den *Linter* zufrieden zu stellen...

**Anpassungen**

Oft gibt es einzelne Aspekte, die wir nicht für wichtig halten, oder bei denen wir bewusst von Stil-Vorgaben abweichen. Dafür lassen sich viele Linter ziemlich detailiert anpassen. Ein Beispiel hier wäre die Änderung der maximal gewünschten Zeilenlänge von 79 auf z.B. 120 Zeichen:

```bash
flake8 --max-line-length 120 code_example_for_linting.py
```

Oder, wenn wir eine spezielle Meldung ignorieren wollen, geht z.B.

```bash
flake8 --ignore E231 code_example_for_linting.py
```

Es ist auch möglich einen Linter über eine spezielle Konfigurationsdatei noch viel detaillierter auf die eigenen Bedürfnisse abzustimmen. 

#### Mehr Informationen zu `flake8`

- https://flake8.pycqa.org/en/latest/
- https://calmcode.io/flake8/introduction.html

### ruff

Jetzt noch ein recht neues Python Tool: `ruff`.

Kann ebenfalls mit `pip install ruff` installiert werden.

Danach wird es z.B. als umfangreicher Linter ausgeführt mit:

```bash
ruff --select=ALL check code_example_for_linting.py
```

**Hauptmerkmale:**

- ruff funktioniert ähnlich wie pylint oder flake8, ist aber **deutlich** schneller in der Ausführung.
- 

#### Weitere Informationen zu `ruff`

- https://docs.astral.sh/ruff/configuration/#command-line-interface
- https://pythonspeed.com/articles/pylint-flake8-ruff/

### black

Black ist anders als Pylint und Flake8. Es ist nicht nur ein Linter, sondern auch ein Code-Formatter. Anstatt nur stilistische Probleme und Fehler im Code zu melden, formatiert Black den Code automatisch gemäß seinem eigenen Stil, der eng an PEP 8 angelehnt ist.

**Hauptmerkmale:**

- Automatische Codeformatierung.
- Hat eine strikte und unveränderliche Stilrichtlinie, die es "The Blackened" nennt.
- Unterstützt Python 3.6 und höher.

**Vorteile:**

- Keine Entscheidungen bezüglich des Stils: Black entscheidet für Sie.
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

Als nächstes einmal ausprobieren wie `black` als *Formatter* funktioniert (was eigentlich auch der Standard-Modus von `black` ist). Um die Datei nicht zu überschreiben, bitte einmal vorher die Datei kopieren und umbenennen (z.B. in bash mit `mv code_example_for_linting.py code_example_before_black.py`).

Dann

```bash
black code_example_before_black.py
```

#### Mehr Informationen zu `black`

- https://black.readthedocs.io/en/stable/index.html
- https://calmcode.io/black/introduction.html



### Linter (Pylint vs flake8 vs ruff) vs Formatter (black)

Alle drei Linter-Bibliotheken funktionieren sehr gut, `pylint` und `flake8` sind zudem sehr etabliert und bekannt (`ruff` wird da aber wahrscheinlich bald aufholen). Es gibt im Internet zahlreiche Pros/Cons-Debatten. Oft reicht es aus, nach subjektiver Präferenz einen der Linter auszuwählen.

- `flake8` lässt sich über Plugins erweitern, ist aber im einfachen Modus nicht so umfangreich/gründlich wie `pylint` oder `ruff`
- `ruff` ist mit Abstand am schnellsten, das spielt aber erst bei größeren Projekten ein wichtige Rolle.
- `black` ist am komfortabelsten, da es die nötigen Änderungen auch gleich ausführt. In den meisten Fällen kann dies ein strengeres Linting aber nicht ganz ersetzen
- Für umfangreiche Python-Softwareprojekte bietet es sich an, zumindest **einen Linter** zu nutzen. Und, falls gewünscht, einen **Formatter** wie `black` noch davorzuschalten.



### Ausblick

Es gibt noch viele weitere Linter, sowie auch umfangreichere Tools um automatisiert die Code Qualität zu überprüfen bzw. zu verbessern. Zwei erwähnenswerte:

- `mypy` wird genutzt um die korrekte/konsistente Verwendung von Datentypen zu überprüfen
- `SonarCloud` ist ein **sehr** umfangreiches Tool um Code zu beurteilen und potentielle Schachstellen aufzudecken.





## **2. Der erweiterte Entwicklungsprozess**

Bisher (z.B. bei einfacheren Data Science Workflows) konnten wir oft mit recht reduzierten Code-Entwicklungsabläufen arbeiten. Im Prinzip haben wir dabei oft nur iterativ ein Skript (oder Jupyter Notebook) erstellt und solange verändert/verbessert bis es die gewünschten Ergebnisse liefert.

Für umfangreichere Projekte, oder aber auch die Entwicklung eigener Tools oder Software, reicht das in der Regel aber nicht mehr aus!

![fig_development_process_sketch](../images/fig_development_process_sketch.png)

**2.1. Idee**
Jeder Entwicklungsprozess beginnt mit einer Idee oder einem Problem. Es ist wichtig, diese Idee klar zu definieren und zu verstehen, welche Herausforderungen sie mit sich bringt.

**+ Recherche**
Bevor man mit der Programmierung beginnt, sollte man sich einen Überblick über bestehende Lösungen, Datenquellen und Tools verschaffen.

**+ Prototyping**
Hier wird eine erste, oft rudimentäre Lösung entwickelt, um die Machbarkeit zu testen.

**2.2. Code Design**
Ein oft übersehener Schritt, aber entscheidend für den Erfolg des Projekts. Hier wird der Code geplant, Strukturen werden erstellt und mögliche Herausforderungen antizipiert.

**2.3. Implementierung**
Der eigentliche Programmierprozess. Hier wird der zuvor geplante Code umgesetzt.

**2.4. Testen**
Nach der Implementierung muss der Code gründlich getestet werden. Dies stellt sicher, dass er wie erwartet funktioniert und frei von Fehlern ist.

**2.5. Auswertung und Analyse**
Nach dem Testen wird der Code analysiert. Funktioniert alles wie erwartet? Gibt es noch Optimierungsmöglichkeiten?

**2.6. Anwendung und Produktion**
Sobald der Code vollständig getestet und analysiert wurde, kann er in die Produktion übernommen werden.

Das ist keinesfalls ein zwingender Entwicklungsablauf, sondern soll nur eine erste Idee vermitteln, dass der Prozess insgesamt deutlich komplexer ist als ein Jupyter Notebook "zusammenzubasteln".