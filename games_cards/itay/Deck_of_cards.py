import random

from games_cards.itay.class_cards import Card


class Deck_Of_Cards: #קלאס אשר נקרא חבילת קלפים

    def __init__(self, fill=True): #פונקציה זו משתמשת בלולאות בכדי לייצר את האובייקט קלף ולהוסיף אותו לרשימת קלפים.
                                    #לפונקציה יש פרמטר הנקרא פיל ומוזן אליו ערך בוליאני טרו, פרמטר זה מונע יצירת חבילה בעלת 52 כל פעם שקוראים לקלאס וכך בהמשך ניתן לקרוא לקלקאס זה ללא יצירת חבילה חדשה
        self.card_list = []
        if fill:
            num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            shape_list = ['club', 'heart', 'spade', 'diamond']
            for num in num_list:
                for shape in shape_list:
                    card = Card(num, shape)
                    self.card_list.append(card)
            # self.shuffle()  # done by CardGame

    def shuffle(self): #שימוש בפונקציה מובנת כדי לערבב את חפיסת הקלפים
        random.shuffle(self.card_list)

    def __len__(self): #פונקציה המאפשרת התייחסות לאורך האובייקט ולא למאורך המיקום  שלו בזיכרון
        return len(self.card_list)

    def deal_one(self): #פונקציה השולפת את הקלף הראשון בחפיסה
       return self.card_list.pop(0)

    def show(self): #פונקציה המאפשרת את הדפסת החפיסה
        for i in self.card_list:
            print(i)

    def __str__(self):
        return str(self.card_list)

def main():
    deck = Deck_Of_Cards()

    deck.show()

    deck.shuffle()
    print("=" * 30)
    deck.show()

    print("=" * 30)
    print(len(deck))
    deck.deal_one()
    print(len(deck))
    deck.show()

    print("=" * 30)
    print(deck)


if __name__ == "__main__":
    main()
