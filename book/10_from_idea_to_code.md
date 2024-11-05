# From Idea to Code

Beim Programmieren gibt es oft einen sehr starken Impuls "einfach loszulegen", also direkt mit dem Schreiben von Code zu beginnen. Bei kleineren Aufgaben, z.B. Übungsaufgaben, ist das in der Regel auch OK. Sobald es aber um ein größeres Programm geht ist es nicht nur sinnvoll, sondern oft fast unverzichtbar zuerst ein Konzept oder ein Code Design zu erstellen. Gerade bei komplexen Aufgaben, ist es aber gar nicht so leicht sich eine erste Vorstellung davon zu machen wie der Code aufgebaut sein sollte. 

Anstatt uns lange allgemeine Best Practices und Prinzipien anzuschauen, ist das Ziel hier, dass wir anhand eines konkreten Beispiels einmal durchspielen wie wir von einer Idee zum Code kommen können. Wir hangelnd uns dazu aber entlang etablierter Entwurfsphasen entlang. Diese werden wir aber zuerst zumindest kurz einführen müssen um den generellen Ablauf zu verstehen.

Es gibt viele verschiedene Beschreibungen typischer Softwareentwicklungs-Prozesse. Sehr bekannt ist der *Unified Software Development Process* (oder *Unified Process*), von dem es viele Variationen gibt wie z.B. den [*Rational Unified Process*](https://en.wikipedia.org/wiki/Rational_unified_process) oder den [*Agile Unified Process*](https://en.wikipedia.org/wiki/Agile_unified_process). Eine Variante de Unified Process wird auf [geeksforgeeks.org](https://www.geeksforgeeks.org/unified-process-in-ooad/) dargestellt.

Im folgenden halten wir uns nicht an einen spezifischen dieser Prozesse, sondern geben nur eine (an vielen Stellen vereinfachte) Struktur vor mit deren Hilfe sich ein Code Design erstellen lässt.

## Entwicklungsphasen von der Idee zum Code

Absolut, für Data-Science-Studenten mit begrenzter Softwareentwicklungserfahrung ist es wichtig, einen klaren und praktischen Prozess zu vermitteln, der den Übergang von einer Idee zu einem konkreten Softwaredesign erleichtert. Das Ziel ist, ihnen zu helfen, ihre Problemlösungsansätze systematisch in strukturierten Code umzusetzen. Hier ist ein vereinfachter, aber professioneller Workflow, der sich an aktuellen Best Practices in der Softwareentwicklung orientiert:



### Problemdefinition und Anforderungsanalyse

**Ziel**: Klare Verständigung darüber, was gelöst werden muss.

**Aktivitäten**:

- **Definieren des Problems**:
 - Formuliere die Problemstellung in eigenen Worten.
 - Identifiziere die Kernziele und Einschränkungen.
- **Anforderungen sammeln**:
 - Bestimme, welche Eingaben benötigt werden.
 - Definiere die erwarteten Ausgaben oder Ergebnisse.
 - Berücksichtige spezifische Leistungs- oder Benutzerfreundlichkeitsanforderungen.

**Ergebnis**:

- Eine klare, präzise Problemstellung.
- Eine Liste funktionaler Anforderungen (was die Software tun soll).
- Eine Liste nicht-funktionaler Anforderungen (Leistung, Benutzerfreundlichkeit usw.).

### High-Level Lösungsplanung

**Ziel**: Einen allgemeinen Ansatz zur Lösung des Problems skizzieren.

**Aktivitäten**:

- **Lösungen brainstormen**:
 - Überlege mögliche Methoden oder Algorithmen, die das Problem adressieren können.
 - Bewerte die Vor- und Nachteile jedes Ansatzes.
- **Ansatz auswählen**:
 - Wähle den am besten geeigneten Lösungsweg basierend auf Machbarkeit und Anforderungen.

**Ergebnis**:

- Ein ausgewählter Lösungsansatz.
- Begründung für die Auswahl dieses Ansatzes.

### Zerlegung des Problems in Komponenten

**Ziel**: Die Lösung in handhabbare Teile aufteilen.

**Aktivitäten**:

- **Identifizierung der Hauptaufgaben**:
 - Liste die Hauptaufgaben oder Schritte auf, die zur Umsetzung der Lösung erforderlich sind.
 - Gruppiere verwandte Aufgaben zusammen.
- **Definition von Modulen oder Funktionen**:
 - Entscheide für jede Aufgabengruppe, ob sie eine Funktion, Methode oder Klasse sein sollte.
 - Weisen jedem Modul klare Verantwortlichkeiten zu.

**Ergebnis**:

- Eine Liste von Modulen, Funktionen oder Klassen mit zugewiesenen Verantwortlichkeiten.
- Eine hierarchische Struktur, die zeigt, wie die Komponenten interagieren.

### Detailliertes Design mit Flussdiagrammen und Diagrammen

**Ziel**: Die Logik und Struktur der Software visualisieren.

**Aktivitäten**:

- **Erstellung von Flussdiagrammen**:
 - Zeichne Flussdiagramme für komplexe Funktionen oder Prozesse.
 - Verwende standardisierte Symbole, um Operationen, Entscheidungen und Datenfluss darzustellen.
- **Skizzierung von Klassendiagrammen (bei Verwendung von OOP)**:
 - Identifiziere Klassen, ihre Attribute und Methoden.
 - Definiere Beziehungen zwischen Klassen (Vererbung, Assoziation).
- **Design von Datenstrukturen**:
 - Entscheide über die benötigten Datenstrukturen (Listen, Dictionaries, benutzerdefinierte Objekte).
 - Stelle sicher, dass sie mit den Datentypen der Eingaben und Ausgaben übereinstimmen.

**Ergebnis**:

- Detaillierte Flussdiagramme, die die Programmlogik veranschaulichen.
- Klassendiagramme, die die Struktur der Klassen und ihre Beziehungen zeigen.
- Definitionen der Datenstrukturen.

### Definition von Schnittstellen und Interaktionen

**Ziel**: Spezifizieren, wie die verschiedenen Komponenten kommunizieren.

**Aktivitäten**:

- **Schnittstellendesign**:
 - Definiere Funktionssignaturen (Eingabeparameter und Rückgabetypen).
 - Spezifiziere Methodenschnittstellen für Klassen.
- **Interaktionsdiagramme (optional)**:
 - Verwende Sequenzdiagramme, um Interaktionen über die Zeit darzustellen.
 - Kläre die Reihenfolge von Operationen und den Datenfluss zwischen Komponenten.

**Ergebnis**:

- Gut definierte Schnittstellen für alle Module.
- Klare Verständnis der Komponenteninteraktionen.

### Implementierungsplanung

**Ziel**: Sich mit einem klaren Fahrplan auf die Codierungsphase vorbereiten.

**Aktivitäten**:

- **Priorisierung der Entwicklungstasks**:
 - Ordne Tasks basierend auf Abhängigkeiten und Wichtigkeit.
 - Setze Meilensteine für schrittweisen Fortschritt.
- **Einrichtung von Tools und Umgebung**:
 - Wähle die Programmiersprache und Bibliotheken aus.
 - Richte Entwicklungsumgebungen und Versionskontrollsysteme ein.
- **Teststrategie**:
 - Plane, wie jede Komponente getestet werden soll (Unit-Tests, Integrationstests).
 - Entscheide über Testfälle zur Validierung der Funktionalität.

**Ergebnis**:

- Ein Schritt-für-Schritt-Implementierungsplan.
- Entwicklungsumgebung bereit für die Codierung.
- Erste Entwürfe des Testplans.

Überprüfung und Feedback

**Ziel**: Das Design vor der Implementierung validieren.

**Aktivitäten**:

- **Peer Review**:
 - Präsentiere das Design Kommilitonen oder Dozenten.
 - Diskutiere mögliche Probleme oder Verbesserungen.
- **Verfeinerung**:
 - Integriere Feedback in das Design.
 - Kläre alle unklaren Teile des Designs.

**Ergebnis**:

- Verbessertes und validiertes Design.
- Erhöhtes Vertrauen in den geplanten Ansatz.

---

### Erläuterung und Ausrichtung an Best Practices

Dieser vereinfachte Prozess spiegelt wesentliche Phasen der professionellen Softwareentwicklung wider, ist aber für Software-Development-Anfänger angepasst:

- **Betont das Verständnis**: Beginnend mit der Problemdefinition wird ein tiefes Verständnis sichergestellt, bevor mit dem Codieren begonnen wird.
- **Modulares Design**: Die Aufteilung des Problems in Komponenten entspricht dem Prinzip der Modularität und verbessert die Wartbarkeit des Codes.
- **Visualisierungstools**: Die Verwendung von Flussdiagrammen und Diagrammen hilft bei der Planung und Kommunikation komplexer Logik.
- **Iteratives Feedback**: Die Einbindung von Überprüfungsphasen spiegelt agile Praktiken wider und fördert Anpassungsfähigkeit und kontinuierliche Verbesserung.
- **Vorbereitung auf die Implementierung**: Vorausplanung ebnet den Weg für effizientes Codieren und Testen.

---

### Zusätzliche Tipps

- **Halte es einfach**: Fokussiere dich auf Klarheit statt Komplexität. Einfache Designs sind leichter zu implementieren und zu debuggen.
- **Dokumentiere dein Design**: Selbst informelle Notizen und Skizzen können während des Codierens wertvoll sein.
- **Bleibe flexibel**: Sei bereit, dein Design anzupassen, wenn du während der Implementierung mehr erfährst.
- **Suche Zusammenarbeit**: Die besten Code Designs entstehen oft über Austausch und Zusammenarbeit.

---

## Praktisches Python Beispiel

Wenden wir diesen Prozess auf ein konkretes Projekt an: **Erstellung eines ASCII-Scatterplots**

### Problemdefinition und Anforderungsanalyse

- **Problem**: Entwicklung eines Programms, das x- und y-Koordinaten aus einer CSV-Datei lädt und ein Scatterplot als ASCII-Grafik darstellt.
- **Funktionale Anforderungen**:
  - Laden von Daten aus einer CSV-Datei mit "x" und "y" Spalten.
  - Skalierung der Koordinaten, um sie an ein ASCII-Raster anzupassen.
  - Darstellung der Datenpunkte im Raster mit einem spezifischen Zeichen.
  - Hinzufügen von Achsen zum Raster.
- **Nicht-funktionale Anforderungen**:
  - Anpassbare Rastergröße und Zeichen.
  - Effiziente Verarbeitung und Skalierung der Daten.
  - Klare und lesbare Ausgabe auf der Konsole.

### High-Level Lösungsplanung

- **Ansatz**: Implementierung einer Python-Klasse `AsciiScatterPlot`, die alle erforderlichen Funktionen kapselt:
  - Laden und Validieren der CSV-Daten.
  - Skalierung der Koordinaten entsprechend der Rastergröße und des Seitenverhältnisses.
  - Erstellung des Rasters und Hinzufügen von Achsen.
  - Plotten der Datenpunkte auf dem Raster.
  - Ausgabe des Rasters auf der Konsole.

### Zerlegung des Problems in Komponenten

- **Module/Funktionen**:
  - **Initialisierung**: `__init__(char, width, height, aspect_ratio)`
    - Initialisiert das Raster und die Parameter.
  - **Datenladen**: `load_csv(filepath)`
    - Lädt die CSV-Datei und überprüft das Vorhandensein von "x" und "y" Spalten.
  - **Koordinatenskalierung**: `scale_coordinates(data)`
    - Skaliert die Koordinaten, um sie an die Rasterdimensionen anzupassen.
  - **Achsen hinzufügen**: `add_axes()`
    - Fügt x- und y-Achsen zum Raster hinzu.
  - **Punkte plotten**: `plot_points(scaled_coords)`
    - Platziert die Datenpunkte auf dem Raster.
  - **Anzeigen**: `display()`
    - Gibt das Raster auf der Konsole aus.
  - **Gesamtprozess**: `plot_from_csv(filepath)`
    - Führt alle Schritte aus, um das Scatterplot zu erstellen.

### Detailliertes Design mit Flussdiagrammen und Diagrammen

- **Klassendiagramm**:

  ```
  +------------------------+
  |     AsciiScatterPlot   |
  +------------------------+
  | - char: str            |
  | - width: int           |
  | - height: int          |
  | - aspect_ratio: float  |
  | - grid: list           |
  +------------------------+
  | + __init__(...)        |
  | + load_csv(filepath)   |
  | + scale_coordinates(data)|
  | + add_axes()           |
  | + plot_points(scaled_coords)|
  | + display()            |
  | + plot_from_csv(filepath)|
  +------------------------+
  ```

- **Flussdiagramm für `plot_from_csv(filepath)`**:

  ```
  Start
    |
    v
  load_csv(filepath)
    |
    v
  scale_coordinates(data)
    |
    v
  add_axes()
    |
    v
  plot_points(scaled_coords)
    |
    v
  display()
    |
    v
  Ende
  ```

- **Datenstrukturen**:
  - **`data`**: Pandas DataFrame mit den Originalkoordinaten.
  - **`scaled_coords`**: Pandas DataFrame mit den skalierten Koordinaten.
  - **`grid`**: 2D-Liste, die das ASCII-Raster repräsentiert.

### Definition von Schnittstellen und Interaktionen

- **Methodenschnittstellen**:
  - `__init__(char="*", width=50, height=50, aspect_ratio=2.0)`
    - Initialisiert das Raster mit den gegebenen Parametern.
  - `load_csv(filepath) -> DataFrame`
    - Lädt die CSV-Datei und gibt die "x" und "y" Daten zurück.
  - `scale_coordinates(data) -> DataFrame`
    - Skaliert die Daten und gibt die skalierten Koordinaten zurück.
  - `add_axes()`
    - Fügt Achsen zum Raster hinzu.
  - `plot_points(scaled_coords)`
    - Plottet die Punkte auf dem Raster.
  - `display()`
    - Gibt das Raster auf der Konsole aus.
  - `plot_from_csv(filepath)`
    - Führt den gesamten Prozess aus.

- **Interaktionen**:
  - Die Methode `plot_from_csv` orchestriert den Ablauf, indem sie die anderen Methoden aufruft.
  - Daten fließen von `load_csv` zu `scale_coordinates` zu `plot_points`.

### Implementierungsplanung

In vielen Fällen, besonders bei Projekten die im Team bearbeitet werden kann (und soll) die Implementierungsplanung natürlich kein streng linearer Ablaufplan sein. Die folgende Reihenfolge ist an vielen Stellen beliebig, wichtig daran ist vor allem kleinschrittige Aufgaben zu definieren und im Team zu verteilen und zu bearbeiten.

- **Entwicklungsschritte**:
  1. Implementiere die Initialisierung und die Erstellung des leeren Rasters.
  2. Implementiere `load_csv`, um die Daten zu laden und zu validieren.
  3. Implementiere `scale_coordinates`, um die Daten an die Rastergröße anzupassen.
  4. Implementiere `add_axes`, um die Achsen zum Raster hinzuzufügen.
  5. Implementiere `plot_points`, um die Datenpunkte zu platzieren.
  6. Implementiere `display`, um das Raster auszugeben.
  7. Teste jede Methode einzeln mit Beispieldaten.
  8. Führe alles in `plot_from_csv` zusammen und teste den gesamten Ablauf.

- **Tools**:
  - Programmiersprache: Python
  - Bibliotheken: Pandas für Datenmanipulation
  - Entwicklungsumgebung: Jupyter Notebook oder IDE
  - Versionskontrolle: Git (optional)

- **Teststrategie**:
  - Erstelle kleine CSV-Dateien mit bekannten Daten zum Testen.
  - Überprüfe die Ausgabe visuell, um sicherzustellen, dass das Scatterplot korrekt dargestellt wird.
  - Teste Randfälle, z.B. leere Daten, sehr große oder kleine Werte.

### Überprüfung und Feedback

- **Peer Review**:
  - Präsentation des Designs und Codes an Kommilitonen oder den Dozenten.
  - Einholen von Feedback zur Benutzerfreundlichkeit und Codequalität.
- **Verfeinerung**:
  - Verbesserungen basierend auf Feedback implementieren, z.B. Fehlerbehandlung, zusätzliche Funktionen (z.B. unterschiedliche Zeichen für verschiedene Datenpunkte).

### Ausblick

Wir kommen in folgenden Teilen zu weiteren Möglichkeiten die die eigentliche Implementierung begleiten können wie z.B. Testing.

1. **Anforderungsanalyse**
   - **Ziel**: Verständnis dafür gewinnen, was das Programm erreichen soll.
   - **Schritte**: Anforderungen und Zielvorgaben klären, häufige Anwendungsfälle (*Use cases*) durchdenken und dokumentieren.
2. **Konzeptionelles Modell**

   - **Ziel**: Ein Modell entwickeln, das die Kernkomponenten und deren Beziehungen skizziert.
   - **Schritte**: Hauptelemente und deren Verantwortlichkeiten identifizieren; oft durch Diagramme unterstützt.
3. **Zerlegung und Abstraktion**

   - **Ziel**: Das Problem in kleinere, überschaubare Teile aufteilen und logisch strukturieren.
   - **Schritte**: Jedes Teilmodul für eine bestimmte Aufgabe definieren, z. B. Daten laden, verarbeiten und darstellen.
5. **Pseudocode und Flussdiagramme**
   - **Ziel**: Den Ablauf des Programms skizzieren, ohne sich um den eigentlichen Code zu kümmern.
   - **Schritte**: Pseudocode schreiben und/oder Flussdiagramme erstellen, um die Logik des Programms klar darzustellen.
6. **Prototyping und Feedback**
   - **Ziel**: Eine erste, einfache Version des Programms entwickeln und testen.
   - **Schritte**: Kernfunktionen implementieren, testen und auf Basis des Feedbacks weiter verbessern.
7. **Iterative Verfeinerung**
   - **Ziel**: Das Programm kontinuierlich verbessern und verfeinern.
   - **Schritte**: Rückmeldungen und Tests nutzen, um die Struktur, Logik und Benutzerfreundlichkeit des Programms zu optimieren.

Diese sechs Phasen sind nur eine Möglichkeit den Prozess einzuteilen. Außerdem darf man sich das Ganze nicht als einen streng linearen Prozess vorstellen. Viele der Phasen können auch parallel in Angriff genommen werden, oder es häufig auch Gründe wieder zu einer "früheren" Phase zurückzukehren, z.B. weil an einer Stelle Unstimmigkeiten oder Unvereinbarkeiten entdeckt werden.

## Building an ASCII Scatter Plot Tool in Python

**Problemstellung**

Wir wollen ein Python-Tool erstellen, das:

1. x- und y-Koordinaten aus einer CSV-Datei lädt.
2. Ein ASCII-Scatter-Plot in der Konsole anzeigt, wobei ein Zeichen unserer Wahl verwendet wird 
   (z. B. "*", "x", "o").
3. Einfache x- und y-Achsen hinzufügt, um das Diagramm lesbarer zu machen.

---

**Phasen der Entwicklung**

---

### Endprodukt

Hier eine mögliche Lösung. Der folgende Code kann jede CSV-Datei mit `x, y`-Koordinaten laden und ein sauberes ASCII-Scatterplot mit klaren Achsen in der Konsole darstellen.


```python
import pandas as pd


class AsciiScatterPlot:
    def __init__(self, char="*", width=50, height=50, aspect_ratio=2.0):
        """
        Initializes the ASCII scatter plot with specified character, grid dimensions, and aspect ratio.
        - char: The character used to represent each point.
        - width: Width of the ASCII grid.
        - height: Height of the ASCII grid.
        - aspect_ratio: Adjusts scaling for the difference in character dimensions.
        """
        self.char = char
        self.width = int(width * aspect_ratio)
        self.height = height
        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]
        self.add_axes()

    def load_csv(self, filepath):
        """
        Loads CSV data with columns x and y.
        """
        data = pd.read_csv(filepath)
        if not all(col in data.columns for col in ["x", "y"]):
            raise ValueError("CSV file must contain 'x' and 'y' columns.")
        return data[["x", "y"]]

    def scale_coordinates(self, data):
        """
        Scales coordinates to fit the ASCII grid.
        """
        x_min, x_max = data["x"].min(), data["x"].max()
        y_min, y_max = data["y"].min(), data["y"].max()

        # Scale x and y to the grid dimensions
        data["x_scaled"] = ((data["x"] - x_min) / (x_max - x_min)) * (self.width - 1)
        data["y_scaled"] = ((data["y"] - y_min) / (y_max - y_min)) * (self.height - 1)

        # Rounding coordinates to nearest integer grid point and clamping to grid boundaries
        data["x_scaled"] = data["x_scaled"].round().clip(0, self.width - 1).astype(int)
        data["y_scaled"] = data["y_scaled"].round().clip(0, self.height - 1).astype(int)
        
        return data[["x_scaled", "y_scaled"]]

    def add_axes(self):
        """
        Adds x and y axes to the grid.
        """
        # X-axis
        for x in range(self.width):
            self.grid[self.height - 1][x] = "-"

        # Y-axis
        for y in range(self.height):
            self.grid[y][0] = "|"

        # Origin point
        self.grid[self.height - 1][0] = "+"

    def plot_points(self, scaled_coords):
        """
        Maps scaled coordinates onto the ASCII grid.
        """
        for _, (x, y) in scaled_coords.iterrows():
            # Invert y to plot from top to bottom
            self.grid[self.height - 1 - y][x] = self.char

    def display(self):
        """
        Prints the ASCII grid to the console.
        """
        for row in self.grid:
            print("".join(row))

    def plot_from_csv(self, filepath):
        """
        High-level function to load, scale, plot, and display the scatter plot from a CSV file.
        """
        data = self.load_csv(filepath)
        scaled_coords = self.scale_coordinates(data)
        self.plot_points(scaled_coords)
        self.display()

# Usage example
plotter = AsciiScatterPlot(char="*", width=30, height=30, aspect_ratio=2.0)

# Assuming 'data.csv' contains x, y coordinates
plotter.plot_from_csv("data.csv")
```
