from vikingsClasses import Soldier, Viking, Saxon, War
import random

soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura", 'Thor', 'Odin', 'Loki', 'Freyja', 'Baldr', 'Frigg', 'Freyr', 'Heimdallr', 'Tyr', 'Sif']
war_instance = War()
# temp = Viking("Ana", 100, 100)
# print(random.randint(1,100))
# war_instance.addViking(temp)


#Create 5 Vikings
for i in range(0,5):
    temp=Viking(soldier_names[random.randint(0,len(soldier_names))],100,random.randint(0,100))
    war_instance.addViking(temp)



#Create 5 Saxons
for i in range(0,5):
    war_instance.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0

#Run the WAAAAAAR
while war_instance.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    war_instance.vikingAttack()
    war_instance.saxonAttack()
    print(f"\n\n\n round: {round}  \n Viking army: {len(war_instance.vikingArmy)} warriors",f"and Saxon army: {len(war_instance.saxonArmy)} warriors")
    print(war_instance.showStatus())
    round += 1
"""
"""