class list:
    def __init__(self, seq=()):
        self.seq = seq

    def __repr__(self, *args, **kwargs):
        return self.seq


a = list()
print(a)