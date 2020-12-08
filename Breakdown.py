def Breakdown(Expenses):
    Catagories = []
    for Expense in Expenses:
        cat = Expense.Category
        new = True
        for Catagory in Catagories:
            if cat == Catagory[0]:
                new = False
        if new == True:
            Catagories.append(cat)
        for Catagory in Catagories:
            if cat == Catagory[0]:
                Catagory.append(Expense)
    
    for Catagory in Catagories:
        print(Catagory[0])
        for i in range(1, len(Catagory)):
            print(Catagory[i].Description)
            print(Catagory[i].Amount)
