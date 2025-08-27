from src.cards import DeckOfCards


def main():
    deck = DeckOfCards()
    deck.create_deck(shuffled=True)


if __name__ == "__main__":
    main()
