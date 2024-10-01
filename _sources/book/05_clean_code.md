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

## Die Bedeutung von „besserem“ Code

### Was ist „besser“?
„Besser“ ist ein relatives Konzept. In der Programmierung bezieht es sich oft darauf, wie effizient, lesbar und wartbar ein Code ist. Es ist wichtig zu betonen, dass "besser" nicht immer "perfekt" bedeutet. In der echten Welt ist es oft nicht notwendig (meistens auch gar nicht möglich) einen perfekten Code zu schreiben. Stattdessen sollte das Ziel sein, den Code kontinuierlich zu verbessern wo es sinnvoll ist und so einen Code zu erstellen, der wiederholbar und zuverlässig funktioniert.

### Warum besserer Code wichtig ist

Besserer Code ist aus mehreren Gründen wichtig:

- **Zuverlässigkeit:** Code, der den *Best Practices* folgt, hat tendenziell weniger Fehler und funktioniert vorhersehbarer.
- **Wartbarkeit:** Es ist einfacher, Code zu aktualisieren und zu verbessern, wenn er gut organisiert und dokumentiert ist.
- **Zusammenarbeit:** In Teams ist es wesentlich einfacher, mit Code zu arbeiten, der den gemeinsamen Standards folgt.

### Der Weg zu „besserem“ Code: Clean Code

Während es viele Methoden gibt, um Code zu verbessern, ist eine der effektivsten und anerkanntesten Methoden die Anwendung von "Clean Code" Prinzipien. "Clean Code" bietet nicht nur eine klare Struktur und Lesbarkeit, sondern stellt auch sicher, dass der Code nachhaltig, wartbar und effizient bleibt. Im nächsten Abschnitt werden wir uns genauer mit der Definition, den Vorteilen und den Prinzipien von Clean Code beschäftigen und wie diese in der Python-Programmierung umgesetzt werden können.

## Clean Code - Grundlagen

### Was ist Clean Code?
Clean Code ist ein Code, der leicht zu lesen, zu verstehen und zu warten ist. Es geht nicht nur darum, wie der Code aussieht, sondern auch darum, wie er strukturiert ist.

Clean Code ist aber nicht nur ein Ziel, sondern auch eine Methode. Es gibt bestimmte Prinzipien und Best Practices, die Entwickler befolgen können, um ihren Code sauberer und effizienter zu gestalten.

Prinzipiell gilt, das Clean Code kein Selbstzweck ist, sondern sich auf viele Aspekte bei der Softwareentwicklung sehr positiv auswirkt, z.B.:

- **Lesbarkeit:** Ein sauberer Code ist einfacher zu lesen und zu verstehen.
- **Wartbarkeit:** Ein sauberer Code ist einfacher zu warten und zu erweitern.
- **Fehlerreduktion**: Clean Code führt zu weniger Missverständnissen und damit auch zu weniger Fehlern. Wenn der Code klar und logisch strukturiert ist, sinkt die Wahrscheinlichkeit, dass unbemerkte Fehler entstehen.
- **Produktivität:** Mit sauberem Code können Entwickler schneller und effizienter arbeiten.

**Eingangsbeispiele und ihre Bedeutung**
Zur Verdeutlichung der Prinzipien von Clean Code werden im Laufe des Kapitels verschiedene Codebeispiele analysiert und diskutiert.

```python
animals = ['dog', 'cat', 'elephant']

# vs

animals= [    'dog',   'cat',"elephant"   ]
```

### Clean Code – Wer entscheidet über den Stil?

Ein häufig gestellte Frage ist: Wer entscheidet eigentlich, wie der Code aussehen sollte? Warum kann nicht jeder seinen eigenen Stil entwickeln?

Die Antwort lautet: Für den **Python-Interpreter** ist der Stil zwar nebensächlich, aber für Menschen, die den Code lesen, ist er entscheidend. Die Lesbarkeit steht im Vordergrund, denn Code wird häufiger gelesen als geschrieben.

- **Ziel 1**: Der Stil sollte die Lesbarkeit maximieren.
- **Ziel 2**: Code sollte global verständlich sein, nicht nur für den Autor.

In der Praxis wird diese Frage oft über sogenannte *Style Guides* adressiert.

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
