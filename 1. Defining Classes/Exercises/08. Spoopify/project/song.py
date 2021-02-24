class Song:
    def __init__(self, name, length, single=False):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f'{self.name} - {self.length}'