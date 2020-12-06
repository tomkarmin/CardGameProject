
from random import randint

from Deck_of_cards import Deck_Of_Cards


class Player:
    def __init__(self, name, numOfCards=10):
        self.name = name
        self.package = Deck_Of_Cards(fill=False)
        if numOfCards > 26:
            numOfCards = 26
        self.numOfCards = numOfCards

    def __len__(self):
        return len(self.package)

    def setHand(self, deck1):
        for i in range(self.numOfCards):
            self.package.card_list.append(deck1.deal_one())

    def getCard(self):
        return self.package.deal_one()

    def addCard(self, c):
        self.package.card_list.append(c)

    def show(self):
        print(f"player's name: {self.name} "
              f"and player's cards package: {self.package}")


def main():
    player = Player("Tom")
    player.show()

    deck = Deck_Of_Cards()
    player.setHand(deck)
    player.show()


if __name__ == "__main__":
    main()
