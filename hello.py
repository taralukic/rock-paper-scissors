
import sys
import random

player = input("1 for rock\n2 for paper\n3 for scissors\n")
playerchoice = int(player)
if playerchoice > 3 or playerchoice < 1:
    sys.exit("you must enter 1 2 or 3")

computer = random.choice("123")
computerchoice = int(computer)

print("")
print("you chose " + str(playerchoice))
print("computer chose " + str(computerchoice))

if playerchoice == 1 and computerchoice == 3:
    print("🥳 you won")
elif playerchoice == 2 and computerchoice == 1:
    print("🥳 you won")
elif playerchoice == 3 and computerchoice == 2:
    print("🥳 you won")
elif playerchoice == computerchoice:
    print("tie game")
else:
    print("😭 you lost")
