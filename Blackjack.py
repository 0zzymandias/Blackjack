##Blackjack exercise.

import random

playerbalance = 500
bet = 25

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

resolved = 'false'

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
        
        #Call the player hand from above. Add the actual value of the card to it.
        global playerhandvalue
        playerhandvalue += HandValueCounter(hit, playerhandvalue)
        
        playerhand.append(hit)

 
        #Log the card value to the split container. If both containers equal each other, the player can split cards.
        splitchecker = int(HandValueCounter(hit, playerhandvalue))
        print(hit)
        return splitchecker
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
playersplitchecker1 = (PlayerHit(playersplitchecker1))
playersplitchecker2 = (PlayerHit(playersplitchecker2))
print('Total:')
print(playerhandvalue)
print('')



#Determine first-card events.
evenmoneyevent = 0 
answeredcorrectly = 'false'
#if int(playerhandvalue) == 21 and (int(dealerhandvalue+10) == 21 or int(dealerhandvalue+10) == 20):


if 1 == 1:
        evenmoneyevent = 1
        print('Even money? (Yes or no)')
        x = input()
        x = x.lower()
        if (x == 'no') or (x == 'yes'):
                answeredcorrectly='true'
        while (answeredcorrectly == 'false'):
                print('Even money? (Yes or no)')
                x = input()
                x = x.lower()
                if (x == 'no') or (x == 'yes'):
                        answeredcorrectly='true'
        if x == 'yes':
                playerbalance += bet
                print('+'+ str(bet))
        if x == 'no':
                evenmoneyevent = 0
                
print('End!')
#if int(playerhandvalue) == 21 and int(evenmoneyevent) == 0 and int(dealerhandvalue) != 21:
 #       print('Blackjack!')
        
#if evenmoneyevent == 0 and (int(dealerhandvalue+10) == 21 or int(dealerhandvalue+10) == 20):
 #       print('Insurance?')



#while resolved = False
 #       if int(playersplitchecker1) == int(playersplitchecker2):
  #              print('You can split.')

   #     print('Which action will you take?')
    #    print('Hit (1), Stay (2), Split (3), or Double?(4)')
