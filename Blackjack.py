##Blackjack exercise.

import random
import time

playerbalance = 500
bet = 25
#Card combinations in their own dictionaries
#
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

#Player hits to their own lists, checking for splits.
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

def PlayerHit2():
        hit = (random.choice(originaldeck))
        originaldeck.remove(hit)
        
        #Call the player hand from above. Add the actual value of the card to it.
        global playerhandvalue
        playerhandvalue += HandValueCounter(hit, playerhandvalue)
        
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

#Check if the hand is soft; 
def AceCheck(currenthand):
        global handace
        x = str(currenthand)
        if 'Ace' in x:
                handace = 'Soft'
        if 'Ace' not in x:
                handace = 'Hard'

hand = 'unresolved'
handace = 'Undefined' 

#Actual game thus far
print('')
print('Dealer has:')
DealerHit()
print("and a hidden card")
print('')
print('Dealer count estimate: ' + str(dealerhandvalue+10)) #Add a ten to the dealer count estimate.
print('(Assume the dealer is hiding a 10, but not always. (House edge in always making this assumption: 10.03%))') 
print('')


print("You have:")
playersplitchecker1 = (PlayerHit(playersplitchecker1))
playersplitchecker2 = (PlayerHit(playersplitchecker2))
print('Total:')
print(playerhandvalue)

AceCheck(playerhand)

#Determine first-card events.
evenmoneyevent = 0 
answeredcorrectly = 'false'

answeredcorrectly = 'false'
#Before any action is taken, prompt even-money event in the case of dual-blackjacks.
if int(playerhandvalue) == 21 and (int(dealerhandvalue+10) == 21 or int(dealerhandvalue+10) == 20):
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
                print('')
                print('Dealer flips over their card...')
                time.sleep(0.5)
                DealerHit()
        if dealerhandvalue == playerhandvalue:
                print('The game ends in a push.')
print('')


#Current issues with Soft 21 busting. (K+A)

if int(playerhandvalue) == 21 and int(evenmoneyevent) == 0 and int(dealerhandvalue) != 21:
       print('Blackjack!')
        
if evenmoneyevent == 0 and (int(dealerhandvalue+10) == 21 or int(dealerhandvalue+10) == 20):
       print('Insurance?')



#while resolved = False
if int(playersplitchecker1) == int(playersplitchecker2):
        print('You can split.')


while hand != 'resolved':
        print('')
        print('Current hand value:')
        print(str(handace) + ' ' + str(playerhandvalue))
        print('Hit (1), Stay (2), Split (3), Double (4)')
        action = input('Choice: #')
        
        #Hit
        if action == '1':
                #Draw card
                PlayerHit2()
                #Player busts on hard card
                if playerhandvalue > 21 and handace == 'Hard':
                        print(playerhandvalue)
                        print('======')
                        print('Busted!')
                        print('======')
                        print('Dealer had a total of...')
                        print(dealerhandvalue)
                        hand = 'resolved'
                #Player has actions remaining
                if playerhandvalue < 21:
                        print('What will you do?')
                #Player uses up soft ace
                if playerhandvalue > 21 and handace == 'Soft':
                        playerhandvalue = playerhandvalue - 10
                        handace = 'Hard'
        #Stand
        if action == '2':
                print('')
                print('Dealer flips over their card...')
                time.sleep(0.5)
                DealerHit()
                print('Dealer has '+str(dealerhandvalue)+'.')
                while dealerhandvalue < 17:
                        DealerHit()
                        print('Dealer flips over their card...')
                        time.sleep(0.5)
                        print('Dealer has '+str(dealerhandvalue)+'.')
                if dealerhandvalue > playerhandvalue and dealerhandvalue <=21:
                        print('Dealer has won with '+str(dealerhandvalue)+'.')
                        hand = 'resolved'
                if dealerhandvalue > 21:
                        print('Dealer has busted with '+str(dealerhandvalue)+'!')
                        hand = 'resolved'
                if playerhandvalue > dealerhandvalue:
                        print('Player has won with '+str(playerhandvalue)+'!')
                        hand = 'resolved'
                if dealerhandvalue == playerhandvalue:
                        print('Push!')
                        hand = 'resolved'
        #Split
        #if action = '3':
        #Double
        #if action = '4':


#Note to self: you may want to create card slots for each hand. 6 card Charlie is statistically improbable.

action = input('Done with hand!')
                


                





print('End!')