class Menu:

    def __init__(self):

        self.items = [
            {
                "name": "HOME",
                "icon": "home.png"
            },
            {
                "name": "GAMES",
                "icon": "games.png"
            }
        ]

        self.selected = 0

    # ------------------------

    def left(self):

        if self.selected > 0:
            self.selected -= 1

    # ------------------------

    def right(self):

        if self.selected < len(self.items) - 1:
            self.selected += 1

    # ------------------------

    def current(self):

        return self.items[self.selected]

    # ------------------------

    def count(self):

        return len(self.items)