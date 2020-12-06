import random
from cards.Deck_of_cards import Deck_Of_Cards

from cards.class_player import Player


class CardGame:
    def __init__(self, name1, name2, numCards=10):
        self.deckK = Deck_Of_Cards()
        player1 = Player(name1, numCards)
        player2 = Player(name2, numCards)
        self.player1 = player1
        self.player2 = player2
        self.numCards = numCards
        self.new_game_called = False
        self.new_game()

    def new_game(self):
        if self.new_game_called:
            print("new game called again")
        else:
            self.new_game_called = True
            if self.numCards > 0:
                self.deckK.shuffle()
                self.player1.setHand(self.deckK)
                self.player2.setHand(self.deckK)
            else:
                print("ERROR")
    def get_round_winner(self):
        x = self.player1.getCard()
        y = self.player2.getCard()
        if x > y:
            self.player2.addCard(y)
            self.player2.addCard(x)
            return [self.player1.name, x]
        else:
            self.player1.addCard(y)
            self.player1.addCard(x)
            return [self.player2.name, y]

    def get_winner(self):
        if (len(self.player1.package)==len(self.player2.package)):
            return None
        elif (len(self.player1.package)>len(self.player2.package)):
            return self.player2.name
        else:
            return self.player1.name

    def show(self):
        self.player1.show()
        self.player2.show()
