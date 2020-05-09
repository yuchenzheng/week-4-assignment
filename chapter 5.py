#Yuchen Zheng Csc101
#chapter 5 practice project
#Put new number of inventory into the original data
def addToInventory(Inventory, addedItem):
    #set a for loop for check every elements in the new inventory list
    for i in range(len(addedItem)): 
        if addedItem[i] in Inventory.keys():
            Inventory[addedItem[i]] += 1
        else:
            Inventory.setdefault(addedItem[i], 1)
    #return new dictionary of inventory data
    return Inventory



#transfer dictionary as display mode
def displayInventory(Inventory):
    print('Inventory:')
    total = 0
    #set a for loop for print out every inventery and compute the total number
    for key, value in Inventory.items():
        print(str(value) + ' ' + key)
        total += Inventory[key]
    print()
    print()
    #print out the total number
    print('Totol number of items: ' + str(total))


#two pre-conditions, it can be change to any other data with same form
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#use the new dictionary to display
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

