class User():

    def __init__(self, name, username) -> None:
        self.name = name
        self.username = username

    def __repr__(self) -> str:
        return str(self.username)
