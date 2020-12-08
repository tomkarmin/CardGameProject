from class_player import Player
from Deck_of_cards import Deck_Of_Cards
from card_game import CardGame
card=CardGame('tom','itay')
tom=Player('tom',10)
deck=Deck_Of_Cards()


print(len(deck.card_list))

for i in range(11):
    tom.getCard()

