from unittest import TestCase
from Deck_of_cards import *


class TestDeck_Of_Cards(TestCase): #קוראים לקלאס כדי לייצר חפיסת קלפים שעליה נבצע את הבדיקות
    def setUp(self):
        self.deck1=Deck_Of_Cards()

    def test_shuffle(self): #משווים בין חפיסה מעורבבת ואחת שלא, התוצאה תהיה פולס מכיוון שאחת מהם באמת מעורבבת
        self.assertTrue(self.deck1.shuffle(),self.deck1)

    def test_deal_one(self): #השוואה בין הקלף שנשלף  לקלף הראשון ברדימה וכך מוודא שהקלף הנכון באמת נשלף
        self.assertTrue(self.deck1.card_list[0],self.deck1.deal_one())


