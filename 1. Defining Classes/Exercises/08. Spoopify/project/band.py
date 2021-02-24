class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album):
        for al in self.albums:
            if al.name == album:
                if al.published:
                    return f"Album has been published. It cannot be removed."
                else:
                    self.albums.remove(al)
                    return f"Album {album} has been removed."
        return f"Album {album} is not found."

    def details(self):
        data = f'Band {self.name}\n'
        for album in self.albums:
            data += f"{album.details()}\n"
        return data
