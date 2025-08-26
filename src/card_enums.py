from enum import Enum


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

class Suit(Enum):
    CLUBS = "CLUBS"
    DIAMONDS = "DIAMONDS"
    HEARTS = "HEARTS"
    SPADES = "SPADES"
    JOKER = "JOKER"

class Rank(Enum):
    ACE = "ACE"
    TWO = "TWO"
    THREE = "THREE"
    FOUR = "FOUR"
    FIVE = "FIVE"
    SIX = "SIX"
    SEVEN = "SEVEN"
    EIGHT = "EIGHT"
    NINE = "NINE"
    TEN = "TEN"
    JACK = "JACK"
    QUEEN = "QUEEN"
    KING = "KING"
    JOKER = "JOKER"