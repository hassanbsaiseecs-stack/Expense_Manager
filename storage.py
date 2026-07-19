import json
from expense import Expense,ExpenseTracker
def save_expenses(tracker,filename):
    data =[e.to_dict() for e in tracker.expenses]
    with open(filename,"w") as file:
        json.dump(data,file)
def load_expenses(filename):
    tracker=ExpenseTracker()
    with open(filename,"r") as file:
        data=json.load(file)
    for item in data:
        expense=Expense(item["amount"],item["category"],item["description"],item["date"])
        tracker.add_expense(expense)
    return tracker