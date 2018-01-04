from enum import Enum

class Color(Enum):
    RED = 0
    BLUE = 1
    YELLOW = 2
    GREEN = 3
    ALL = 4

class Detail(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    REVERSE = 10
    SKIP = 11
    DRAW_TWO = 12
    WILD = 13
    WILD_DRAW_FOUR = 14

class Card:
    color = Color
    detail = Detail

    def __init__(self, color, detail):
        self.color = color
        self.detail = detail

    def is_special(self):
        return self.detail.value > 9

    def __str__(self):
        return self.color.name + " " + self.detail.name