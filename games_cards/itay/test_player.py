from unittest import TestCase
from games_cards.itay.class_player import Player
from games_cards.itay.Deck_of_cards import Deck_Of_Cards


class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player('tom', )
        self.deck1 = Deck_Of_Cards()

    def test_setHand(self):
        self.player.setHand(self.deck1)
        self.assertEqual(len(self.player.package.card_list), 10)
        for i in self.player.package.card_list:
            x = i in self.deck1.card_list
        self.assertTrue(True, x)

    def test_getCard(self):
        for i in range(10):
            self.player.getCard()
        self.assertIsNone(self.player.getCard(), None)

    def test_getCard(self):
        self.player.setHand(self.deck1)
        self.assertTrue(self.player.getCard(), self.player.package.card_list[-1])

    def test_addCard_invalid_type(self):
        self.assertFalse(self.player.addCard('tom'), True)

    def test_addCard(self):
        x = self.deck1.card_list.pop()
        self.player.addCard(5)
        self.assertEqual(self.player.package.card_list[0], x)
