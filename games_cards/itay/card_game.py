from Deck_of_cards import Deck_Of_Cards

from class_player import Player

class CardGame:
    def __init__(self, name1, name2, num_cards=10): #קונסטרקטור זה מכנס לתוכו את את שאר הקלאסיםץ
                                                    #הוא מקבל שמות שחקנים ומספק קלפים מאמת שאכן השמות תקינים ןשמספר הקלפים תקין מייצר שחקנים שבמות אלה וקורא לפונקציה new game

        self.deckK = Deck_Of_Cards()
        if not self.validate_name(name1):
            print("error in name 1")
            return
        if not self.validate_name(name2):
            print("error in name 2")
            return
        if name1==name2:
            name1+=".A"
            name2+='.B'
        if type(num_cards) != int or num_cards < 10:
            print("invalid card number")
            return
        player1 = Player(name1, num_cards)
        player2 = Player(name2, num_cards)
        self.player1 = player1
        self.player2 = player2
        self.numCards = num_cards
        self.new_game_called = False
        self.new_game()

    def validate_name(self, name): #פונקציה המוודא שהשמות תקיניםת הפונקצייה נקראת בקונסטרקוטור
        return type(name) is str and len(name) > 0


    def new_game(self): #פונקציה שיכולה להיקרא אך ורק מהקונסטרקטור שעושה שאםל לחפיסה ומחלקת יד לכל משתמש עפ מספר הקלפים שנבחר בקונסטרקטור
                         # עם מינמום של לפחות עשרה קלפים
        if self.new_game_called:
            print("new game called again")
        else:
            self.new_game_called = True #לפונקציה זו יש פלאג שנקבע בקונסטרוקטור ומנועת ממנה לרוץ שנית
            if self.numCards >=10:
                self.deckK.shuffle()
                self.player1.setHand(self.deckK)
                self.player2.setHand(self.deckK)
            else:
                print("ERROR")

    def get_round_winner(self): #פונקציה זו נקראת עשר פעמים במיין ולמעשה מריצה את המשחק עצמו: עשרה סיבובים בהם אחד המשתתפים מנצח אם הרלף שלו גדול יותק
        x = self.player1.getCard()
        y = self.player2.getCard()
        if x > y:
            self.player2.addCard(y)
            self.player2.addCard(x)  #פונקציה זו גם מוסיפה קלפים לשחקו המפסיד
            return [self.player1.name, x]
        else:
            self.player1.addCard(y)
            self.player1.addCard(x)
            return [self.player2.name, y]

    def get_winner(self): #פונקציה זו משווה בין אורכי רשימות הקלפים שביד השחקן. השחקן שאורך הרשימה קצר יותר מנצח
        if len(self.player1.package) == len(self.player2.package):
            return None
        elif len(self.player1.package) > len(self.player2.package):
            return self.player2.name
        else:
            return self.player1.name

    def show(self): #פונקציה המדפיסה את שם השחקן ואת ומדפיסה את הקלפים שבידו
        self.player1.show()
        self.player2.show()
