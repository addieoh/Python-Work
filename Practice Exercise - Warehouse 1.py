inventory = {'cats':10}
transaction = ('receive', 'a', 10)


def warehouse_process(inventory, transaction):
    if transaction[0] == 'receive':
        x = transaction[1]
        y = transaction[2]
        if x in inventory.keys():
            z = inventory[x]
            inventory.update({x:z+y})
        else:
            inventory.update({x:y})
    if transaction[0] == 'ship':
        x = transaction[1]
        y = transaction[2]
        z = inventory[x]
        inventory.update({x:z-y})
