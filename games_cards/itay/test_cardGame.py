from unittest import TestCase
from card_game import CardGame
from class_cards import Card
from Deck_of_cards import Deck_Of_Cards
from class_player import Player

class TestCardGame(TestCase):

    def setUp(self):
        self.game = CardGame('tom', 'itay',10)
        self.card = Card(13, "club")
        self.card = Card(1, "diamond")
        self.deck1=Deck_Of_Cards()
        self.card1=Card(3,'heart')
        self.card2=Card(3,'club')
        self.card3=Card(4,'diamond')





    def test_new_game(self): #שלאחר חלוקת הקלפים לשחקנים יש כמות קלפיםש שווה ביד ושכמות זהה של קלפים ירדו מן החפיסה
        self.game.player1.setHand(self.deck1)
        self.game.player2.setHand(self.deck1)
        self.assertEqual(len(self.game.player1.package.card_list),len(self.game.player2.package.card_list))
        self.assertEqual(len(self.deck1 ),32)

    def test_get_round_winner(self):
        self.fail()

    def test_get_winner(self): #בדיקה זו מוכיחה שהשחקן שיש ךו פחות קלפים ביד מנצח
       self.game.player2.addCard(self.card3)
       self.assertEqual(self.game.get_winner(),self.game.player1.name)

                    #בדיקות שמאמתות שהפונקציה לאימות שם עובדת כראוי
    def test_validate_name_num(self): # לא מקבלת מספר
        self.assertFalse(self.game.validate_name(777), True)

    def test_validate_name_none(self): #לא מקבלת מקום ריק
        self.assertFalse(self.game.validate_name(''), True)

    def test_validate_name(self): #מקבלת שם תקני שבנוי מסטרינג
        self.assertTrue(self.game.validate_name('tom'), True)


