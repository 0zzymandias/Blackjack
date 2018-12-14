##Blackjack exercise.

import random

#Card combinations in their own dictionaries
CardNum = {2, 3, 4, 5, 6, 7, 9, 10, 'Jack', 'King', 'Queen', 'Ace'}
CardSuit = {'Clubs','Hearts', 'Diamonds','Spades'}

#Reference deck, zeroed
originaldeck = []

#Zeroed hand values
playerhand = []
dealerhand = []
playerhandvalue = 0
dealerhandvalue = 0

playersplitchecker1 = 0
playersplitchecker2 = 0


#Add all card combinations to a list
for x in CardNum:
    for y in CardSuit:
        originaldeck.append(str(x) + ' of ' + str(y))

#################################################
#Find all cards and assign value to the hand, assuming aces can go both high and low.
#Because strings are immutable in Python, we have to "punch" used cards from the original reference hand.
#Else, we will count only the highest card twice.
def HandValueCounter(drawncard, handvalue_numeric):
        if 'Ace' in drawncard and handvalue_numeric < 11:
                return 11
        if 'Ace' in drawncard and handvalue_numeric >= 11:
                return 1
        if 'Queen' in drawncard:
                return 10
        if 'King' in drawncard:
                return 10
        if 'Jack' in drawncard:
                return 10
        if '10' in drawncard:
                return 10
        if '9' in drawncard:
                return 9
        if '8' in drawncard:
                return 8
        if '7' in drawncard:
                return 7
        if '6' in drawncard:
                return 6
        if '5' in drawncard:
                return 5
        if '4' in drawncard:
                return 4
        if '3' in drawncard:
                return 3
        if '2' in drawncard:
                return 2

#Player hits to their own lists.
def PlayerHit(splitchecker):
        hit = (random.choice(originaldeck))
        originaldeck.remove(hit)
        global playerhandvalue
        playerhandvalue += HandValueCounter(hit, playerhandvalue)
        splitchecker = 0
        splitchecker += int(HandValueCounter(hit, playerhandvalue))
        playerhand.append(hit)
        print(hit)
#Dealer hits to their own lists.
def DealerHit():
        hit = (random.choice(originaldeck))
        originaldeck.remove(hit)
        global dealerhandvalue
        dealerhandvalue += HandValueCounter(hit, dealerhandvalue)
        dealerhand.append(hit)
        print(hit)



#Actual game thus far
print('')
print('Dealer has:')
DealerHit()
print("and a hidden card")
print('')
print('Dealer count estimate: ' + str(dealerhandvalue+10)) #Add a ten to the dealer count estimate.
print('(Always assume the dealer is hiding a 10.)') 
print('')


print("You have:")
PlayerHit(playersplitchecker1)
PlayerHit(playersplitchecker2)
print('Total:')
print(playerhandvalue)


print(playersplitchecker1)
print(playersplitchecker2)
if int(playersplitchecker1) == int(playersplitchecker2):
        print('You can split.')

print('Which action will you take?')
print('Hit (1), Stay (2), Split (3), or Double?(4)')
