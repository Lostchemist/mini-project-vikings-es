import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        self.strength = strength
        return self.strength
        
    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        #Health and Strengh son variables heredadas del padre
        super().__init__(health)
        super().__init__(strength)

    def attack(self):
        return "Odin Owns You All!"
    
    def battleCry(self):
        return "¡Odin os posee a todos!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} ha recibido {damage} puntos de daño"
        else:
            return f"{self.name} ha muerto en acto de combate"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health)
        super().__init__(strength)
        

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"Un 'Saxon' ha recibido {damage} puntos de daño"
        else:
            return f"Un 'Saxon' ha muerto en combate"

# Davicente

class War():
    def __init__(self):
        vikingArmy = []
        saxonArmy = []

    def addViking(self, viking):
        vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        saxonArmy.append(saxon)
    
    def vikingAttack(self):
        #Guardamos las instancias de vikings y saxons en las listas correspondientes
        elegidoSaxon = random.choice(saxonArmy)
        elegidoViking = random.choice(vikingArmy)
        #Invocamos el methodo recieveDamage sobre el saxon elegido con methodo random
        elegidoSaxon.recieveDamage(elegidoViking.strength)
        #Comprobamos si aun esta vivo el saxon
        if elegidoSaxo.health  < 1:
            saxonArmy.remove(saxonElegido)
        return elegidoViking.strength
    
    def saxonAttack(self):
        #Guardamos las instancias de vikings y saxons en las listas correspondientes
        elegidoSaxon = random.choice(saxonArmy)
        elegidoViking = random.choice(vikingArmy)
        #Invocamos el methodo recieveDamage sobre el viking elegido con methodo random
        elegidoViking.recieveDamage(elegidoSaxon.strength)
        #Comprobamos si aun esta vivo el Viking
        if elegidoViking.health  < 1:
            vikingArmy.remove(elegidoViking)
        return elegidoSaxon.strength

    def showStatus(self):
        if vikingArmy.len()==0:
            return f"Los Sajones han luchado por sus vidas y sobreviven otro día..."
        elif saxonArmy.len()==0:
            return f"¡Los Vikingos han ganado la guerra del siglo!"
        else:
            return f"Los Vikingos y los Sajones todavía están en plena batalla."
    pass

#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass


