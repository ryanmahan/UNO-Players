from deck import Deck
from card import Color

class DumbPlayer:
    hand = []
    deck = None

    def __init__(self, hand, deck):
        self.hand = hand
        self.deck = deck

    def add_to_hand(self, c):
        self.hand.append(c)

    def play_card(self, played):
        for c in self.hand:
            card = self.check_card(c, played)
            if not card:
                continue
            self.hand.remove(card)
            return card
        for c in self.hand:
            if c.color == Color.ALL:
                self.hand.remove(c)
                return c

    
    def check_card(self, card, played):
        if card.color == played.color:
            return card
        elif card.detail == played.detail:
            return card
        return False

    def choose_color(self):
        color = [0, 0, 0, 0, 0]
        for card in self.hand:
            color[card.color.value] += 1
            if color[card.color.value] > len(self.hand) / 2:
                return card.color

        max = color[0]
        biggest = 0
        for i in range(4):
            if color[i] > max:
                biggest = i
        return Color(biggest)

    def has_won(self):
        return len(self.hand) == 0

    def __str__(self):
        to_string = ''
        for card in self.hand:
            to_string += str(card) + " "
        return to_string