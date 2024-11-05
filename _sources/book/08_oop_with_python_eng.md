## Code Design & Object-Oriented Programming (OOP) Basics

### Part 1: Repetition of OOP Basics

#### 1. Class vs. Instance

In Object-Oriented Programming (OOP), **classes** and **instances** are two fundamental concepts that allow us to organize code in a structured, modular way.

- **Class**: A blueprint or template for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
- **Instance**: A specific object created from a class. Each instance has its own set of data, based on the class’s structure.

Let’s start with an analogy to make the concept clearer:

Imagine a class called `Bike`. It defines the structure and features of a car in general, such as its color, model, and methods like `drive()` and `stop()`. However, the class itself isn’t a car you can drive. Instead, you create **instances** of the `Car` class—individual cars with specific attributes, like a red Toyota or a blue Ford.

```python
# Defining a basic class in Python
class Bike:
    # Class attribute
    wheels = 4  # All cars have 4 wheels
    
    # Constructor method
    def __init__(self, color, model):
        # Instance attributes
        self.color = color
        self.model = model

# Creating instances of the Car class
car1 = Car("red", "Toyota")
car2 = Car("blue", "Ford")

# Accessing instance attributes
print(car1.color)  # Output: red
print(car2.color)  # Output: blue

# Accessing a class attribute
print(Car.wheels)  # Output: 4
```

#### Key Points:
- `Car` is the **class**. It provides the structure: `wheels`, `color`, `model`.
- `car1` and `car2` are **instances** of the `Car` class, each with their own `color` and `model` attributes.
- `wheels` is a **class attribute**, shared by all instances. Changing it in the class changes it for all instances.
  
#### 2. Class in Python

A **class** in Python is defined using the `class` keyword. It typically contains a constructor method, `__init__`, which is called when a new instance is created. The constructor allows us to define initial attributes specific to each instance.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name      # Instance attribute
        self.species = species # Instance attribute

# Creating instances of the Animal class
animal1 = Animal("Leo", "Lion")
animal2 = Animal("Bella", "Elephant")

print(animal1.name)  # Output: Leo
print(animal2.species)  # Output: Elephant
```

In this example:
- `name` and `species` are **instance attributes**—specific to each instance (`animal1` and `animal2`).
- Each instance has unique data, but they both share the structure of the `Animal` class.

#### 3. Methods and Attributes

**Attributes** are the data stored within an instance, while **methods** are functions defined in a class that operate on instances of the class.

There are two main types of attributes:
- **Instance Attributes**: Specific to each instance. They are defined inside the `__init__` method using `self`.
- **Class Attributes**: Shared across all instances of the class.

**Methods** are functions defined within a class and are typically used to modify instance data or perform actions related to the class.

```python
class Circle:
    # Class attribute
    pi = 3.1415
    
    def __init__(self, radius):
        # Instance attribute
        self.radius = radius
    
    # Method to calculate the area
    def calculate_area(self):
        return Circle.pi * (self.radius ** 2)
    
    # Method to calculate the circumference
    def calculate_circumference(self):
        return 2 * Circle.pi * self.radius

# Creating an instance of Circle
circle1 = Circle(5)

# Calling methods on the instance
print(circle1.calculate_area())           # Output: 78.5375
print(circle1.calculate_circumference())  # Output: 31.415
```

In this example:
- `pi` is a **class attribute**, which is common to all circles.
- `radius` is an **instance attribute** set during initialization.
- `calculate_area` and `calculate_circumference` are **methods** that operate on the instance data and use both class and instance attributes.
