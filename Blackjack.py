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


#Add all card combinations to a list
for x in CardNum:
    for y in CardSuit:
        originaldeck.append(str(x) + ' of ' + str(y))



#Player hits to their own lists.
def PlayerHit():
        hit = (random.choice(originaldeck))
        originaldeck.remove(hit)
        playerhand.append(hit)
        print(hit)
#Dealer hits to their own lists.
def DealerHit():
        hit = (random.choice(originaldeck))
        originaldeck.remove(hit)
        dealerhand.append(hit)
        print(hit)

#Find all cards and assign value to the hand, assuming aces can go both high and low.
#Stringvalues 
def HandValueCounter(stringvalues, handvalue_numeric):
        if 'Ace' in stringvalues and handvalue_numeric < 11:
                stringvalues.replace('Ace','Counted',1)
                return 11
        if 'Ace' in stringvalues and handvalue_numeric >= 11:
                return 1
        if 'Queen' in stringvalues:
                return 10
        if 'King' in stringvalues:
                return 10
        if 'Jack' in stringvalues:
                return 10
        if '10' in stringvalues:
                return 10
        if '9' in stringvalues:
                return 9
        if '8' in stringvalues:
                return 8
        if '7' in stringvalues:
                return 7
        if '6' in stringvalues:
                return 6
        if '5' in stringvalues:
                return 5
        if '4' in stringvalues:
                return 4
        if '3' in stringvalues:
                return 3
        if '2' in stringvalues:
                return 2


#Because strings are immutable in Python, we have to "punch" used cards from the original reference hand.
#Else, we will count only the highest card twice.



#Actual game thus far
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

#The post-hit dealer and player hands, in string format.
string_dealerhand = str(dealerhand)
string_playerhand = str(playerhand)


playerhandvalue += int(HandValueCounter(string_playerhand, playerhandvalue))
playerhandvalue += int(HandValueCounter(string_playerhand, playerhandvalue))

print('Playerhand')
print(playerhand)
print('Playerhand -> To string')
print(string_playerhand)
print('Player hand numerical value')
print(playerhandvalue)