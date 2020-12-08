from card_game import CardGame

cardGame = CardGame("tom","itay") #יצירת אובייקט משחק והזנת שמות שחקנים,שימוש בברית המחדל של עשרה קלפים

cardGame.show() #מראה את שמות השחקנים ואת הקלפים שביד כל אחד מהם

for round in range (10): #לולאה המריצה עשר פעמים את הפונקציה גט ווונר ובסוף מדפיסה את המנצח ואת הקלף שלו
    round_winner_list=cardGame.get_round_winner()
    print(f'the name of the winner is :{round_winner_list[0]}')
    print(f'the winnig crad was :{round_winner_list[1]}')

print('===================================')

cardGame.show()  #מראה את שמות השחקנים ואת הקלפים שביד כל אחד מהם

cardGame.new_game() #לא ניתן לקרוא לפונקציה זו מחות לקונסטרקטוטר

print(cardGame.get_winner()) #פונקציה המכריזה על שם המנצח
