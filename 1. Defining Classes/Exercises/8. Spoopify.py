class Song:
    def __init__(self, name, length, single=False):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f'{self.name} - {self.length}'


class Album:
    published = False

    def __init__(self, name, *args):
        self.name = name
        self.songs = [*args]

    def add_song(self, song):
        if self.published:
            return f"Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song):
        if self.published:
            return f"Cannot remove songs. Album is published."
        elif song not in self.songs:
            return f"Song is not in the album."
        self.songs.remove(song)
        return f"Removed song {song.name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        data = f"""Album: {self.name}
"""
        for song in self.songs:
            data += f"{Song.get_info(song)}\n"

        return data


class Band:
    albums = []

    def __init__(self, name):
        self.name = name

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
        data = f'Band: {self.name}\n'
        for album in self.albums:
            data += f"{Album.details(album)}\n"

        return data


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())