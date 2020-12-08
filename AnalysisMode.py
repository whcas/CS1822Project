from AveragesFunftion import *
from Total_Expenditure import *
from Breakdown import * 

def AnalysisMode(Expenses):
    print("Analysis Mode")
    average = AveragesFunction(Expenses)
    total = Total(Expenses)
    Breakdown(Expenses)
    print("The average expense is " average)
    print("The total expenditure is " total)
