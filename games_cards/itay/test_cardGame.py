from unittest import TestCase
from games_cards.itay.card_game import CardGame
from games_cards.itay.class_cards import Card


class TestCardGame(TestCase):

    def setUp(self):
        self.game = CardGame('tom', 'itay')
        self.card = Card(13, "club")
        self.card = Card(1, "diamond")

    def test_new_game(self):
        self.fail()

    def test_get_round_winner(self):
        self.fail()

    def test_get_winner(self):
        self.fail()

    def test_validate_name_num(self):
        self.assertFalse(self.game.validate_name(777), True)

    def test_validate_name_none(self):
        self.assertFalse(self.game.validate_name(''), True)

    def test_validate_name(self):
        self.assertTrue(self.game.validate_name('tom'), True)
