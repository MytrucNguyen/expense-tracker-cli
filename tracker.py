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


    def list_all(self) -> list[Expense]:
        return self.expenses


    def filter_by_category(self, category: str) -> list[Expense]:
        return [e for e in self.expenses if e.category == category]


    def total(self, category: str | None = None) -> float:
        if category is None:
            return sum([e.amount for e in self.expenses])
        
        return sum([e.amount for e in self.expenses if e.category == category])


if __name__ == "__main__":
    tracker = ExpenseTracker()
    
    tracker.add(description="Coffee", amount=4.50, category="Food", date="2026-05-05")
    tracker.add(description="Bus", amount=2.75, category="Transport", date="2026-05-05")
    tracker.add(description="Movie", amount=15.00, category="Entertainment", date="2026-05-05")
    
    print("All:", [e.to_dict() for e in tracker.list_all()])
    print("Food only:", [e.to_dict() for e in tracker.filter_by_category("Food")])
    print("Total all:", tracker.total())
    print("Total Food:", tracker.total("Food"))