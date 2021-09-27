from instacoders import InstaCoders

insta = InstaCoders()

class User():

    def __init__(self, name, username) -> None:
        self.name = name
        self.username = username

    def follow(self, username, bestFriend=False):
        weight = bestFriend + 1
        insta.addArrow(self.username, username, weight)

    def unfollow(self, username):
        insta.removeArrow(self.username, username)

    def tagAsBestFriend(self, username):
        if username in insta.adjacency[self.username].keys():
            insta.adjacency[self.username][username] = 2

    def untagAsBestFriend(self, username):
        if username in insta.adjacency[self.username].keys():
            insta.adjacency[self.username][username] = 1

    def __repr__(self) -> str:
        return str(self.username)
