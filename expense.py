CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"]

class Expense:
    def __init__(self, id: int, description: str, amount: float, category: str, date: str):
        self.id = id
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            id=data["id"],
            description=data["description"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
        )

if __name__ == "__main__":
    expense = Expense(
        id=1,
        description="Coffee",
        amount=4.50,
        category="Food",
        date="2026-05-04",
    )

    print(expense.to_dict())

    data = expense.to_dict()
    expense2 = Expense.from_dict(data)
    print(f"Expense 2: {expense2.to_dict()}")
    print(f"Expense 2 Description: {expense2.description}")