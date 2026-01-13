## Requirements

- Python 3.8+

-------------------------------------------------------------------------------

## Running Tests

This project uses Python's built-in `unittest` framework.

To run all tests:

```bash
python -m unittest


----------------------------------------------------------------------------


## Architecture Overview

- `StudentManager` handles all business logic
- JSON persistence is separated from core logic
- CLI layer is responsible for user interaction

----------------------------------------------------------------------------

## Example Data File

```json
{
  "version": 1,
  "students": {
    "Alice": {
      "age": 20,
      "grades": [90, 85],
      "courses": ["Math", "Physics"]
    }
  }
}


----------------------------------------------------------------------------

# 🎓 Student Manager

A Python project to manage students, courses, and grades using clean architecture,
object-oriented programming, and JSON persistence.

---

## 🚀 Features

- Add students with age and courses
- Add grades to students
- Calculate average grades
- Filter top-performing students
- List students by course
- Persistent storage using JSON
- Command-line interface (CLI)
- Unit tests with `unittest`

---

## 🛠️ Requirements

- Python 3.8+

---

## 📁 Project Structure

```text
student-manager/
├── student_manager/
│   ├── manager.py        # Core business logic
│   └── persistence.py    # JSON persistence
│
├── cli.py                # CLI interface
├── main.py               # Entry point
├── tests/                # Unit tests
└── students.json         # Auto-generated data file
