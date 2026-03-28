## Calculate your expenses
Here are my first codes to calculate my expenses through two programs (one in Python, one in Java) 

Python code:
1. I use csv and os imports to calculate my expenses
2. I use two classes (OOP) `Expense` and `BudgetManager`
   - `Expense`
     > Constructor `__init__(self,category,amount)`
     > Function `to_list(self)` - makes a list out of `category` and `amount`
   - `BudgetManager`
     > Constructor `__init__(self,filename)` - defines the file with filename `budget.csv`
     > Function `setupfile(self)` - sets up the file from filename with columns `Kategorie` and `Betrag`
     > Function `addnewexpense(self,expense)` - adds a new expense with `to_list(self)`
     > Function `get_total(self)` - calculates the sum of my expenses
     > Function `reset_liste(self)` - resets the csv file and make the list again out of `category` and `amount`     
     
