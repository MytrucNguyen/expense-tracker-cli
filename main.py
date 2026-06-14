from tracker import ExpenseTracker
from expense import CATEGORIES


def show_menu() -> None:
    print()
    print("=== Expense Tracker ===")
    print("1. Add expense")
    print("2. List all expenses")
    print("3. Filter by category")
    print("4. View total")
    print("5. Quit")


def prompt_category() -> str:
    print("Categories:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f" {i}. {cat}")

    print(f" {len(CATEGORIES) + 1}. Custom")

    choice = input("Pick a category: ").strip()
    index = int(choice) - 1

    if index == len(CATEGORIES):
        return input("Custom category: ").strip()

    return CATEGORIES[index]


def handle_add(tracker: ExpenseTracker) -> None:
    description = input("Description: ").strip()
    amount = float(input("Amount: ").strip())
    category = prompt_category()
    date = input("Date (YYYY-MM-DD): ").strip()

    expense = tracker.add(description, amount, category, date)
    print(f"Added expense {expense.id}: {expense.description} (${expense.amount:.2f})")


def handle_list(tracker: ExpenseTracker) -> None:
    expenses = tracker.list_all()
    
    if not expenses:
        print("No expenses yet.")
        return
    
    for expense in expenses:
        print(f"  [{expense.id}] {expense.date} - {expense.description} ({expense.category}) ${expense.amount:.2f}")


def handle_filter(tracker: ExpenseTracker) -> None:
    category = prompt_category()
    expenses = tracker.filter_by_category(category)
    
    if not expenses:
        print(f"No expenses in {category}.")
        return
    
    for expense in expenses:
        print(f"  [{expense.id}] {expense.date} - {expense.description} ${expense.amount:.2f}")


def handle_total(tracker: ExpenseTracker) -> None:
    print(f"Total: ${tracker.total():.2f}")
    
    print("By category:")
    for category in CATEGORIES:
        amount = tracker.total(category)
        if amount > 0:
            print(f"  {category}: ${amount:.2f}")


def main() -> None: 
    tracker = ExpenseTracker()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_add(tracker)
        elif choice == "2":
            handle_list(tracker)
        elif choice == "3":
            handle_filter(tracker)
        elif choice == "4":
            handle_total(tracker)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print(f"Invalid option: {choice}")
                        

if __name__ == "__main__":
    main()