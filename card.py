#Susmita Poudel
#May 09, 2022
#This lab represents the suit and face of a card.

class Card:
    '''
    Represents the face value and suit of card in a deck. 
    '''

    l_suit = ['spades', 'clubs', 'diamonds', 'hearts']
    l_rank = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    
    #constructor 
    def __init__(self,rank, suit):
        
        self.rank = rank
        self.suit = suit
        
    #string representation
        
    def __str__(self):
        if self.rank == 11:
            rank_str = 'J'

        elif self.rank == 12:
            rank_str = 'Q'

        elif self.rank == 13:
            rank_str = 'K'

        elif self.rank == 14:
            rank_str = 'A'

        else:
            rank_str = str(self.rank)


        if self.suit == 'spades':
            suit_symbol = f'{rank_str}\N{BLACK SPADE SUIT}'

        elif self.suit == 'clubs':
            suit_symbol = f'{rank_str}\N{BLACK CLUB SUIT}'

        elif self.suit == 'diamonds':
            suit_symbol = f'{rank_str}\N{BLACK DIAMOND SUIT}'

        else:
            suit_symbol = f'{rank_str}\N{BLACK HEART SUIT}' 

        return suit_symbol 


    def __repr__(self):
        return f'{Card({self.rank}, {self.suit})}'
    
    #function  to get the suit of card
    def getSuit(self):
        return self.suit

    #function to get the face value of card
    def getRank(self):
        return self.rank
    #comparison function
    def __lt__(self, other):
        return self.rank < other.rank


def main():
    c1 = Card(12, 'diamonds')
    c2 = Card(14, 'spades')
    print(c1)
    print(c2)


    if c1 < c2:
        print(f'{c2} beats {c1}')
    else:
        print(f'{c1} beats {c2}')


if __name__ == '__main__':
    
    main()
            

    
