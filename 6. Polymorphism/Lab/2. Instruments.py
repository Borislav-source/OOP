def play_instrument(inst):
    return inst.play()


class Guitar:
    def play(self):
        print("playing the guitar")


guitar = Guitar()
play_instrument(guitar)
