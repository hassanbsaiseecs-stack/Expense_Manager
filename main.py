from expense import Expense,ExpenseTracker,InvalidExpenseError
from storage import save_expenses,load_expenses
FILENAME="expenses.json"
try:
    tracker=load_expenses(FILENAME)
    print("Existing expenses loaded")
except FileNotFoundError:
    tracker=ExpenseTracker()
    print("No existing data found. Starting fresh")
while True:
    print("\n--------Expenses Tracker--------")
    print("1. Add expense")
    print("2.View all expenses")
    print("3.View total spending")
    print("4.View total by category")
    print("5.Delete an expense")
    print("6.Exit")
    choice= input("Enter your choice: ")
    if choice=="1":
        try:
            amount=float(input("Amount: "))
            category=input("Category: ")
            description=input("Description: ")
            date=input("Date: ")
            expense=Expense(amount,category,description,date)
            tracker.add_expense(expense)
            print("Expense added successfully")
        except InvalidExpenseError as  e  :
            print(f"Error : {e}")
        except ValueError:
            print("Amount must be a number")
    elif choice=="2":
        for i,e in enumerate(tracker.list_expenses()):
            print(f"{i}.{e.date}|{e.category}|{e.description}|{e.amount}") 
    elif choice=="3":
        print(f"Total spending :{tracker.total()}")
    elif choice=="4":
        category=input("Enter the category: ")
        print(f"Total for {category}:{tracker.total_by_category(category)}")
    elif choice=="5":
        try: 
            index=int(input("Enter the expense number to delete : "))
            tracker.delete_expenses(index)
            print("Expense deleted ")
        except(ValueError,IndexError) as e:
            print(f"Error :{e}")
    elif choice=="6":
        save_expenses(tracker,FILENAME)
        print("Expenses saved.\nGoodbye")
        break
    else:
        print("Invalid choice selected.\nPlease try again")
        
        