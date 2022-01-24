
import random


gameLenght = 5
summaryGold=0

giftFromBox = ["green box - 1000 gold", "orange box - 4000 gold", "purple box - 9000 gold", "gold box - 16000 gold",]


moveOption = ["CHEST", "NOTHING"]

print("welcome to the chamber, you have five moves!!!")
print()

while 0 < gameLenght:
    gameAnswer=input("Do you wang move forward?[y/n]: ")
    print()
    
    if (gameAnswer == "y"):
        print("great let's see what you got")
        print()
        moveForward = random.choices(moveOption, [60, 40], k=1)[0]
        if (moveForward == "CHEST"):
            boxDraw=random.choices(giftFromBox, [75, 20, 4, 1], k=1)[0]
            print("you found",boxDraw)
            if (boxDraw == "green box - 1000 gold"):
                summaryGold=summaryGold+1000
            elif (boxDraw == "orange box - 4000 gold"):
                summaryGold=summaryGold+4000
            elif (boxDraw == "purple box - 9000 gold"):
                summaryGold=summaryGold+9000
            elif (boxDraw == "gold box - 16000 gold"):
                summaryGold=summaryGold+16000
        elif (moveForward == "NOTHING"):
            print("you didn't found the box")
        gameLenght -= 1
        continue
    elif (gameAnswer == "n"):
        print("you end the game")
        break

print()
print("Gratulation you found",summaryGold,"gold")

        
    
    
'''
gameLenght = 5
print("you have only five move")

while 0 < gameLenght:
    gameAnswer = input("Do you want to move forward? ")
    if (gameAnswer == "y"):
        print("Great, let's see what you got...")
        
        
    else:
        print("you can go just straight")
        continue

    gameLenght -= 1
'''

