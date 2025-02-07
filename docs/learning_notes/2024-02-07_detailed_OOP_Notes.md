# Object-Oriented Programming Progress Notes
Session Date: February 07, 2025

## 1. Class Interactions Deep Dive

### What We Learned
Classes can interact by:
1. Passing objects as parameters
2. Storing references to other objects
3. Returning objects from methods

### Examples

#### Bad Practice (String-based):
```python
def add_course(self, course_name: str):
    if course_name == "AOM_1":
        self.hours += 20  # Magic numbers, no validation
```

#### Good Practice (Object-based):
```python
def add_course(self, course: Course):
    if self.can_add_hours(course.LC_hours):
        self.assigned_hours += course.LC_hours
        self.courses.append(course)  # Keep reference to course object
```

### Key Benefits
1. Type Safety: Python can check if you're passing the right type
2. Access to All Properties: No need to look up course details separately
3. Maintainability: Changes to Course class automatically reflect everywhere

## 2. Input Validation Patterns

### Simple vs. Robust Validation

#### Simple (What we started with):
```python
def get_hours_input():
    hours = int(input("Hours: "))  # Dangerous!
    return hours
```

#### Robust (What we evolved to):
```python
def get_hours_input():
    while True:
        try:
            hours = int(input("Hours: ").strip())
            if hours >= 0:
                return hours
            print("Hours must be positive")
        except ValueError:
            print("Please enter a valid number")
```


## 3. Loop Control Patterns

### Finding Objects in Lists

#### Initial Approach (Problematic):
```python
# Problem: Creates unnecessary list, checks all items even after finding match
course_names = [c.name for c in courses]
if course_name in course_names:
    return courses[course_names.index(course_name)]
```

#### Better Approach:
```python
# Direct comparison, returns immediately on match
for course in courses:
    if course.name.upper() == course_name.upper():
        return course
```


## 4. Practical Examples of Class Integration

### Teacher-Course Relationship

```python
class Teacher:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        self.courses: List[Course] = []  # Track assigned courses
        self.hours_by_course: dict = {}  # Track hours per course

    def assign_course(self, course: Course) -> bool:
        if course not in self.courses:
            self.courses.append(course)
            self.hours_by_course[course.name] = 0
            return True
        return False

    def add_hours(self, course: Course, hours: int) -> bool:
        if course not in self.courses:
            return False
        self.hours_by_course[course.name] += hours
        return True
```

## 5. Common Pitfalls and Solutions

### 1. Object Comparison
```python
# Wrong: String comparison
if course_name == "AOM_1":

# Right: Object comparison
if course.name.upper() == input_name.upper():
```

### 2. Error Handling
```python
# Wrong: Catch-all exception
try:
    # code
except:
    print("Error")

# Right: Specific exceptions
try:
    hours = int(input("Hours: "))
except ValueError:
    print("Please enter a valid number")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 3. State Management
```python
# Wrong: No validation before state change
def add_hours(self, hours):
    self.assigned_hours += hours

# Right: Validate before changing state
def add_hours(self, hours):
    if self.can_add_hours(hours):
        self.assigned_hours += hours
        return True
    return False
```

## 6. Next Steps and Challenges

### Immediate Challenges
1. Implement teaching type selection
2. Track teacher-course assignments


### Future Enhancements
1. Add weekly schedule tracking
2. Implement semester-based validation
3. Add reporting methods

## Questions to Explore

1. Data Structure Decisions:
   - How to track hours by week?
   - How to handle schedule conflicts?
   - Best way to store teaching history?

2. Validation Rules:
   - When should validation happen?
   - What makes input valid?
   - How to handle edge cases?

Save in: `docs/learning_notes/2025-02-07_detailed_oop_concepts.md`

For next session, start with:
"Hi Claude, after reviewing our detailed OOP notes, I'm ready to implement teaching type tracking in the Course-Teacher relationship. I'm working on Phase 1 still, focusing on the interaction between Course and Teacher classes with different teaching types."