class Album:

    def __init__(self, name, *args):
        self.name = name
        self.songs = [*args]
        self.published = False

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
        for sng in self.songs:
            if sng.name == song:
                self.songs.remove(sng)
                return f"Removed song {song} from album {self.name}."

        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        data = f"""Album {self.name}
"""
        for song in self.songs:
            data += f"{song.get_info()}\n"

        return data
