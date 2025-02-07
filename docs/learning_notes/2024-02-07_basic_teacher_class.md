# Object-Oriented Programming in Python - Teacher Class Implementation
Session Date: February 07, 2024

## 1. Basic Class Concepts

### What is a Class?
- A class is like a blueprint for creating objects
- It defines both:
  - Properties (data/attributes)
  - Methods (functions that work with that data)
- Think of it as a template that describes what every teacher should have and be able to do

### Class Structure
```python
class Teacher:                  # Class name in CapitalizedWords
    def __init__(self, ...):   # Constructor method
        self.property = value   # Setting up properties
    
    def some_method(self):     # Additional methods
        # method code here
```

### Class Naming Conventions
- Class names use CapitalizedWords (also called PascalCase)
  - Good: `class Teacher:`
  - Not: `class teacher:` or `class TEACHER:`
- This is part of PEP 8 (Python's style guide)
- Helps immediately identify classes vs functions/variables
- Makes code more readable and professional

## 2. Properties (Attributes)

### What are Properties?
- Variables that belong to each instance of the class
- Defined using `self.property_name`
- Represent the data/state of an object

### Our Teacher Properties
```python
def __init__(self, name, position, total_hours, weekly_hours):
    self.name = name                # Teacher's name
    self.assigned_hours = 0         # Start with 0 hours
    self.total_hours = total_hours  # Maximum yearly hours
    self.weekly_hours = weekly_hours # Maximum weekly hours
    self.position = position        # Local or Invited
```

### Understanding self
- `self` refers to the specific instance being created/used
- Every instance method needs `self` as first parameter
- Allows accessing instance properties and methods
- Think of it as "this specific teacher"

## 3. Methods

### What are Methods?
- Functions that belong to a class
- Can access and modify the object's properties
- Defined inside the class
- Always take `self` as first parameter

### Special Methods
- `__init__`: Constructor method
  - Called when creating new object
  - Sets up initial properties
  - Name must be exactly `__init__`

### Our add_hours Method
```python
def add_hours(self, hours):
    self.assigned_hours += hours    # Add new hours
    return self.assigned_hours      # Return new total
```

## 4. Creating and Using Objects

### Creating Objects (Instantiation)
```python
my_teacher = Teacher("Maxime", "Local", 380, 20)
```
- Creates new Teacher object
- Calls `__init__` automatically
- Passes arguments to constructor

### Using Methods
```python
# Adding hours
current_hours = my_teacher.add_hours(25)

# Accessing properties
print(my_teacher.name)
print(my_teacher.assigned_hours)
```

## 5. Input Handling

### Type Conversion
- `input()` always returns strings
- Must convert to appropriate type:
  ```python
  hours = int(input('How_much_hours? '))
  ```
- Be careful with type mismatches

## 6. Next Steps

### Validation to Add
1. Check for negative hours
   ```python
   if hours < 0:
       # handle error
   ```

2. Check total hours limit
   ```python
   if self.assigned_hours + hours > self.total_hours:
       # handle error
   ```

3. Check weekly hours limit
   ```python
   if hours > self.weekly_hours:
       # handle error
   ```

### Future Enhancements
1. Track different types of teaching activities
2. Handle semester-based scheduling
3. Add reporting methods
4. Implement hour history tracking

## 7. Common Problems and Solutions

### TypeError with Input
Problem: `TypeError: can't add int and str`
Solution: Convert input to int before using
```python
# Good
hours = int(input('Hours? '))
self.assigned_hours += hours

# Bad
hours = input('Hours? ')  # Still a string
self.assigned_hours += hours  # Error!
```

### Value Not Updating
Problem: Changes not visible
Solution: Either return new value or print property
```python
# Option 1: Return and print
new_total = my_teacher.add_hours(hours)
print(f"New total: {new_total}")

# Option 2: Access property
my_teacher.add_hours(hours)
print(f"New total: {my_teacher.assigned_hours}")
```

## 8. Project Structure
```
course_planner/
├── src/
│   └── models/
│       └── teacher.py    # Our Teacher class
├── tests/
├── docs/
│   └── learning_notes/   # Where to save these notes
└── data/
```

## 9. Complete Current Code
```python
class Teacher:
    def __init__(self, name, position, total_hours, weekly_hours):
        self.name = name
        self.assigned_hours = 0
        self.total_hours = total_hours
        self.weekly_hours = weekly_hours
        self.position = position

    def add_hours(self, hours):
        self.assigned_hours += hours
        return self.assigned_hours

def main():
    my_teacher = Teacher("Maxime", "Local", 380, 20)
    hours = int(input('How_much_hours? '))
    print(f"Teacher: {my_teacher.name}")
    print(f"Position: {my_teacher.position}")
    print(f"Initial hours: {my_teacher.assigned_hours}")
    new_total = my_teacher.add_hours(hours)
    print(f"After adding {hours} hours: {new_total}")

if __name__ == "__main__":
    main()
```