from card import Card
from hand import Hand
from deck import Deck
import random

def main():
    TABLE_MIN = 100
    you_points = TABLE_MIN
    cpu_points = TABLE_MIN

    play_more = "y"

    print('\nSCORES: ')
    print(f'You: {you_points:4>}')
    print(f'CPU: {cpu_points:4>}', end='\n\n') # Leave empty line.

    while play_more[0].lower() != 'n' and you_points > 0 and cpu_points > 0:
        # Create and shuffle the deck.
        deck = Deck()
        deck.shuffle()

        # Create hands for each player.
        you = Hand()
        cpu = Hand()

        # Deal 5 cards to each player.
        for i in range(5):
            you.add_card(deck.deal())
            cpu.add_card(deck.deal())
        
        # Show the player their cards.
        print(f' Your hand: {you.show_hand()}', end='\n\n')

        # Simplified one-shot betting.
        cpu_wager = random.randint(1, cpu_points)
        print(f'       CPU wagers: {cpu_wager}')
        you_wager = int(input('What do you wager? '))

        print(f'\nCPU\'s hand: {cpu.show_hand()}')

        # Compare the hands.
        if you < cpu:
            print('\nYou win!', '\N{GRINNING FACE}')
            you_points += cpu_wager
            cpu_points -= cpu_wager
        elif cpu < you:
            print('\nCPU wins!', '\N{WORRIED FACE}')
            cpu_points += you_wager
            you_points -= you_wager
        else:
            print('\nTIED!')
    
        print('\nSCORES: ')
        print(f' You have: ${you_points:4>}')
        print(f'  CPU has: ${cpu_points:4>}', end='\n\n')
        
        if you_points <= 0 or cpu_points <= 0:
            break

        play_more = input("Play another hand? (y/n) ")
    
    # END WHILE

    if you_points <= 0:
        print('You lost everything!', '\N{MONEY WITH WINGS}')
    elif cpu_points <= 0:
        print('You won everything from the computer!', '\N{MONEY BAG}')
    else:
        print('Quit before you\'re broke. Good move.')


def test_main():
    # Some test cases:
    i = 0
    # Royal Flush
    p3 = Hand()
    p3.add_card(Card('hearts', 10))
    p3.add_card(Card('hearts', 11))
    p3.add_card(Card('hearts', 13))
    p3.add_card(Card('hearts', 12))
    p3.add_card(Card('hearts', 14))
    print(f'Test Hand {i}: ', end='')
    i += 1
    p3.show_hand()

    # Flush
    p4 = Hand()
    p4.add_card(Card('clubs', 3))
    p4.add_card(Card('clubs', 7))
    p4.add_card(Card('clubs', 4))
    p4.add_card(Card('clubs', 6))
    p4.add_card(Card('clubs', 5))
    print(f'Test Hand {i}: ', end='')
    i += 1
    p4.show_hand()

    # Full House
    p4 = Hand()
    p4.add_card(Card('spades',  8))
    p4.add_card(Card('spades',  2))    
    p4.add_card(Card('diamonds',8))
    p4.add_card(Card('hearts',  8))
    p4.add_card(Card('clubs',   2))
    print(f'Test Hand {i}: ', end='')
    i += 1
    p4.show_hand()

    # Two pair
    p5 = Hand()
    p5.add_card(Card('spades', 7))
    p5.add_card(Card('spades', 9))
    p5.add_card(Card('hearts', 7))
    p5.add_card(Card('hearts', 9))
    p5.add_card(Card('clubs',  3))
    print(f'Test Hand {i}: ', end='')
    i += 1

    p5.show_hand()

    # Two pair, another
    p6 = Hand()
    p6.add_card(Card('diamonds', 3))
    p6.add_card(Card('hearts',   3))
    p6.add_card(Card('diamonds',13))
    p6.add_card(Card('diamonds', 3))
    p6.add_card(Card('clubs',   13))
    print(f'Test Hand {i}: ', end='')
    i += 1
    p6.show_hand()
    
    # if p4 < p5:
    #     print('Player 4 wins.')
    # else:
    #     print('Player 5 wins.')

    # if p5 < p6:
    #     print('Player 5 wins.')
    # else:
    #     print('Player 6 wins.')


if __name__ == '__main__':
    main()
