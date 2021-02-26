class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}
        """
        In rented_books we add dictionaries with USERNAMES for keys and as value - another DICTIONARY 
        with BOOKS for keys and DAYS TO RETURN as value
        """

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        # self.user_records.insert(0, user)
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        if user.username in self.rented_books:
            del self.rented_books[user.username]

    def change_username(self, user_id: int, new_username: str):
        for user in self.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - " \
                           "it should be different than the username used so far!"
                for u, value in self.rented_books.items():
                    if u.user_id == user_id:
                        del self.rented_books[u.username]
                        self.rented_books[new_username] = value
                user.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            return f"There is no user with id = {user_id}!"
