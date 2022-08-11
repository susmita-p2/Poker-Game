from card import Card
from deck import Deck
import random

class Hand:
    '''
    Defines different hands in poker game and compares them.
    '''

    #constructor
    def __init__(self):
        
        self.l_cards = []
    
    #add cards to the list
    def add_card(self, card):
        self.l_cards.append(card)

    #displays the hand as str
    def show_hand(self):
        s_cards = ""
        for i in range(len(self.l_cards)):
            get_card = str(self.l_cards[i])
            s_cards += get_card

        return s_cards

           
    def __str__(self):
        cards = self.show_hand()

        return cards

    def __repr__(self):
        return f'{Hand({self.s_cards})}'
    
    def four_of_a_kind(self):
        '''
        Checks if a hand is four of a kind.
        (four cards of same face value and one different card)
        Parameters:
        [hand]: A hand object
        Return:
        boolean value [True or False]
        '''
        self.l_cards.sort()
        found_one= True
        found_two = True
        for i in range(4):
            if self.l_cards[i] != self.l_cards[i+1]:
                found_one = False
               
               

        for i in range(1,len(self.l_cards)-1):
            if self.l_cards[i] != self.l_cards[i+1]:
                found_two = False

        if found_one or found_two == True:
            return True

    def three_of_a_kind(self):
        '''
        Checks if a hand is three of a kind.
        (three cards of same face value and two different cards)
        Parameters:
        [hand]: A hand object
        Return:
        boolean value [True or False]
        '''
        
        self.l_cards.sort()
        found_one = True
        found_two = True
        found_three = True

        if self.four_of_a_kind() == True:
            return False

        for i in range(2):
            if self.l_cards[i] != self.l_cards[i+1]:
                found_one = False

        for i in range(1,3):
            if self.l_cards[i] != self.l_cards[i+1]:
                found_two = False

        for i in range(2,len(self.l_cards)-1):
            if self.l_cards[i] != self.l_cards[i+1]:
                found_three = False

        if found_one or found_two or found_three == True:
            return True

    def flush(self):
        '''
        Checks if a hand is flush.
        (all cards of the same suit)
        Parameters:
        [hand]: A hand object
        Return:
        boolean value [True or False]
        '''

        found = True
        for i in range(len(self.l_cards)-1):
            if self.l_cards[i].getSuit() != self.l_cards[i+1].getSuit():
                found = False

        return found

    def straight_flush(self):
        '''
        Checks if a hand is straight flush.
        (five consecutive cards of the same suit)
        Parameters:
        [hand]: A hand object
        Return:
        boolean value [True or False]
        '''

        found = False

        if self.flush() == True and self.straight() == True:
            found = True
           
            

        return found

    def straight(self):
        '''
        Checks if a hand is straight.
        (five consecutive cards)
        Parameters:
        [hand]: A hand object
        Return:
        boolean value [True or False]
        '''

        found = True
        self.l_cards.sort()


        for i in range(len(self.l_cards)-1):
            if not(self.l_cards[i].getRank() + 1 == self.l_cards[i+1].getRank()):
                found = False

        return found

    def one_pair(self):
        '''
        Checks if a hand is one-pair.
        (two of same face value and the remaining three different values)
        Parameters:
        [hand]: A hand object
        Return:
        boolean value [True or False]
        '''

        self.l_cards.sort()
        found = False

        for i in range(len(self.l_cards)-1):
            if self.l_cards[i].getRank() == self.l_cards[i+1].getRank():
                found =  True

        return found

    def two_pair(self):
        '''
        Checks if a hand is two pair.
        (two pairs of same face value and one different card)
        Parameters:
        [hand]: A hand object
        Return:
        boolean value [True or False]
        '''
        
        found_pair1 = False
        found_pair2 = False

        for i in range(len(self.l_cards)-1):
            if found_pair1 and self.l_cards[i].getRank() == self.l_cards[i+1].getRank():
                found_pair2 = True
            if self.l_cards[i].getRank() == self.l_cards[i+1].getRank():
                found_pair1 = True

        return (found_pair1 and found_pair2)

    def full_house(self):
        '''
        Checks if a hand is a full house.
        (has a three of a kind and a pair)
        Parameters:
        [hand]: A hand object
        Return:
        boolean value [True or False]
        '''

        self.l_cards.sort()
        found_house = False

        
        if (self.l_cards[0].getRank() == self.l_cards[1].getRank()) and (self.l_cards[2].getRank() == self.l_cards[4].getRank()):
            found_house = True

        elif (self.l_cards[0].getRank() == self.l_cards[2].getRank()) and (self.l_cards[3].getRank() == self.l_cards[4].getRank()):
            found_house = True

    
          
    #ranks the hands by highest order to least
    def hand_value(self):
        value = 0
        
        if self.straight_flush():
            value = 1

        elif self.four_of_a_kind():
            value = 2
            
        elif self.full_house():
            value = 3

        elif self.flush():
            value = 4

        elif self.straight():
            value = 5

        elif self.three_of_a_kind():
            value = 6

        elif self.two_pair():
            value = 7

        elif self.one_pair():
            value = 8

        else:
            value = 9

        return value

    #comparison function
    def __lt__(self,other):
        return self.hand_value() < other.hand_value()

  
             


            

        
    
                

            
                
                
                
            
        
        

            
                
            
        
               
            
           
       

        
