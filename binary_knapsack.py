from copy import deepcopy

class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        
def optimal_knapsack(bag, max_weight):
    table = [[0 for x in range(0, max_weight+1)] for item in bag]
    items = []
    
    for i in range(0, len(bag)):
        for wt in range(0, max_weight+1):
            if i == 0 and bag[i].weight <= wt:
                table[i][wt] = bag[i].weight
                
            elif bag[i].weight <= wt:
                remainder_value = table[i-1][wt - bag[i].weight]
                table[i][wt] = max(table[i-1][wt], bag[i].value + remainder_value)
                
            else:
                table[i][wt] = table[i-1][wt]
    
    wt = max_weight     
    for i in range(len(bag)-1, 0, -1):
        if table[i-1][wt] == table[i][wt]:
            items.append(bag[i-1])
        wt -= bag[i-1].weight
        
    for row in table:
        print row
    return items

if __name__ == "__main__":
    bag = [Item("knife",1,1), Item("apple",4,3), Item("phone",5,4), Item("matches",7,5)]

    for item in optimal_knapsack(bag, 7):
        print(item.name)
        
    