##Blackjack exercise.

import random

CardNum = {2, 3, 4, 5, 6, 7, 9, 'Jack', 'King', 'Queen', 'Ace'}
CardSuit = {'Clubs','Hearts', 'Diamonds','Spades'}
#Reference deck
originaldeck = []

#Zeroed hand values
playerhand = []
dealerhand = []
playerhandvalue = 0
dealerhandvalue = 0


for x in CardNum:
    for y in CardSuit:
        originaldeck.append(str(x) + ' of ' + str(y))

def PlayerHit():
        hit = (random.choice(originaldeck))
        originaldeck.remove(hit)
        playerhand.append(hit)
        print(hit)
def DealerHit():
        hit = (random.choice(originaldeck))
        originaldeck.remove(hit)
        dealerhand.append(hit)
        print(hit)

print('')
print('Dealer has:')
DealerHit()
print("and a hidden card")
print('')

print("You have:")
PlayerHit()
PlayerHit()
print("")

print('=')



def HandValueCounter(hand, handvaluecounter):
        if ('Ace' in hand) and (handvaluecounter < 11):
                handvaluecounter+=11
        elif ('Ace' in hand) and (handvaluecounter >= 11):
                        handvaluecounter+=1
        print(handvaluecounter)

HandValueCounter(playerhand, playerhandvalue)