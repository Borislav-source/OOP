class CardRepository:
    def __init__(self):
        self.cards = []
        self.card_names = []
        self.count = len(self.cards)

    def add(self, card):
        if card.name in self.card_names:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.card_names.append(card.name)

    def remove(self, card: str):
        if not card:
            raise ValueError("Card cannot be an empty string!")
        the_card = self.find(card)
        self.cards.remove(the_card)
        self.card_names.remove(the_card.name)

    def find(self, name: str):
        for card in self.cards:
            if card.name == name:
                return card
