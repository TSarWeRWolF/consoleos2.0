from games import Games
from launcher import Launcher


class Library:

    def __init__(self):

        self.games = Games()
        self.launcher = Launcher()

        self.selected = 0

    # -------------------------

    def next(self):

        if self.selected < self.games.count() - 1:
            self.selected += 1

    # -------------------------

    def previous(self):

        if self.selected > 0:
            self.selected -= 1

    # -------------------------

    def current(self):

        return self.games.get(self.selected)

    # -------------------------

    def launch(self):

        game = self.current()

        if game["launcher"] == "steam":

            self.launcher.launch_steam(
                game["appid"]
            )