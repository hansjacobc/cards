class DeckNotDivisibleException(Exception):
    def __init__(self, num_players: int, len_deck: int):
        super().__init__(
            f"Cannot evenly deal {len_deck} cards to {num_players} players. "
        )