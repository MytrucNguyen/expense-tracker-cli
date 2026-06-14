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

You'll see a menu like this:

```
=== Expense Tracker ===
1. Add expense
2. List all expenses
3. Filter by category
4. View total
5. Quit
Choose an option:
```

## Example session

```
Choose an option: 1
Description: Coffee
Amount: 4.50
Categories:
 1. Food
 2. Transport
 3. Entertainment
 4. Bills
 5. Shopping
 6. Other
 7. Custom
Pick a category: 1
Date (YYYY-MM-DD): 2026-05-05
Added expense 1: Coffee ($4.50)

Choose an option: 4
Total: $4.50
By category:
  Food: $4.50
```

## Project Structure

```
expense-tracker-cli/
├── expense.py    # Expense data model with JSON serialization
├── tracker.py    # Storage and business logic
├── main.py       # CLI interface
└── data.json     # Generated at runtime (gitignored)
```

## Architecture

The project separates concerns across three files:

- `expense.py` defines what a single Expense is - its fields, validation, and JSON conversion
- `tracker.py` manages the collection of expenses - add, list, filter, total, plus persistence to disk
- `main.py` is the user interface - menu loop, prompts, formatted output

This separation means the storage layer or UI could be swapped (e.g. to SQLite or a web frontend) without changing the data model or business logic.