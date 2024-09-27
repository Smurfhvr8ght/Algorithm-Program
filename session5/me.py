import random

#class for vehicle that moves in a 2d plane but there is chance of breaking down
class AW:
    #initial value
    x=0
    y=0
    def __init__(self,vehicle,durability,failchance):
       self.vehicle = vehicle
       self.durability = durability
       self.chance = failchance

    #moving in the x-axis
    def xmove(self,x):
        move = abs(x)
        if self.durability >= 0:
            for i in range(move):
                if x>0:
                    self.x += 1
                elif x<0:
                    self.x -=1
                if random.randint(1,100) <= self.chance:
                    self.durability -= 1
                    if self.durability <= 0:
                        print (self.vehicle,"is broken")
                        break
        else:
            print(self.vehicle,"is broken")

    #moving in the y-axis
    def ymove(self,y):
        move = abs(y)
        if self.durability >= 0:
            for i in range(move):
                if y>0:
                    self.y += 1
                elif y<0:
                    self.y -=1
                if random.randint(1,100) <= self.chance:
                    self.durability -= 1
                    if self.durability <= 0:
                        print (self.vehicle,"is broken")
                        break
        else:
            print(self.vehicle,"is broken")

    #display info on vehicle
    def info(self):
        print ("vehicle:",self.vehicle)
        if self.durability <= 0:
            print ("condition: broken")
        else:
            print ("condition: working (durability:",str(self.durability) +")")
        print ("Coordinate: (" + str(self.x) + ", "+ str(self.y)+")")

    #add durability
    def improve(self,fix):
        self.durability += fix

    #reduce durability
    def dmg(self,dmg):
        for i in range(dmg):
            if self.durability > 0:
                self.durability -= 1
            else:
                break
