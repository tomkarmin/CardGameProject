
from cards.Deck_of_cards import *
from cards.class_player import Player
from cards_new.card_game1 import CardGame

cardGame = CardGame("tom","itay")

cardGame.show()

for round in range (10):
    round_winner_list=cardGame.get_round_winner()
    print(f'the name of the winner is :{round_winner_list[0]}')
    print(f'the winnig crad was :{round_winner_list[1]}')

print('===================================')

cardGame.show()

print(cardGame.get_winner())
