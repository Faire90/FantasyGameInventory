import pprint

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#function for displaying inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    #iterate through the given dictionary totaling all quantities (v)
    #and displaying each item (k) with its number (v)
    for k, v in inventory.items():
        item_total += v
        print(k, v)
    pprint.pprint("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
#iterate through the added items list.
#With each item in the list, find the item in the original inventory and add one.
#if the item doesn't exist, then add the item and set it's total to 1.
    for i in addedItems:
        inventoryAddition = inventory.get(i, 0)
        if inventoryAddition != 0:
            inventory[i] = inventoryAddition + 1
        else:
            inventory[i] = 1


if __name__ == '__main__':
    displayInventory(stuff)
    addToInventory(stuff, dragonLoot)
    displayInventory(stuff)
