from src.card_enums import Card


class DeckOfCards:
    """Class to create a deck of cards"""

    def __init__(self, num_decks: int = 1, include_jokers: bool = False):
        self.num_decks = num_decks
        self.include_jokers = include_jokers
        self.deck = []

    def create_deck(self) -> list[Card]:
        a = self.deck
        print(a)
        return []

    def another_func(self):
        pass
