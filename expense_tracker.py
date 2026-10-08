import csv
import os

expenses = []
def save_expenses():
    with open("expenses.csv" , "w", newline = "") as file :
        writer = csv.DictWriter( file , fieldnames=["name" , "category" , "amount" ,"date"])
        writer.writeheader()
        writer.writerows(expenses)
def load_expenses():
     if os.path.exists("expenses.csv"):
         with open("expenses.csv" , "r") as file:
             reader = csv.DictReader(file)
             for row in reader:
                 row["amount"] = float(row["amount"])
                 expenses.append(row)
load_expenses()
while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. View Category-wise Spending")
    print("5. View Highest Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        date = input("enter date (DD-MM-YYYY): ")

        expense = {
            "name": name,
            "category": category,
            "amount": amount,
            "date": date
        }

        expenses.append(expense)
        save_expenses()

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\n----- ALL EXPENSES -----")

            for expense in expenses:
                print(
                    f"{expense['name']} | "
                    f"{expense['category']} | "
                    f"₹{expense['amount']}"
                    f"{expense['date']}" 
                              )              

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total spending: ₹{total}")

    elif choice == "4":
        category_totals = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        print("\n----- CATEGORY-WISE SPENDING -----")

        for category, total in category_totals.items():
            print(f"{category}: ₹{total}")

    elif choice == "5":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            highest = expenses[0]

            for expense in expenses:
                if expense["amount"] > highest["amount"]:
                    highest = expense

            print("\n----- HIGHEST EXPENSE -----")
            print("Name:", highest["name"])
            print("Category:", highest["category"])
            print("Amount:", highest["amount"])

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    elif choice == "7":
         if len(expenses) == 0:
             print("No expenses to delete.")
    else:
             print("\n----- SELECT EXPENSE TO DELETE -----")

    for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['name']} | {expense['category']} | ₹{expense['amount']}")

    number = int(input("Enter expense number to delete: "))

    if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses()
            print(f"Deleted: {deleted['name']} | ₹{deleted['amount']}")
    else:
           print("Invalid expense number.")

else :
    print("Invalid choice. Please try again.")  