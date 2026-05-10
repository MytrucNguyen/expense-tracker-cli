import json
import os
from expense import Expense

DATA_FILE = "data.json"


class ExpenseTracker:
    def __init__(self):
        self.expenses: list[Expense] = []
        self._load()


    def _load(self) -> None:
        if not os.path.exists(DATA_FILE):
            return
        
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        self.expenses = [Expense.from_dict(d) for d in data]


    def _save(self) -> None:
        data = [e.to_dict() for e in self.expenses]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    
    def add(self, description: str, amount: float, category: str, date: str) -> Expense:
        if not self.expenses:
            next_id = 1

        else: 
            next_id = max([e.id for e in self.expenses]) + 1

        expense = Expense(
            id = next_id,
            description = description,
            amount = amount,
            category = category,
            date = date
        )

        self.expenses.append(expense)

        self._save()

        return expense


if __name__ == "__main__":
    tracker = ExpenseTracker()
    print("Loaded expenses:", tracker.expenses)

    new_expense = tracker.add(
        description="Coffee",
        amount=4.50,
        category="Food",
        date="2026-05-05",
    )
    
    print("Added:", new_expense.to_dict())
    print("After:", [e.to_dict() for e in tracker.expenses])
