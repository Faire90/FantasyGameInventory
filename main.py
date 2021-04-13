import pprint

#function for displaying inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    #iterate through the given dictionary totaling all quantities (v)
    #and displaying each item (k) with its number (v)
    for k, v in inventory.items():
        item_total = item_total + v
        print(k, v)
    pprint.pprint("Total number of items: " + str(item_total))

if __name__ == '__main__':
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)
