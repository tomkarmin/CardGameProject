import random

from cards.class_cards import Card


class Deck_Of_Cards:

    def __init__(self, fill=True):
        self.card_list = []
        if fill:
            num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            shape_list = ['club', 'heart', 'spade', 'diamond']
            for num in num_list:
                for shape in shape_list:
                    card = Card(num, shape)
                    self.card_list.append(card)
            # self.shuffle()  # done by CardGame

    def shuffle(self):
        random.shuffle(self.card_list)

    def __len__(self):
        return len(self.card_list)

    def deal_one(self):
       return self.card_list.pop()

    def show(self):
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
