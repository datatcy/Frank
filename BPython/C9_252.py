# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:07:17 2017

@author: FPaulraj
"""

class Card(object):
    RANKS =["A","2","3","4","5","6","7","8","10","J","K","Q"]
    SUITS=["c","d","h","s"]
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def __str__(self):
        rep=self.rank+self.suit
        return rep

class Hand(object):
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep=""
            for card in self.cards:
                rep +=str(card)+ " "
        else:
            rep="<empty>"
        return  rep
    def clear(self):
        self.cards=[]
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
"""Example for Inhereting from base class/ creating derived class  """
class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self,hands,per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Can't contnue deal, out of cards!")

""" Overriding Base Class Method """
class Unprintable(Card):
    def __str__(self):
        return "<unprintable>"
    
"""  Invoking Base Class Method  """
class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=True):
        super(Positionable_Card,self).__init__(rank,suit)
        self.is_face_up=face_up
    def __str__(self):
        if self.is_face_up:
            rep= super(Positionable_Card,self).__str__()
        else:
            rep="XX"
        return rep
    def flop(self):
        self.is_face_up=not self.is_face_up   
    
card1=Card(rank="A", suit="c")
print("printing a card object")
print(card1)
        
card2=Card(rank="2", suit="c")
card3=Card(rank="3", suit="c")
card4=Card(rank="4", suit="c")
card5=Card(rank="5", suit="c")
print("\nPrining the rest of the objects individually:")
print(card2)
print(card3)
print(card4)
print(card5)
my_hand=Hand()
print("\n Printing my hand before i add any cards:")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\n Printing my hand after adding 5 cards")
print(my_hand)

your_hand=Hand()
my_hand.give(card1,your_hand)
my_hand.give(card2,your_hand)
print("\n Gave the first two cards form my hand to your hand")
print("your hand :")
print(your_hand)
print("My hand")
print(my_hand)
my_hand.clear()
print("\n My hand after clearing it:")
print(my_hand)
"""Using DECK class"""
deck1=Deck()
print("Created a new deck:")
print(deck1)
deck1.populate()
print("Populated Deck")
print(deck1)
deck1.shuffle()
print("\n Shuffled the deck")
print(deck1)
my_hand=Hand()
your_hand=Hand()
hands=[my_hand,your_hand]
deck1.deal(hands,per_hand=5)
print("\n Dealt 5 cards to my hand and your hand:")
print("My hand")
print(my_hand)
print("Your Hand:")
print(your_hand)
print("Deck")
print(deck1)
deck1.clear()
print(deck1)
""" Overriding base class methods"""
card1=Card("A","c")
card2=Unprintable("A","d")
card3=Positionable_Card("A","h")

print("\n Printing a Card Object")
print(card1)
print("\n Printing an Unprintable card object")
print(card2)
print("\n Printing an Positionalble card object")
print(card3)
card3.flop()
print("\n Printing an after flip")
print(card3)
