#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle
from itertools import product
import pdb

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
       self.cards = list(product(SUITE,RANKS))

    def shuffleCards(self):
        shuffle(self.cards)

    def split(self):
        halfOne = [card for card in self.cards[::2]]
        halfTwo = [card for card in self.cards[1::2]]
        return (halfOne, halfTwo)

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove(self):
        return self.cards.pop()

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

class Player():

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play(self):
        card = self.hand.remove()
        print("{} has placed: {}".format(self.name,card))
        print("\n")
        return card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards)!=0
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
d = Deck()
d.shuffleCards()
halfOne, halfTwo = d.split()

computer = Player("computer", Hand(halfOne))
name = input("What is your name? ")
player = Player(name, Hand(halfTwo))

total_rounds = 0
war_count = 0

while player.still_has_cards() and computer.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings:")
    print(player.name+" has the count "+str(len(player.hand.cards)))
    print(computer.name+" has the count "+str(len(computer.hand.cards)))
    print("play a card!")
    print("\n")

    table_cards = []

    computer_card = computer.play()
    player_card = player.play()

    table_cards.append(computer_card)
    table_cards.append(player_card)

    if computer_card[1] == player_card[1]:
        war_count += 1

        print("war")
        table_cards.extend(player.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

        if RANKS.index(computer_card[1]) < RANKS.index(player_card[1]):
            player.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)
    else:
        if RANKS.index(computer_card[1]) < RANKS.index(player_card[1]):
            player.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)

print("Game over, number of rounds:" + str(total_rounds))
print("A war happened " + str(war_count) + " times")



# Use the 3 classes along with some logic to play a game of war!
