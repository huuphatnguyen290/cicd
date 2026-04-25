# Spending Tracker

def calculate_total(expenses: list) -> float:
    return sum(e["amount"] for e in expenses)



def calculate_average(expenses: list) -> float:
    if len(expenses) == 0:
        return 0.0
    return calculate_total(expenses) / len(expenses)


def get_top_category(expenses: list) -> str | None:
    if not expenses:
        return None
    category_totals: dict = {}
    for e in expenses:
        category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]
    return max(category_totals, key=lambda k: category_totals[k])


def add_expense(expenses: list, desc: str, amount: float, category: str) -> None:
    if not desc or amount <= 0:
        raise ValueError("Invalid expense")
    expenses.append({"desc": desc, "amount": amount, "category": category})


if __name__ == "__main__":
    expenses: list = []

    while True:
        print("\n1. Add expense")
        print("2. View report")
        print("3. Quit")
        choice: str = input("Choose: ")

        if choice == "1":
            desc = input("Description: ")
            amount = float(input("Amount: $"))
            category = input("Category (Food/Transport/Shopping/Bills/Other): ")
            try:
                add_expense(expenses, desc, amount, category)
                print("Expense added!")
            except ValueError:
                print("Invalid input. Description cannot be empty and amount must be positive.")

        elif choice == "2":
            if not expenses:
                print("No expenses yet.")
            else:
                print("\nSpending Tracker Report")
                print("-----------------------")
                print(f"Total Spent:    ${calculate_total(expenses):.2f}")
                print(f"Average:        ${calculate_average(expenses):.2f}")
                print(f"Top Category:   {get_top_category(expenses)}")
                print(f"Transactions:   {len(expenses)}")

        elif choice == "3":
            break