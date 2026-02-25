expenses = []

def add_expense(category, amount):
    expense = {
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print(f"Added ${amount:.2f} to {category} category.")

def get_total_expenses():
    return sum(expense["amount"] for expense in expenses)

def get_category_total(category):
    return sum(expense["amount"] for expense in expenses if expense["category"] == category)

def show_category_expenses(category):
    total = get_category_total(category)
    count = sum(1 for expense in expenses if expense["category"] == category)
    print(f"\n{category} Expenses:")
    for expense in expenses:
        if expense["category"] == category:
            print(f"  - ${expense['amount']:.2f}")
    print(f"Total for {category}: ${total:.2f} ({count} transactions)")

def display_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nExpense Tracker:")
    categories = set(expense["category"] for expense in expenses)
    for category in categories:
        total = get_category_total(category)
        print(f"{category}: ${total:.2f}")
    print(f"Total Expenses: ${get_total_expenses():.2f}")

def main():
    while True:
        try:
            print("\n1.Add Expense")
            print("2.View Expenses")
            print("3.View Category Expenses")
            print("4.Exit")

            choice = input("Choose an option: ")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break
        if choice == '1':
            try:
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))
                add_expense(category, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            category = input("Enter category to view: ")
            show_category_expenses(category)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()