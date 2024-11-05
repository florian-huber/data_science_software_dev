# From Idea to Code

Beim Programmieren gibt es oft einen sehr starken Impuls "einfach loszulegen", also direkt mit dem Schreiben von Code zu beginnen. Bei kleineren Aufgaben, z.B. Übungsaufgaben, ist das in der Regel auch OK. Sobald es aber um ein größeres Programm geht ist es nicht nur sinnvoll, sondern oft fast unverzichtbar zuerst ein Konzept oder ein Code Design zu erstellen. Gerade bei komplexen Aufgaben, ist es aber gar nicht so leicht sich eine erste Vorstellung davon zu machen wie der Code aufgebaut sein sollte. 

Anstatt allgemeine Best Practices und Prinzipien anzuschauen, ist das Ziel hier, dass wir anhand eines konkreten Beispiels einmal durchspielen wie wir von einer Idee zum Code kommen können. Wir hangelnd uns dazu aber entlang etablierter Entwurfsphasen entlang. Diese werden jetzt zuerst sehr knapp eingeführt.
Hier ist eine kurze Übersicht der allgemeinen Entwicklungsphasen, die in einer Einführung verwendet werden könnte:

## Entwicklungsphasen von der Idee zum Code

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

Wir gehen die einzelnen Phasen Schritt für Schritt durch und wenden sie auf unser ASCII-Scatterplot-Tool an.

### Phase 1: Anforderungsanalyse & Anwendungsfälle

#### **Ziele**:
- **Hauptziel**: Visualisierung von `x, y`-Koordinaten in einem einfachen ASCII-Scatterplotformat.
- **Detaillierte Anforderungen**:
  - Daten aus einer CSV-Datei mit den Spalten `x` und `y` laden.
  - Koordinaten auf einem ASCII-Raster skalieren und anzeigen.
  - Anpassbare Zeichen zur Darstellung der Punkte verwenden.
  - Das nicht-quadratische Seitenverhältnis der Zeichen berücksichtigen.
  - x- und y-Achsen hinzufügen, um die Lesbarkeit zu verbessern.

#### **Anwendungsfall**:
Angenommen, ein Data Scientist hat eine CSV-Datei mit `x, y`-Koordinaten und benötigt eine schnelle Möglichkeit, die Daten zu visualisieren. Dieses ASCII-Diagramm bietet eine einfache, textbasierte Lösung, die besonders in Umgebungen ohne grafische Tools nützlich ist.

---

### Phase 2: Konzeptionelles Modell

**Hauptkomponenten**:
- **CSV-Leser**: Lädt `x, y`-Daten aus einer Datei und überprüft, ob diese Spalten vorhanden sind.
- **Skalierer**: Passt die Koordinatenwerte an, um sie in ein ASCII-Raster einer bestimmten Größe einzufügen. Dabei wird das Seitenverhältnis des Zeichens berücksichtigt, um Verzerrungen zu vermeiden.
- **Plotter**: Ordnet jede Koordinate der richtigen Position im ASCII-Raster zu.
- **Anzeigemodul**: Gibt das fertige ASCII-Diagramm in der Konsole aus.

---

### Phase 3: Zerlegung & Abstraktion

Jede Funktion in der Klasse erfüllt eine spezifische Aufgabe:

- **`load_csv()`**: Diese Funktion verwendet `pandas`, um die CSV-Datei zu laden und sicherzustellen, dass die `x`- und `y`-Spalten vorhanden sind.
- **`scale_coordinates()`**: Passt die `x`- und `y`-Werte so an, dass sie in die Rasterdimensionen passen. Die Skalierung hält die Koordinaten proportional zum Raster, während das Seitenverhältnis sicherstellt, dass jeder Punkt an der richtigen Stelle angezeigt wird.
- **`plot_points()`**: Diese Methode ordnet die skalierten Koordinaten dem Raster zu, wobei das angegebene Zeichen für jeden Punkt verwendet wird.
- **`add_axes()`**: Diese Funktion fügt einfache x- und y-Achsen hinzu, um das Diagramm besser interpretierbar zu machen.
- **`display()`**: Gibt das Raster Zeile für Zeile in der Konsole aus und simuliert so ein 2D-Scatterplot im ASCII-Format.

Wir können in dieser Phase, zumindest für ein so recht einfaches Problem, auch schon unsere Klassen/Methoden/Attribute (für OOP) oder Funktionen (für Functional Programming) weiter definieren.

