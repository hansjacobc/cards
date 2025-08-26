from dataclasses import dataclass

from src.card_enums import Suit, Card
from src.card_enums import Rank



class DeckOfCards:

    def __init__(self, num_decks: int = 1, include_jokers: bool = False):
        self.num_decks = num_decks
        self.include_jokers = include_jokers
        self.deck = []

    def create_deck(self) -> list[Card]:

        return []
