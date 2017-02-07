class Warehouse:
    def __init__(self):
        self.inventory = {}
            
    def process(self, transaction):
        if transaction[0] == 'receive':
            x = transaction[1]
            y = transaction[2]
            if x in self.inventory.keys():
                z = self.inventory[x]
                self.inventory.update({x:z+y})
            else:
                self.inventory.update({x:y})
        if transaction[0] == 'ship':
            x = transaction[1]
            y = transaction[2]
            z = self.inventory[x]
            self.inventory.update({x:z-y})

    def lookup(self, commodity):
        if commodity in self.inventory.keys():
            return self.inventory.get(commodity)
        else:
            return 0

