from unittest import TestCase
from class_player import Player
from Deck_of_cards import Deck_Of_Cards


class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player('tom', )
        self.deck1 = Deck_Of_Cards()

    def test_setHand(self): #בדיקה שאכן חולקו עשרה קלפים לשחקן ושהקלפים האלה כבר לא חיימים בחפיסה המקורית ממנה הם נשלפו
        self.player.setHand(self.deck1)
        self.assertEqual(len(self.player.package.card_list), 10)
        for i in self.player.package.card_list:
            x = i in self.deck1.card_list
        self.assertTrue(True, x)

    def test_getCard_empty_list(self): #בדיקה מה קורה שכאשר אין יותר קלפים ביד השחקן ושולפים קלף
        for i in range(10):
            self.player.getCard()
        self.assertIsNone(self.player.getCard(), None)

    def test_getCard(self): #בדיקה שהפונקציה שולפת את הקלף הנכון מתוך היד של השחקן
        self.player.setHand(self.deck1)
        self.assertTrue(self.player.getCard(), self.player.package.card_list[0])

    def test_addCard_invalid_type(self):#הפונקציה מסוגלת להוסיף רק קלפים לרשימת השחקן
        self.assertFalse(self.player.addCard('tom'), True)

    def test_addCard(self): #הפונקציה מסוגלת להוסיף קלפים ליד השחקן
        x = self.deck1.card_list.pop()
        self.player.addCard(x)
        self.assertEqual(self.player.package.card_list[0], x)
