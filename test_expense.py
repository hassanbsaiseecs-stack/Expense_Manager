from expense import Expense,ExpenseTracker,InvalidExpenseError
tracker=ExpenseTracker()
tracker.add_expense(Expense(100,"Food","Lunch","2026-07-19"))
tracker.add_expense(Expense(50,"Transport","Bus fare","2026-07-19"))
assert tracker.total()==150,"Total should be 150"
assert tracker.total_by_category("food")== 100,"Food total should be 100"

assert len(tracker.get_unique_categories())==2,"There should be 2 unique categories"
try:
    Expense(-10,"Food","Bad expense","2026-07-19")
    assert False, "Should have raised InvalidExpenseError"
except InvalidExpenseError:
    pass
print("All tests passed..............")