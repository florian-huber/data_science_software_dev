## Code Design & Grundlagen der Objektorientierten Programmierung (OOP)

### Teil 1: Wiederholung der OOP-Grundlagen

#### 1. Klasse vs. Instanz

In der objektorientierten Programmierung (OOP) sind **Klassen** und **Instanzen** zwei grundlegende Konzepte, die es uns ermöglichen, Code strukturiert und modular zu organisieren.

- **Klasse**: Eine Vorlage oder ein Bauplan zur Erstellung von Objekten. Eine Klasse definiert eine Reihe von Attributen und Methoden, die die erstellten Objekte haben werden.
- **Instanz**: Ein spezifisches Objekt, das aus einer Klasse erstellt wurde. Jede Instanz hat ihre eigenen Daten, basierend auf der Struktur der Klasse.

Stellen wir uns zur Verdeutlichung eine Klasse namens `Bike` vor. Diese Klasse definiert die Struktur und Eigenschaften eines Fahrrads im Allgemeinen, wie z. B. die Farbe, das Modell und Methoden wie `fahren()` und `stoppen()`. Die Klasse selbst ist jedoch kein Fahrrad, das man fahren kann. Stattdessen erstellt man **Instanzen** der `Bike`-Klasse—also individuelle Fahrräder mit spezifischen Attributen, wie ein rotes Mountainbike oder ein blaues Rennrad.

```python
# Definition einer einfachen Klasse in Python
class Bike:
    # Klassenattribut
    wheels = 2  # Alle Fahrräder haben 2 Räder
    
    # Konstruktor-Methode
    def __init__(self, color, model):
        # Instanzattribute
        self.color = color
        self.model = model

# Erstellen von Instanzen der Bike-Klasse
bike1 = Bike("rot", "Mountainbike")
bike2 = Bike("blau", "Rennrad")

# Zugriff auf Instanzattribute
print(bike1.color)  # Ausgabe: rot
print(bike2.color)  # Ausgabe: blau

# Zugriff auf ein Klassenattribut
print(Bike.wheels)  # Ausgabe: 2
```

#### Wichtige Punkte:
- `Bike` ist die **Klasse**. Sie stellt die Struktur bereit: `wheels`, `color`, `model`.
- `bike1` und `bike2` sind **Instanzen** der `Bike`-Klasse, jede mit eigenen `color`- und `model`-Attributen.
- `wheels` ist ein **Klassenattribut**, das von allen Instanzen geteilt wird. Eine Änderung in der Klasse würde sich auf alle Instanzen auswirken.

#### 2. Klasse in Python

Eine **Klasse** in Python wird mit dem Schlüsselwort `class` definiert. Sie enthält normalerweise eine Konstruktor-Methode, `__init__`, die aufgerufen wird, wenn eine neue Instanz erstellt wird. Der Konstruktor ermöglicht es, initiale Attribute für jede Instanz festzulegen.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name  # Instanzattribut
        self.species = species  # Instanzattribut

# Erstellen von Instanzen der Animal-Klasse
animal1 = Animal("Leo", "Löwe")
animal2 = Animal("Bella", "Elefant")

print(animal1.name)  # Ausgabe: Leo
print(animal2.species)  # Ausgabe: Elefant
```

In diesem Beispiel:
- `name` und `species` sind **Instanzattribute**—spezifisch für jede Instanz (`animal1` und `animal2`).
- Jede Instanz hat eigene Daten, aber beide teilen die Struktur der `Animal`-Klasse.

#### 3. Methoden und Attribute

**Attribute** sind die Daten, die in einer Instanz gespeichert sind, während **Methoden** Funktionen sind, die in einer Klasse definiert werden und auf Instanzen der Klasse operieren.

Es gibt zwei Hauptarten von Attributen:
- **Instanzattribute**: Spezifisch für jede Instanz. Sie werden im `__init__`-Methodenblock über `self` definiert.
- **Klassenattribute**: Werden von allen Instanzen der Klasse geteilt.

**Methoden** sind Funktionen, die in einer Klasse definiert werden und normalerweise verwendet werden, um Instanzdaten zu ändern oder Aktionen auszuführen, die mit der Klasse in Verbindung stehen.

```python
class Circle:
    # Klassenattribut
    pi = 3.1415
    
    def __init__(self, radius):
        # Instanzattribut
        self.radius = radius
    
    # Methode zur Berechnung der Fläche
    def calculate_area(self):
        return Circle.pi * (self.radius ** 2)
    
    # Methode zur Berechnung des Umfangs
    def calculate_circumference(self):
        return 2 * Circle.pi * self.radius

# Erstellen einer Instanz der Circle-Klasse
circle1 = Circle(5)

# Aufruf von Methoden auf der Instanz
print(circle1.calculate_area())
print(circle1.calculate_circumference())
```

In diesem Beispiel:
- `pi` ist ein **Klassenattribut**, das für alle Kreise gleich ist.
- `radius` ist ein **Instanzattribut**, das bei der Initialisierung festgelegt wird.
- `calculate_area` und `calculate_circumference` sind **Methoden**, die auf den Daten der Instanz arbeiten und sowohl Klassen- als auch Instanzattribute verwenden.
