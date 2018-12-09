##Blackjack exercise.

import random
x = 1
CardNum = {2, 3, 4, 5, 6, 7, 9, 'Jack', 'King', 'Queen', 'Ace'}
CardSuit = {'Clubs','Hearts', 'Diamonds','Spades'}
#Reference deck
originaldeck = []

for x in CardNum:
    for y in CardSuit:
        originaldeck.append(str(x) + ' of ' + str(y))

productiondeck = originaldeck



print("")
print("")
print("")

def DrawPlayerCards():
    playercard1 = (random.choice(productiondeck))
    playercard2 = (random.choice(productiondeck))
    productiondeck.remove(playercard1)
    productiondeck.remove(playercard2)
    print(playercard1)
    print(playercard2)

for x in productiondeck:
    print(x)

