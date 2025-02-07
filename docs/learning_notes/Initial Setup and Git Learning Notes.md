# Development Environment Setup and Git Basics
Learning notes from initial project setup - Date: 2024-02-07

## Project Structure Setup
We created the following directory structure:
```
course_planner/
│
├── docs/                    # Documentation
│   ├── learning_notes/     # Personal notes on concepts
│   └── challenges/         # Documentation of challenges and solutions
│
├── src/                    # Source code
│   ├── models/            # Data classes
│   ├── controllers/       # Business logic
│   ├── views/            # User interface
│   └── utils/            # Helper functions
│
├── tests/                 # Test files
├── data/                 # Data storage
└── README.md             # This file
```

### Python Package Structure
We created `__init__.py` files in each directory to mark them as Python packages:
```bash
touch src/__init__.py
touch src/models/__init__.py
touch src/controllers/__init__.py
touch src/views/__init__.py
touch src/utils/__init__.py
```

**Why __init__.py?**
- Makes directories recognizable as Python packages
- Allows importing from these directories
- Can contain initialization code
- Controls what gets exposed when importing

Example usage:
```python
# Without __init__.py this wouldn't work:
from src.models.teacher import Teacher
```

## Git Setup and Basic Commands

### Initial Git Configuration
```bash
# Check Git installation
git --version

# Configure Git (replace with your details)
git config --global user.name "Okamorii"
git config --global user.email "your.email@example.com"
```

### Git Command Workflow
Think of Git like taking photos for an album:

1. `git add` (Gathering people for photo)
   - Stages files for commit
   ```bash
   git add filename.py    # Stage specific file
   git add .             # Stage all files
   ```

2. `git commit` (Taking the photo)
   - Creates a snapshot of staged files
   ```bash
   git commit -m "Description of changes"
   ```

3. `git push` (Uploading to social media)
   - Uploads commits to GitHub
   ```bash
   git push
   ```

### Working with Branches
Branches are separate lines of development.

Basic Branch Commands:
```bash
# View branches
git branch

# Create new branch
git branch feature-name

# Create and switch to new branch
git checkout -b feature-name

# Switch branches
git checkout main
```

Example Branch Workflow:
```bash
# Start new feature
git checkout -b feature-teacher-class

# Make changes
echo "class Teacher:" > src/models/teacher.py
git add .
git commit -m "Start Teacher class development"

# Switch back to main for urgent fix
git checkout main
# Make fix
git commit -m "Fix urgent issue"

# Return to feature
git checkout feature-teacher-class
git merge main  # Get main's changes

# When feature is complete
git push -u origin feature-teacher-class
```

### Important Git Concepts

1. **Empty Directories**
   - Git doesn't track empty folders
   - Solution: Add `.gitkeep` file
   ```bash
   touch docs/learning_notes/.gitkeep
   touch docs/challenges/.gitkeep
   touch tests/.gitkeep
   touch data/.gitkeep
   ```

2. **Branch Patterns**
   - main: Stable code
   - develop: Work in progress
   - feature branches: New features
   - bugfix branches: Bug fixes

3. **.gitignore File**
   Important files to ignore:
   - `__pycache__/`
   - Virtual environment folders
   - IDE settings
   - System files
   - Sensitive data

## Next Steps
1. Create first feature branch for Teacher class
2. Set up Python virtual environment
3. Start implementing basic classes
4. Write initial tests

## Questions for Future Reference
- How to resolve merge conflicts?
- How to undo changes in branches?
- How to collaborate using branches?
- How to manage dependencies?

## Resources
- Git documentation: https://git-scm.com/doc
- Python packaging: https://packaging.python.org/
- GitHub guides: https://guides.github.com/