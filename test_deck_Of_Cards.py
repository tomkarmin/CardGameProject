from unittest import TestCase
from cards.Deck_of_cards import Deck_Of_Cards

class TestDeck_Of_Cards(TestCase):
    def setUp(self):
         self.deck1=Deck_Of_Cards()

    def test_shuffle(self):
        self.assertFalse(self.deck1.shuffle(),self.deck1)

    def test_deal_one(self):
        self.assertGreater(len(self.deck1.deal_one()),len(self.deck1)) #טעות(השוואה של קלף לדק1)

    def test_show(self):
        self.fail()
