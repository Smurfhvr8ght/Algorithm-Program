class player:
    living = True
    def __init__(self,health,inv,wealth):
        self.health = health
        self.inv = inv
        self.wealth = wealth
    def hp(self,change):
        self.health += change
    def money(self,money):
        self.wealth += money
        if self.health <= 0:
            self.living = False
            print("Dead")
    def addinv(self,item,type):
        self.inv[type] = item
    def reminv(self,inv):
        self.inv.pop(inv)
    def reminvtype(self,type):
        self.inv = {k: v for k, v in self.inv.items() if v != type}
        
#testing below
bob = player(100,{"B bag":"bag","S bag":"bag"},200)
#change hp and lives
bob.hp(-100)
print(bob.health)
print(bob.living)
#change money
bob.money(20)
print(bob.wealth)
#add item
bob.addinv("bag","M bag")
print (bob.inv)
#remove item
bob.reminv("S bag")
print (bob.inv)
#remove item base on type
bob.reminvtype("bag")
print (bob.inv)
