class Card:
    def __init__(self, num, shape):  # 'לקלאס CARD יש שני מאפיינים צורה (shape) מספר (num) '
        self.card_num = num
        self.card_shape = shape
        self.shape_dict = {'club': 17, 'heart': 16, 'spade': 15,
                           'diamond': 14}  # 'לכל צורה יש ערך מספרי הנקבע באמצעות דיקשנרי'

    def __gt__(self, other):  # 'פונקציה המשווה בין הקלפיםת ובודקת מי מבינהם גדול יותר :'
        if self.card_num < other.card_num:  # קודם הפונקציה משווה בין המספר של הקלף
            return False
        elif self.card_num > other.card_num:
            return True
        elif self.card_num == other.card_num:  # במקרה שבו לשני הקלפים יש את אותו מספר הפונקציה תעבור להשוות בין הצורות, ותבדוק למי מהצורות יש ערך מספרי גדול יוצתר עפ הערך שיש להם בדיקשנרי
            return self.shape_dict[self.card_shape] > other.shape_dict[other.card_shape]
        # מכיוון שאנו משתמשים בחפיסה אחת וכל קלף קיים פעם אחת בחפיסה אין מצב שבו גם הצורה וגם הקלף יהיו זהים

    def __str__(self):
        return f"{self.card_num}{self.card_shape}"

    # שתי הפונקציות  האלה נועדו כדי שנוכל לעשות הדפסה לאובייקט ולקבל את האובייקט ולא את מיקומו בזיכרון

    def __repr__(self):
        return str(self)

    # __repr__ = __str_
_
