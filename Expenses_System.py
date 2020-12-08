from Expense import *
from AnalysisMode import *

Expenses = []

running = True
while running == True:
    print("Main Menu")
    print("For Edit Mode type 1")
    print("For Analysis Mode type 2")
    print("To exit the program type Exit")
    Choice = input()
    if Choice == 1:
        pass
    elif Choice == 2:
        AnalysisMode(Expenses)
    elif Choice == "Exit":
        running = False
