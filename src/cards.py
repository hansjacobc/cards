import random

from src.card_enums import Card, Ranks, Suits


class DeckOfCards:
    """Class to create a deck of cards"""

    deck: list[Card]

    def __init__(self):
        self.deck = []

    def create_deck(
        self, shuffled: bool = False, num_decks: int = 1, include_jokers: bool = False
    ) -> None:
        for _ in range(num_decks):
            for suit in Suits:
                if suit == Suits.JOKER:
                    continue

                for rank in Ranks:
                    if rank == Ranks.JOKER:
                        continue

                    card = Card(suit=suit, rank=rank)
                    self.deck.append(card)

        if include_jokers:
            card = Card(suit=Suits.JOKER, rank=Ranks.JOKER)
            self.deck.append(card)
            self.deck.append(card)

        if shuffled:
            self.shuffle_deck()

    def shuffle_deck(self) -> None:
        random.shuffle(self.deck)
