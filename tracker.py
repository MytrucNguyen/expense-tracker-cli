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

if __name__ == "__main__":
    tracker = ExpenseTracker()
    print("Loaded expenses:", tracker.expenses)