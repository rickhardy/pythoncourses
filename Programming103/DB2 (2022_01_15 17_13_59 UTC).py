# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 21:42:02 2022

@author: rmh_r
"""

import sqlite3
from random import sample

def read_all_cards():
    result = conn.execute("SELECT * FROM computer")
    return result.fetchall()

def shuffle_pack(cards): 
    #shuffled_deck = random.shuffle(cards) #shuffle does not work on a list of tuples
    shuffled_deck = sample(cards, k=len(cards))
    return shuffled_deck

def take_top_card (deck):
    if len (deck) > 0:
        return deck.pop()
    else:
        return 'empty'

def winning_card (first_card, second_card, category):
    None
    if first_card[category] == second_card[category]:
        return [0,0]
    elif first_card[category] > second_card[category]:
        return [0,1]
    elif first_card[category] < second_card[category]:
        return [1,0]
    else:
        return 'error' #not strictly necessary but good practice to capture all 

conn = sqlite3.connect("computer_cards.db")

deck = shuffle_pack (read_all_cards())

conn.close()

first_card = take_top_card(deck)
second_card = take_top_card(deck)

player1_chooses = True

totals = [0,0]

while  first_card !=  'empty' and second_card !=  'empty':
    
    player1_chooses = not (player1_chooses) # toggle player who chooses
    
    #print (type (deck))
    #print (deck)
    
    if player1_chooses:     
        print ('player 1 Your card is : ', first_card)
    else: 
        print ('player 2 Your card is : ', first_card)
    
    category = int (input ('choose your category 1,2,3,4: '))
    
    print ('Next Card: ',second_card)

    print (first_card[category])
    print (second_card[category])
    
    #this is redundant but I cant see a better way
    first_card = take_top_card(deck)
    second_card = take_top_card(deck)
    
    if player1_chooses :
        scores = winning_card (first_card, second_card, category)
    else:
        scores = winning_card (second_card, first_card, category)
    
    totals[0], totals[1] = totals[0] + scores[0], totals[1] + scores[1] 
    print ('score:',totals)

print ('Not Enough cards to play again')
