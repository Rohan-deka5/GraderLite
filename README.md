# 🎓 GraderLite

**GraderLite** is a lightweight console-based Python app that calculates a student's percentage and returns a grade with a custom motivational (or brutally honest 😭) message.

## 💻 Features

- Enter total and received marks
- Calculates your percentage
- Assigns a letter grade (A–F)
- Returns a spicy motivational message based on performance
- Modular design (split across clean Python files)

## 📂 File Structure

GraderLite/
├── build.py # Main runner
├── grade_logic.py # Grade logic and messages
├── user_percentage.py # User input + percentage calculator


## 🚀 Usage

### Run it from your terminal:

```bash
python build.py

## 💡 Sample Output:

Enter your name: Vortexu
Enter your total marks:- 100
Enter your received marks:- 78
Your percentage is: 78.00%
Grade Letter: B
Practice more, You can do it bro ❤️🌻

## 🛠️ Ideas for v2.0

    Export report as .csv

    Loop over multiple students

    Add input validation

    Make it a web API (Flask/FastAPI)

    Build a frontend (PyScript/Tkinter)


