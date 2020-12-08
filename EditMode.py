class Expense:
    def __init__(self,Index, Description, Category, Amount):
        self.Index = Index
        self.Description = Description
        self.Category = Category
        self.Amount = Amount
IndexList = []
IndexDictionary = {}
def Add():
    Index = input("Please input an index for this item")
    Description = input("Please input a description for this item")
    Category = input("Please input a category for this item")   
    Amount = input("Please input an amount for this item")
    Item = Expense(Index, Description, Category, Amount)
    IndexList.append(Index)
    IndexDictionary[Index] = Item 

def Delete():
    if len(IndexList) > 0:
        
        for Item in IndexList:
            x = int(Item) - 1
            q = IndexDictionary.get(IndexList[x])
            print(IndexList[x],q.Description, q.Category, q.Amount)
            Item = str(Item)
        item_remove = input("Please input the index of the item which you wish to remove")
        check = input("Are you sure you want to remove this item, input yes if you do")
        if check.lower() == "yes":
           for index in IndexList:
               x = int(index)
               x -= 1
               n = IndexDictionary.get(IndexList[x])
               if index == n.Index:
                    IndexList.remove(IndexList[x])
    if len(IndexList) == 0:
        print("There are no items to delete")

Add()
Add()
Delete()

