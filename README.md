# Expense Tracker CLI

A command-line expense tracker built in Python with JSON persistence. Tracks expenses by category, supports filtering and totals, and auto-saves between runs.

## Features

- Add, list, filter, and total expenses
- Predefined categories (Food, Transport, Entertainment, Bills, Shopping, Other) with custom category support
- Auto-load on start, auto-save after every change
- Persistent storage in a local JSON file

## Stack

- Python 3.13
- Standard library only (no external dependencies)

## Usage

Run the interactive menu:

```bash
python3 main.py
```

## Project Structure

```
expense-tracker-cli/
├── expense.py    # Expense data model
├── tracker.py    # Storage and business logic
├── main.py       # CLI interface
└── data.json     # Generated at runtime
```
