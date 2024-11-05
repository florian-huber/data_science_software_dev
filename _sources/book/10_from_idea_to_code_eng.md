## From Idea to Code - Building an ASCII Scatter Plot Tool in Python

### Overview

In this lesson, we’ll go through a concrete example to develop an ASCII scatter plot tool in Python. We'll start with a concept and work through each development phase to build a functional program. This approach demonstrates how to systematically break down an idea and implement it step-by-step.

### **Problem Statement**
We want to create a Python tool that:
1. Loads x, y coordinate data from a CSV file.
2. Displays an ASCII scatter plot in the console, using a character of our choice (e.g., "*", "x", "o").
3. Keeps track of character aspect ratio, since ASCII characters are typically taller than they are wide.
4. Adds simple x and y axes for reference.

---

### **Phases of Development**

Let’s walk through each phase, applying it to our ASCII scatter plot tool.

---

### **Phase 1: Requirement Analysis & Use Cases**

#### **Goals**:
- **Primary Goal**: Visualize `x, y` coordinates in a simple ASCII scatter plot format.
- **Detailed Requirements**:
  - Load data from a CSV file with columns `x` and `y`.
  - Scale and display the coordinates on an ASCII grid.
  - Support custom plot characters for flexibility.
  - Adjust for the non-square aspect ratio of characters.
  - Include x and y axes to improve readability.

#### **Use Case**:
Suppose a data scientist has a CSV file with `x, y` coordinates and needs a quick way to visualize the data. This ASCII plot provides a simple, text-based solution, particularly useful for environments without graphical tools.

---

### **Phase 2: Conceptual Modeling**

**Primary Components**:
- **CSV Reader**: Loads `x, y` data from a file and validates that these columns exist.
- **Scaler**: Adjusts the coordinate values to fit within an ASCII grid of a specified size. It accounts for the character’s aspect ratio to prevent distortion.
- **Plotter**: Maps each coordinate to the correct position in the ASCII grid.
- **Display**: Prints the final ASCII plot to the console.

**Class Structure**:
We decide to wrap these components in an `AsciiScatterPlot` class. This class will manage all the steps in one place, allowing easy modification and reuse. Here’s an outline:

- **Attributes**:
  - `char` – The character for plotting points.
  - `width`, `height` – Dimensions of the ASCII grid.
  - `aspect_ratio` – Adjusts scaling to account for character height/width differences.
  - `grid` – A 2D list representing the ASCII grid.
- **Methods**:
  - `load_csv()` – Loads CSV data, validating `x, y` columns.
  - `scale_coordinates()` – Scales coordinates to fit the grid.
  - `plot_points()` – Maps scaled coordinates onto the grid.
  - `add_axes()` – Adds x and y axes to the grid.
  - `display()` – Prints the final grid to the console.
  - `plot_from_csv()` – High-level function to execute all steps in sequence.

---

### **Phase 3: Decomposition & Abstraction**

Each function in the class handles a specific task:

- **`load_csv()`**: This function will use `pandas` to load the CSV file, ensuring `x` and `y` columns are present.
- **`scale_coordinates()`**: Adjusts `x` and `y` values to fit within the grid dimensions. Scaling keeps coordinates proportionate to the grid, while aspect ratio ensures that each point appears in the correct position visually.
- **`plot_points()`**: This maps the scaled coordinates to the grid, using the specified character for each point. 
- **`add_axes()`**: Provides context to the plot by adding simple x and y axes at the bottom and left edges.
- **`display()`**: Renders the grid to the console row by row, simulating a 2D scatter plot in ASCII format.

---

### **Phase 4: Design Patterns**

We'll skipt this since this is not very relevant for such a simple example.

---

### **Phase 5: Pseudocode and Flowcharts**

**Pseudocode**:
```plaintext
1. Initialize AsciiScatterPlot with specified character, grid dimensions, and aspect ratio.
2. Load CSV file with x, y coordinates using load_csv().
3. Scale the coordinates to fit the ASCII grid using scale_coordinates().
4. Add x and y axes to the grid with add_axes().
5. Map the scaled coordinates onto the grid using plot_points().
6. Display the grid to the console with display().
```

**Flowchart**:

1. **Start** → **Initialize Class** → **Load CSV**
2. If `x, y` columns exist:
   - → **Scale Coordinates**
   - → **Add Axes**
   - → **Map Coordinates to Grid**
   - → **Display Grid**
   - → **End**
3. Else:
   - **Error**: Invalid CSV file

---

### **Phase 6: Prototyping and Feedback**

- We start with a prototype that loads the CSV and scales coordinates.
- In the first version, we don’t implement aspect ratio adjustments or axes. Instead, we focus on loading, scaling, and printing the points directly.
- After testing basic functionality, we add aspect ratio handling and axes to create a more refined prototype.

### **Phase 7: Iterative Refinement**

Refinements include:

1. **Aspect Ratio**: Adjust the `width` based on the specified `aspect_ratio`, improving the look of the plot.
2. **Axes**: Add x and y axes to make the plot easier to interpret.
3. **Simplifications**: We optimize the code by using `clip` and `round` functions in the scaling process to ensure clean, bounded coordinates without complex checks.

---

### **Final Product**

The resulting code is now ready for use, tested to load any CSV file with `x, y` coordinates, and capable of rendering a clean ASCII scatter plot with clear axes.

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

### **Lesson Summary**

1. **From Idea to Code**: We’ve demonstrated the journey from a simple idea to a structured, reusable Python tool.
2. **Structured Phases**: Each development phase helps refine the idea, bringing it closer to working code.
3. **Applying Abstractions and Patterns**: Breaking the problem into smaller pieces and using patterns makes complex problems more manageable.
4. **Iterative Improvement**: Small prototypes allow for testing, refinement, and improvement, leading to a more polished final product.

