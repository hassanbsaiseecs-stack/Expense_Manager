class InvalidExpenseError(Exception):
    pass
class Expense:
    def __init__(self,amount,category,description,date):
        if amount<=0:
            raise InvalidExpenseError("Expense amount must be positive")
        self.amount=amount
        self.category=category.strip().lower()
        self.description=description.strip()
        self.date=date
    def to_dict(self):
        return{
            "amount":self.amount,
            "category":self.category,
            "description":self.description,
            "date":self.date
        }
class ExpenseTracker:
    def __init__(self):
        self.expenses=[]
    def add_expense(self,expense):
        self.expenses.append(expense)
    def total(self):
        return sum(e.amount for e in self.expenses)
    def total_by_category(self,category):
        category=category.strip().lower()
        return sum(e.amount for e in self.expenses if e.category==category)
    def get_unique_categories(self):
        return {e.category for e in self.expenses}
    def delete_expenses(self,index):
        if index<0 or index  >=len(self.expenses):
            raise IndexError("Invalid expense index")
        del self.expenses[index]
    def list_expenses(self):
        return self.expenses