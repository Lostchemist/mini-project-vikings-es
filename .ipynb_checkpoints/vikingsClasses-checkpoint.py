import random
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage  

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        #Health and Strengh son variables heredadas del padre
        super().__init__(health, strength)
        # super().__init__(strength)

    def attack(self):
         
        return self.strength
    
    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        # super().__init__(strength)
        

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        #Guardamos las instancias de vikings y saxons en las listas correspondientes
        self.elegidoSaxon = random.choice(self.saxonArmy)
        self.elegidoViking = random.choice(self.vikingArmy)
        #Invocamos el methodo recieveDamage sobre el saxon elegido con methodo random
        self.elegidoSaxon.receiveDamage(self.elegidoViking.strength)
        #Comprobamos si aun esta vivo el saxon
        if self.elegidoSaxon.health  < 1:
            self.saxonArmy.remove(self.elegidoSaxon)
        #return self.elegidoViking.strength
    
    def saxonAttack(self):
        #Guardamos las instancias de vikings y saxons en las listas correspondientes
        self.elegidoSaxon = random.choice(self.saxonArmy)
        self.elegidoViking = random.choice(self.vikingArmy)
        #Invocamos el methodo recieveDamage sobre el viking elegido con methodo random
        self.elegidoViking.receiveDamage(self.elegidoSaxon.strength)
        #Comprobamos si aun esta vivo el Viking
        if self.elegidoViking.health  < 1:
            self.vikingArmy.remove(self.elegidoViking)
        #return self.elegidoSaxon.strength

    def showStatus(self):
        if len(self.vikingArmy)==0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)==0:
            return f"Vikings have won the war of the century!"
        else:
            return f"Vikings and Saxons are still in the thick of battle."
    pass

# #yop
# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass


