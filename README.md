# 📝 Taskaty CLI
A simple command-line task manager built with Python.


## ✨ Features
- **Add Tasks:** Quickly add tasks with titles, descriptions, and deadlines.
- **List Tasks:** View all tasks or filter by unfinished ones in a beautiful, readable table.
- **Check/Uncheck:** Mark tasks as done with a single command.
- **Remove Tasks:** Delete specific tasks or clear your entire list.
- **Auto-Tracking:** Automatically tracks task creation dates and calculates days left (Due Date).

## 🚀 Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/hamzajs/taskaty-cli.git](https://github.com/hamzajs/taskaty-cli.git)
```

**2. Navigate to the project directory:**
```bash
cd taskaty-cli
```

**3. Create a virtual environment:**
```bash
python -m venv venv
```
*(Or `python3 -m venv venv` depending on your OS)*

**4. Activate the virtual environment:**
* **Windows:**
  ```bash
  venv\Scripts\activate
  ```
* **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

**5. Install the package locally:**
```bash
pip install -e .
```

## 💡 Usage

Once installed, you can use the `taskaty` command from anywhere in your terminal!

**Add a new task:**
```bash
taskaty add "Study Python" --description "Finish argparse chapter" --end_date "2026-05-01"
```

**List unfinished tasks:**
```bash
taskaty list
```

**List all tasks (including done):**
```bash
taskaty list --all
```

**Mark a task as done:**
*(Use the number shown in the list table)*
```bash
taskaty check --task 1
```

**Remove a task:**
```bash
taskaty remove --task 1
```

**Reset (Delete) all tasks:**
```bash
taskaty reset
```

## 🏗️ Architecture
This project is structured using the **MVC (Model-View-Controller)** pattern for clean and maintainable code:
- **Model:** `Task.py` (Data structure)
- **Controller:** `TaskController.py` (Business logic and file operations)
- **View/Router:** `app.py` (Command routing via `argparse`)

## 🛠️ Built With
- **Python 3**
- **argparse:** For parsing command-line options.
- **tabulate:** For formatting the task list into beautiful tables.

---
*Developed by Hamza Sulieman - IT Specialist*