import random

class Deck(object):

    cards = []

    def __init__(self):
        #self.cards = []
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank + " of " + suit)
        
    def shuffle(self):
        return random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
        
    def size(self):
        return len(self.cards)


d1 = Deck()
d1.shuffle()
number_of_cards = d1.size()

print("Original deck size: " + str(number_of_cards))

for i in range(number_of_cards):
   print(d1.deal())

print("FInal deck size: " + str(d1.size()))