**Klassenstruktur**:
Wir entscheiden uns, diese Komponenten in einer `AsciiScatterPlot`-Klasse zusammenzufassen. Diese Klasse verwaltet alle Schritte an einem Ort und ermöglicht eine einfache Anpassung und Wiederverwendung. Hier ist ein Überblick:

- **Attribute**:
  - `char` – Das Zeichen für die Darstellung der Punkte.
  - `width`, `height` – Dimensionen des ASCII-Rasters.
  - `aspect_ratio` – Passt die Skalierung an, um Unterschiede in der Höhe/Breite der Zeichen zu berücksichtigen.
  - `grid` – Eine 2D-Liste, die das ASCII-Raster darstellt.
- **Methoden**:
  - `load_csv()` – Lädt CSV-Daten und überprüft `x, y`-Spalten.
  - `scale_coordinates()` – Skaliert die Koordinaten so, dass sie ins Raster passen.
  - `plot_points()` – Ordnet die skalierten Koordinaten im Raster an.
  - `add_axes()` – Fügt x- und y-Achsen zum Raster hinzu.
  - `display()` – Gibt das fertige Raster in der Konsole aus.
  - `plot_from_csv()` – Hauptfunktion, um alle Schritte in Sequenz auszuführen.

### Phase 4: Pseudocode und Flussdiagramme

**Pseudocode**:
```plaintext
1. Initialisiere AsciiScatterPlot mit dem angegebenen Zeichen, den Rastermaßen und dem Seitenverhältnis.
2. Lade die CSV-Datei mit x-, y-Koordinaten mit load_csv().
3. Skaliere die Koordinaten so, dass sie ins ASCII-Raster passen, mit scale_coordinates().
4. Füge x- und y-Achsen zum Raster hinzu mit add_axes().
5. Ordne die skalierten Koordinaten im Raster an mit plot_points().
6. Gib das Raster in der Konsole aus mit display().
```

**Flussdiagramm**:

1. **Start** → **Klasse initialisieren** → **CSV laden**
2. Wenn `x, y`-Spalten vorhanden sind:
   - → **Koordinaten skalieren**
   - → **Achsen hinzufügen**
   - → **Koordinaten ins Raster einfügen**
   - → **Raster anzeigen**
   - → **Ende**
3. Andernfalls:
   - **Fehler**: Ungültige CSV-Datei

---

### Phase 5: Prototyping und Feedback

- Wir starten mit einem Prototyp, der die CSV-Datei lädt und die Koordinaten skaliert.
- In der ersten Version implementieren wir keine Anpassungen des Seitenverhältnisses oder Achsen. Stattdessen konzentrieren wir uns darauf, die Punkte direkt zu laden, zu skalieren und anzuzeigen.
- Nach dem Testen der Grundfunktionalität fügen wir die Behandlung des Seitenverhältnisses und Achsen hinzu, um einen verfeinerten Prototyp zu erstellen.

### Phase 6: Iterative Verbesserung

Verfeinerungen umfassen:

1. **Seitenverhältnis**: Die `width` wird basierend auf dem angegebenen `aspect_ratio` angepasst, um das Erscheinungsbild des Diagramms zu verbessern.
2. **Achsen**: Fügen Sie x- und y-Achsen hinzu, um das Diagramm leichter interpretierbar zu machen.
3. **Vereinfachungen**: Wir optimieren den Code, indem wir `clip` und `round` in den Skalierungsprozess einbinden, um saubere, begrenzte Koordinaten ohne komplexe Überprüfungen zu gewährleisten.

---

### Endprodukt

Der resultierende Code ist jetzt einsatzbereit und getestet. Er kann jede CSV-Datei mit `x, y`-Koordinaten laden und ein sauberes ASCII-Scatterplot mit klaren Achsen in der Konsole darstellen.

Hier eine mögliche Lösung.

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


---

### Zusammenfassung der Lektion

1. **Von der Idee zum Code**: Wir haben gezeigt, wie wir von einer einfachen Idee zu einem strukturierten, wiederverwendbaren Python-Tool gelangen.
2. **Strukturierte Phasen**: Jede Entwicklungsphase hilft, die Idee weiter zu verfeinern und in funktionsfähigen Code umzuwandeln.
3. **Anwendung von Abstraktionen und Mustern**: Das Problem in kleinere Teile zu zerlegen und Entwurfsmuster zu verwenden, macht komplexe Probleme besser handhabbar.
4. **Iterative Verbesserung**: Kleine Prototypen ermöglichen Testen, Verfeinern und Verbessern, was zu einem ausgereiften Endprodukt führt.
