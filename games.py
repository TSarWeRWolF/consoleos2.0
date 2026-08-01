class Games:

    def __init__(self):

        self.games = [

            {
                "name": "The Elder Scrolls III: Morrowind",
                "launcher": "steam",
                "appid": "22320",
                "icon": "morrowind.png"
            }

        ]

    # --------------------------

    def count(self):

        return len(self.games)

    # --------------------------

    def get(self, index):

        return self.games[index]

    # --------------------------

    def names(self):

        return [game["name"] for game in self.games]

    # --------------------------

    def add(self, game):

        self.games.append(game)

    # --------------------------

    def remove(self, index):

        del self.games[index]