# EXPENSE_TRACKER CLI 

A simple command-line expense tracker built in Python. Add, view, delete, and total expenses by category, with data automatically saved to a JSON file so nothing is lost between sessions.Invalid data handled using exception handling so that the program doesnot crash.

## Features
- Add an expense (amount, category, description, date)
- View all recorded expenses
- View total spending overall
- View total spending by category
- Delete an expense
- Data persists automatically using JSON — your expenses are saved on exit and reloaded next time you run the program
- Handles invalid input gracefully using custom exceptions (no crashes on bad amounts, missing files, or invalid indexes)

## Project Structure
Expense_Tracker/
├── main.py             # CLI menu — the entry point of the app
├── expense.py          # Expense and ExpenseTracker classes (core logic)
├── storage.py          # Functions for saving/loading data to/from JSON
├── test_expense.py     # Assert-based tests for core functionality
├── expensess.json      # Auto-created data file (not manually edited)
└── README.md           # This file
## How to Run
1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run:(main.py )the program and select the choices and trackyour expenses 
4. Follow the on-screen menu to add, view, or delete expenses.

## Running the Tests
This runs a set of `assert`-based checks confirming the core tracker logic (totals, category filtering, invalid-expense handling) behaves correctly. If all checks pass, it prints `All tests passed!`.

## Concepts Used
Built using everything covered across the bootcamp: custom exceptions and `try`/`except` for graceful error handling, OOP with classes and inheritance-ready structure, JSON file persistence, modular code split across multiple files by responsibility, and `assert`-based testing.