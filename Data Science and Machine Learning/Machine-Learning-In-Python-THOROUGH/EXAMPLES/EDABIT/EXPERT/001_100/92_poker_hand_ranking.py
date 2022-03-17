"""
https://edabit.com/challenge/C6pHyc4iN6BNzmhsM
Poker Hand Ranking
In this challenge, you have to establish which kind of Poker combination is present in a deck of five cards. Every card is a string containing the card value (with the upper-case initial for face-cards) and the lower-case initial for suits, as in the examples below:

"Ah" ➞ Ace of hearts
"Ks" ➞ King of spades
"3d" ➞ Three of diamonds
"Qc" ➞ Queen of clubs
There are 10 different combinations. Here's the list, in decreasing order of importance:

Name	Description
Royal Flush	A, K, Q, J, 10, all with the same suit.
Straight Flush	Five cards in sequence, all with the same suit.
Four of a Kind	Four cards of the same rank.
Full House	Three of a Kind with a Pair.
Flush	Any five cards of the same suit, not in sequence.
Straight	Five cards in a sequence, but not of the same suit.
Three of a Kind	Three cards of the same rank.
Two Pair	Two different Pair.
Pair	Two cards of the same rank.
High Card	No other valid combination.
Given a list hand containing five strings being the cards, implement a function that returns a string with the name of the highest combination obtained, accordingly to the table above.

Examples
poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) ➞ "Royal Flush"

poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) ➞ "High Card"

poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) ➞ "Four of a Kind"
"""
def poker_hand_ranking(hand):
    
    dict_hand = {(1,4): "Four of a Kind",
             (2,3): "Full House",
             (1,1,3) : "Three of a Kind",
             (1,2,2) : "Two Pair",
             (1,1,1,2) : "Pair",
             (1,1,1,1,1) : "High Card"
            }    
        
    value_rank = ["1","2", "3", "4", "5","6", "7", "8","9","10", "J", "Q", "K","A"]
    
    value_index = []
    for i in hand:
        value_index.append(value_rank.index(i[:-1]))
    value_index = sorted(value_index)
    
    symbol = []
    for i in hand:
        symbol.append(i[-1])
   
    len_sym = len(set(symbol))
        
    deck, deck_temp = [], []
    for i in (value_index):
        if not i in deck_temp:
            deck_temp.append(i)
            deck.append(value_index.count((i)))

    if len(set(value_index))== 5:
        if (value_index[-1]) - (value_index[0]) == 4 : 
            if len_sym == 1:
                if value_index[0] == 9: 
                    return "Royal Flush"
                else:
                    return "Straight Flush"   
            else: return "Straight"
    
    if len_sym == 1:return "Flush" 
    
    else:
        return dict_hand[tuple(sorted(deck))]


poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) #➞ "Royal Flush"
#poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) #➞ "High Card"
#poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) #➞ "Four of a Kind"
