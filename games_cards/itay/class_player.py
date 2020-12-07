from games_cards.itay.Deck_of_cards import Deck_Of_Cards


from games_cards.itay.class_cards import Card


class Player:
    def __init__(self, name, numOfCards=10): #פונקציה זו מגדריה את המאפיינים לקלאס "שחקן" שהם שם ןמספר קלפיםת ברירת המחדל היא 10
        self.name = name
        self.package = Deck_Of_Cards(fill=False) #אנו משתמשים בקלאס דק אוף קארדס ומזינים לו ערך בולךיאני False ובכך מונעים יצירת חבילת קלפים חדשה בעלת 52 קלפים
        if numOfCards > 26:
            numOfCards = 26
        self.numOfCards = numOfCards

    def __len__(self): #פונקציה המאפשרת בדיקת אורך של אובייקט
        return len(self.package)

    def setHand(self, deck1): #פונקציה המקבלת חבילת קלפים ושולפת מתוכה X קלפים באמצעות הפונקציה דיל וואן מקלאס דק אוף קארדס ומסיפה אותם לרשימה נפרדת של קלפים ביד השחקן. X נקבע עפ הפרמטר של מספר הקלפים (numofcards)
        for i in range(self.numOfCards):
            self.package.card_list.append(deck1.deal_one())

    def getCard(self): #פונקציה השולפת קלף מיד השחקן שוב באמצעות דיל וואן
        if len(self.package) != 0:
            return self.package.deal_one()


    def addCard(self, c): #פונקציה  המקבלת קלף ומוסיפה אותו ליד השחקן
        if c is not type(Card):
            self.package.card_list.append(c)
        else:
            print('invalid parameter')

    def show(self): #פונקציית הדפסה
        print(f"player's name: {self.name} "
              f"and player's cards package: {self.package}")


def main():
    player = Player("Tom")
    player.show()

    deck = Deck_Of_Cards()
    player.setHand(deck)
    player.show()


if __name__ == "__main__":
    main()
