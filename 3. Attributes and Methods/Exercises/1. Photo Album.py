class PhotoAlbum():

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    def __repr__(self):
        result = '-----------\n'
        for row in range(len(self.photos)):
            if len(self.photos[row]) > 0:
                page = ['[]' for _ in range(len(self.photos[row]))]
                result += f'{" ".join(page)}\n'
                result += '-----------\n'
            else:
                result += '\n-----------\n'
        return result

    @staticmethod
    def can_put_photo(photos):
        for page in range(len(photos)):
            if len(photos[page]) < 4:
                return page + 1

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count//4)

    def add_photo(self, label: str):
        page = PhotoAlbum.can_put_photo(self.photos)
        if not page:
            return "No more free spots"
        self.photos[page-1].append(label)
        return f"{label} photo added successfully on page {page}" \
               f" slot {self.photos[page-1].index(label)+1}"

    def display(self):
        return self.__repr__()


# p = PhotoAlbum(4)
# print(p.add_photos('Gordon'))
# print(p.add_photos('Vaseto'))
# print(p.add_photos('Vaset'))
# print(p.add_photos('Vaso'))
# print(p.add_photos('Vaeto'))
# print(p.display())

# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free spots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display()
        print(result)
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display()
        print(result)
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------\n")


if __name__ == "__main__":
    unittest.main()

