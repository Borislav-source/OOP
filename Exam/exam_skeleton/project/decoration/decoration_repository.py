from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    @staticmethod
    def __find_decoration_type(type_):
        if type_ == 'Ornament':
            return Ornament
        return Plant

    def find_by_type(self, decoration_type: str):
        type_ = self.__find_decoration_type(decoration_type)
        for decoration in self.decorations:
            if isinstance(decoration, type_):
                return decoration
        return '"None"'