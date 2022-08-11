

from card import Card
import random

class Deck:
    '''
    Gets a deck of card, shuffles and deals them
    '''

    l_cards = []

    #constructor
    def __init__(self):
        for rank in Card.l_rank:
            for suit in Card.l_suit:
                c = Card(rank, suit)
                self.l_cards.append(c)
                
    #returns the string of all cards in deck   
    def __str__(self):
        cards = ""
        for i in range(len(self.l_cards)):
            str_card = str(self.l_cards[i])
            cards += str_card
            
        return cards
            

    def __repr__(self):
        return f'{Deck ({self.l_cards})}'

    #function that resets the deck
    def reset(self):
        self.__init__()

    #function that shuffes the deck
    def shuffle(self):
        d_cards = self.l_cards
        for i in range(len(d_cards)):
            j = random.randint(i,len(d_cards) - 1)
            d_cards[i] ,d_cards[j] = d_cards[j], d_cards[i]

    #function that deals the card from the deck
    def deal(self):
        return self.l_cards.pop()
            
def main():
    d_cards = Deck()
   
    for i in range(5):
        d_cards.shuffle()
        pick_card = d_cards.deal()
        print(pick_card)
        d_cards.reset()
        
    print(d_cards)

if __name__ == "__main__":
    main()
