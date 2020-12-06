class Card:
    def __init__(self, num, shape):
        self.card_num = num
        self.card_shape = shape
        self.shape_dict = {'club': 17, 'heart': 16, 'spade': 15, 'diamond': 14}

    def __gt__(self, other):
        if self.card_num < other.card_num:
            return False
        elif self.card_num > other.card_num:
            return True
        elif self.card_num == other.card_num:
            if self.shape_dict[self.card_shape] > other.shape_dict[other.card_shape]:
                return True
            else:
                return False  # self.shape_dict[self.card_shape] > other.shape_dict[other.card_shape]

    def __str__(self):
        return f"{self.card_num}{self.card_shape}"

    def __repr__(self):
        return str(self)

    # __repr__ = __str__
