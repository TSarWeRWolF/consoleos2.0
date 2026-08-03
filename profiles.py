class Profiles:

    def __init__(self):

        self.profiles = {

            "morrowind": {

                "A": "SPACE",
                "B": "ESCAPE",
                "X": "E",
                "Y": "TAB",

                "LEFT": "A",
                "RIGHT": "D",
                "UP": "W",
                "DOWN": "S"
            },

            "gta_sa": {

                "A": "ENTER",
                "B": "SPACE",
                "X": "F",
                "Y": "TAB",

                "LEFT": "A",
                "RIGHT": "D",
                "UP": "W",
                "DOWN": "S"
            },

            "farcry": {

                "A": "SPACE",
                "B": "CTRL",
                "X": "R",
                "Y": "F",

                "LEFT": "A",
                "RIGHT": "D",
                "UP": "W",
                "DOWN": "S"
            }

        }

    # -----------------------------

    def get(self, name):

        return self.profiles.get(name)

    # -----------------------------

    def exists(self, name):

        return name in self.profiles