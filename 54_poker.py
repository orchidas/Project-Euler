# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:33:35 2016

@author: ORCHISAMA
"""
# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; 
# for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, 
# for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.

# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards 
# (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume 
# that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, 
# and in each hand there is a clear winner.

# How many hands does Player 1 win?


#setting rank
rank = dict()
rank['high card'] = 0
rank['one pair'] = 1
rank['two pairs'] = 2
rank['three of a kind'] = 3
rank['straight'] = 4
rank['flush'] = 5
rank['full house'] = 6
rank['four of a kind'] = 7
rank['straight flush'] = 8
rank['royal flush'] = 9

#setting order of card values
valueOrder = dict()
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
for i in range(len(values)):
    valueOrder[values[i]] = i

    

def cardExists(v,v_or_s,cards):
    for card in cards:
        if card[v_or_s] == v:
            return True
    return False        
 
def checkSameSuit(cards):
    suit = cards[0][1]
    for card in cards:
        if card[1] != suit:
            return False
    return True        

def checkConsecutive(cards):
    order = list()
    for card in cards:
        order.append(valueOrder[card[0]])
    order.sort()
    
    for i in range(len(order) - 1):
        if order[i+1] - order[i] != 1:
            return False
    return True
    
def checkofaKind(cards,num):
    value = list()
    for card in cards:
        value.append(card[0])
    lst = list()
    for item in value:
        if value.count(item) == num:
            lst.append(item)
    
    if len(lst) > 0:
        return (True, lst)
    return (False, )
            
    
def findHighestCard(cards):
    order = list()
    for card in cards:
        order.append(valueOrder[card[0]])
    return max(order)
    
    
          
def findRankFromHand(cards):
    
    #check for royal flush
    if cardExists('A',0,cards) and cardExists('K',0,cards) and 
    cardExists('Q',0,cards) and cardExists('J',0,cards) and cardExists('T',0,cards):
        return (rank['royal flush'], )
    
    #check for straight flush
    if checkSameSuit(cards) and checkConsecutive(cards):
        return (rank['straight flush'], )
        
    #check for four of a kind
    foursame = checkofaKind(cards,4)
    if foursame[0] is True:
        return (rank['four of a kind'], foursame[1][0])
        
    #check for fullHouse
    threesame = checkofaKind(cards,3)
    onepair = checkofaKind(cards,2)
    if threesame[0] is True and onepair[0] is True:
        return (rank['full house'], threesame[1][0], onepair[1][0])
        
    #check for flush
    if checkSameSuit(cards) is True:
        return (rank['flush'], )
        
    #check if Straight
    if checkConsecutive(cards) is True:
        return (rank['straight'], )
    
    #check if three of a kind
    threesame = checkofaKind(cards,3)
    if threesame[0] is True:
        return (rank['three of a kind'], threesame[1][0])
        
    #check for two pairs
    twopairs = checkofaKind(cards,2)
    if twopairs[0] is True and len(twopairs[1]) == 4:
        return (rank['two pairs'], twopairs[1][0])
        
    #check for a pair
    onepair = checkofaKind(cards,2)
    if onepair[0] is True and len(onepair[1]) == 2:
        return (rank['one pair'], onepair[1][0])
    
    #return highest card
    return (rank['high card'],findHighestCard(cards))
    
        
    
#reading from file
fh = open('poker.txt','r')
count1 = 0
count2 = 0

for line in fh:
    
    card = line.split()
    player1 = list()
    player2 = list()
    for i in range(5):
        player1.append(card[i])
        player2.append(card[5+i])

    tuple_player1 = findRankFromHand(player1)
    tuple_player2 = findRankFromHand(player2)
    if tuple_player1[0] > tuple_player2[0]:
        count1 += 1
    elif tuple_player1[0] < tuple_player2[0]:
        count2 += 1
    #there can be a draw in ranks only if the ranks are
    #four of a kind, full house, three of a kind, two pairs, one pair or high card.
    #In that case we must determine the value of the card, and choose the winner
    else:        
        if tuple_player1[1] > tuple_player2[1]:
            count1 += 1
        elif tuple_player1[1] < tuple_player2[1]:
            count2 += 1
        else:           
            try:
                if len(tuple_player1) > 2:
                    if tuple_player1[2] > tuple_player2[2]:
                        count1 += 1
                    elif tuple_player1[2] < tuple_player2[2]:
                        count2 += 1 
                    else: 
                        card1 = findHighestCard(player1)
                        card2 = findHighestCard(player2)
                        if card1 > card2:
                            count1 += 1
                        else:
                            count2 += 2
                else:                    
                    card1 = findHighestCard(player1)
                    card2 = findHighestCard(player2)
                    if card1 > card2:
                        count1 += 1
                    else:
                        count2 += 2
                    
            except:
                print player1, player2
                print tuple_player1[0], tuple_player2[0]
                break
            
    
print 'Player 1 wins' , count1, 'times'
print 'Player 2 wins', count2,' times'
  
  
#print findRankFromHand(['TS','KH','QC','AS','JH'])
#print findRankFromHand(['3S','6S','4S','5S','2S']) 
#print findRankFromHand(['4S','5S','4H','4C','4D'])
#print findRankFromHand(['3S','3D','3H','2S','2D'])   
#print findRankFromHand(['3S','5S','JS','AS','TS'])    
#print findRankFromHand(['3S','4D','9H','TS','2C'])
    

    

    
        
    
    