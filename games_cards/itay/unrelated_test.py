from games_cards.itay.class_player import Player
from games_cards.itay.Deck_of_cards import Deck_Of_Cards
tom=Player('tom',10)
deck=Deck_Of_Cards()
x=deck.card_list.pop()
print('======')
print(x)
tom.setHand(deck)
print(tom.getCard())

y =tom.addCard('tom')
print(y)