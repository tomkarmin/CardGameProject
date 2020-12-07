from games_cards.itay.card_game import CardGame

cardGame = CardGame("tom","itay")

cardGame.show()

for round in range (10):
    round_winner_list=cardGame.get_round_winner()
    print(f'the name of the winner is :{round_winner_list[0]}')
    print(f'the winnig crad was :{round_winner_list[1]}')

print('===================================')

cardGame.show()

cardGame.new_game()

print(cardGame.get_winner())
