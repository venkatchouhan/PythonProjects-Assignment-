# Expent Tracker

import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        today = datetime.date.today()
        if today not in self.expenses:
            self.expenses[today] = []
        self.expenses[today].append({'amount': amount, 'category': category})

    def get_daily_spending(self, date):
        if date in self.expenses:
            total_spending = sum(expense['amount'] for expense in self.expenses[date])
            return total_spending
        else:
            return 0

    def get_monthly_spending(self, year, month):
        total_spending = 0
        for date, expenses in self.expenses.items():
            if date.year == year and date.month == month:
                total_spending += sum(expense['amount'] for expense in expenses)
        return total_spending

    def get_category_spending(self, category):
        total_spending = 0
        for expenses_list in self.expenses.values():
            for expense in expenses_list:
                if expense['category'] == category:
                    total_spending += expense['amount']
        return total_spending

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracking System")
        print("1. Add Expense")
        print("2. View Daily Spending")
        print("3. View Monthly Spending")
        print("4. View Category Spending")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            tracker.add_expense(amount, category)
            print("Expense added successfully!")
        elif choice == '2':
            date_str = input("Enter the date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            print(f"Total spending on {date}: ${tracker.get_daily_spending(date)}")
        elif choice == '3':
            year = int(input("Enter the year: "))
            month = int(input("Enter the month: "))
            print(f"Total spending in {datetime.date(year, month, 1).strftime('%B %Y')}: ${tracker.get_monthly_spending(year, month)}")
        elif choice == '4':
            category = input("Enter the category: ")
            print(f"Total spending in {category}: ${tracker.get_category_spending(category)}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
