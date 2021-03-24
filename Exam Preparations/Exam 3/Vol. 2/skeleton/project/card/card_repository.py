class CardRepository:
    def __init__(self):
        self.cards = []
        self.count = len(self.cards)
        self.cards_names = []

    def add_card(self, card):
        if card.name in self.cards_names:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.cards_names.append(card.name)

    def find_card(self, name):
        for card in self.cards:
            if card.name == name:
                return card

    def remove_card(self, card):
        if not card:
            raise ValueError("Card cannot be an empty string!")
        card_obj = self.find_card(card)
        self.cards.remove(card_obj)
        self.cards_names.remove(card)
