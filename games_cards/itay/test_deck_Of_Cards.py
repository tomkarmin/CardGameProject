from unittest import TestCase
from games_cards.itay.Deck_of_cards import *


class TestDeck_Of_Cards(TestCase):
    def setUp(self):
        self.deck1=Deck_Of_Cards()

    def test_shuffle(self):
        self.assertFalse(self.deck1.shuffle(),self.deck1)

    def test_deal_one(self):
        self.assertTrue(self.deck1.card_list[0],self.deck1.deal_one())


