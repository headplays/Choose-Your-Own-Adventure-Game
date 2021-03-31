#imports
import time
import os

#inventory
inventory=[]


#variables
attackDamage = 0
coppersword = "coppersword"

answer = input ("Would you like to play? (yes/no)")

if answer.lower().strip() == "yes":

    print ("Welcome to Sillohoute of the Tomb Robber")
    os.system ("pause")
    print ("Objective: find the radio transmitter to contact help")
    os.system ("pause")
    print ("Tomb 1")
    time.sleep(2) 

    answer = input ("Do you want to enter (yes/no)")

    if answer.lower().strip() == "yes":

            print ("You venture deep in")
            time.sleep(2)
            print ("You see a chest ")
            time.sleep(1)
            
            answer = input ("Do you want to loot it? (yes/no/examine)")

            if answer.lower().strip() == "yes":
                
                print ("The chest was rigged with explosives. You died")
                
            if answer.lower().strip() == "no":

                print ("You skip the chest, heading deeper into the cave")

            if answer.lower().strip() == "examine":

                answer = input ("You discover the chest is rigged with explosives (skip/defuse)")   

                if answer.lower().strip() == "skip":

                    print ("You skip the chest, heading deeper into the cave")

                if answer.lower().strip() == "defuse":

                    print ("You successfully defuse the trap")
                    time.sleep(1)
                    answer = input ("You found coppersword (grab/leave)")

                    if answer.lower().strip() == "grab":
                            inventory.append(coppersword)
                            attackDamage = attackDamage + 5
                            time.sleep(1)
                            print ("Your attack damage is now: " + str(attackDamage))
                            print ("Your inventory: " +str(inventory))
                            

    if answer == "no":
            print ("You wait the day out")
    
    else:
            print ("Invalid message. You died")


else:
    print ("Ok. Leave")

def addToInventory(item):
    inventory.append(item)

def printInventory():
    for i in inventory:
        print(i)
