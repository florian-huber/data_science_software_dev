### Teil 2: Fortgeschrittene Konzepte in der OOP

#### 1. Getter und Setter

In Python ermöglichen **Getter** und **Setter** den kontrollierten Zugriff auf Attribute eines Objekts. Dies ist besonders nützlich, wenn man sicherstellen möchte, dass nur gültige Werte zugewiesen werden. Python bietet dafür das Konzept der `@property`-Dekoratoren.

Ein Beispiel mit einer `Elevator`-Klasse, die das aktuelle Stockwerk (`level`) speichert:

```python
class Elevator:
    def __init__(self, level=0):
        self._level = level  # Internes Attribut

    # Getter-Methode mit @property
    @property
    def level(self):
        return self._level

    # Setter-Methode mit @level.setter
    @level.setter
    def level(self, new_level):
        if not isinstance(new_level, int):
            raise ValueError("Value must be an integer")
        self._level = new_level
```

In diesem Beispiel:
- Der **Getter** gibt den Wert von `self._level` zurück.
- Der **Setter** stellt sicher, dass `new_level` ein Integer ist, bevor es dem Attribut zugewiesen wird. Andernfalls wird eine Fehlermeldung ausgegeben.

#### 2. Dekoratoren

**Dekoratoren** sind spezielle Funktionen, die andere Funktionen oder Methoden verändern. In OOP werden sie oft für Getter und Setter verwendet, aber sie können auch zur Modifikation des Verhaltens anderer Methoden dienen. Der `@property`-Dekorator verwandelt eine Methode in ein Attribut, und der `@level.setter`-Dekorator definiert eine zugehörige Setter-Methode.

Dekoratoren sind ein wichtiges Konzept in Python, da sie eine elegante Möglichkeit bieten, Code zu wiederverwenden und die Funktionalität zu erweitern, ohne die ursprüngliche Funktion oder Methode zu verändern.

#### 3. Private und versteckte Attribute

In Python wird durch das Präfix `_` oder `__` angezeigt, dass ein Attribut oder eine Methode **privat** oder **versteckt** ist, d.h., sie sollen nur innerhalb der Klasse verwendet werden.

- **Einfaches Unterstrich-Präfix** (`_level`): Eine Konvention, die darauf hinweist, dass ein Attribut "privat" ist. Es kann immer noch von außerhalb der Klasse zugegriffen werden, aber die Konvention zeigt an, dass dies vermieden werden sollte.
- **Doppel-Unterstrich-Präfix** (`__level`): Dies führt zu einer Namensänderung (Name Mangling), sodass das Attribut schwerer zugänglich ist und nicht so leicht versehentlich überschrieben wird.

```python
class Secret:
    def __init__(self):
        self._hidden = "Nur zur internen Nutzung"
        self.__very_hidden = "Schwer zugänglich"

secret = Secret()
print(secret._hidden)           # Möglich, aber sollte vermieden werden
# print(secret.__very_hidden)    # Fehler: AttributeError
print(secret._Secret__very_hidden)  # Zugriff durch Namensänderung möglich
```

#### 4. Magische Methoden (Dunder-Methoden)

**Magische Methoden** (auch **Dunder-Methoden** genannt, da sie durch doppelte Unterstriche umgeben sind, wie `__init__`, `__str__`, etc.) erlauben es, das Verhalten von Python-Operatoren und Funktionen für benutzerdefinierte Klassen zu definieren.

Einige häufige Magische Methoden:
- `__init__`: Konstruktor, initialisiert eine neue Instanz.
- `__str__`: Gibt eine benutzerfreundliche String-Darstellung eines Objekts zurück.
- `__len__`: Erlaubt die Nutzung der `len()`-Funktion.
- `__getitem__`: Ermöglicht den Zugriff auf Elemente wie bei einer Liste.

Beispiel:

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' with {self.pages} pages"

    def __len__(self):
        return self.pages

book = Book("Python für Einsteiger", 300)
print(book)
print(len(book))
```

Hier definieren wir `__str__` für die String-Darstellung und `__len__`, um die Anzahl der Seiten anzugeben.

#### 5. Ausblick: OOP vs. Funktionale Programmierung

Python unterstützt sowohl die **objektorientierte** als auch die **funktionale Programmierung**. Beide Ansätze haben ihre Stärken, und es gibt keine allgemeingültige Antwort auf die Frage, welcher Ansatz besser ist. Oft hängt es von der Problemstellung ab:

- **OOP** eignet sich gut für umfangreiche, komplexe Programme, bei denen es wichtig ist, Daten und Verhalten zu kapseln.
- **Funktionale Programmierung** ist oft einfacher für Programme, die stateless sind und auf immutabler Datenverarbeitung basieren.

Beide Paradigmen können in Python kombiniert werden, um robuste und gut strukturierte Lösungen zu entwickeln.

#### Gute Gründe für die Nutzung von OOP:

Bisher war die Antwort auf die Frage warum wir OOP nutzen sollten ehrlicherweise oft: "Weil ich OOP lernen will/muss...".

Besser in der Praxis:
- Wenn es den Code einfacher und verständlicher macht.
- Wenn das Code Design stark auf OOP hinweist.
- Vor allem bei umfangreicheren Programmen.
- Wenn die angestrebte Nutzung (z. B. API-Entwicklung) OOP verlangt.
