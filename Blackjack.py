##Blackjack exercise.

import random

CardNum = {2, 3, 4, 5, 6, 7, 9, 'Jack', 'King', 'Queen', 'Ace'}
CardSuit = {'Clubs','Hearts', 'Diamonds','Spades'}
#Reference deck
originaldeck = []

for x in CardNum:
    for y in CardSuit:
        originaldeck.append(str(x) + ' of ' + str(y))

def Hit():
        hit = (random.choice(originaldeck))
        originaldeck.remove(hit)
        print(hit)
        return hit
print('')
print('Dealer has:')
dealerhand = Hit()
print("and a hidden card")
print('')

print("You have:")
playerhand = Hit()
playerhand = Hit()
print("")


print('=')