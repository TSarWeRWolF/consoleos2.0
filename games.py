class Games:

    def __init__(self):

        self.games = [

            {
                "name": "The Elder Scrolls III: Morrowind",

                "launcher": "steam",

                "appid": 22320,

                "profile": "morrowind",

                "image": "morrowind.png"
            },

            {
                "name": "Grand Theft Auto: San Andreas",

                "launcher": "steam",

                "appid": 12120,

                "profile": "gta_sa",

                "image": "gta_sa.png"
            },

            {
                "name": "Minecraft PE",
                "launcher": "android",
                "apk": "/home/a/PycharmProjects/PythonProject/consoleos/gameskonsoleos/Minecraft-PocketEdition_0.14.0.apk"
            }





        ]

    # ---------------------------------

    def all(self):

        return self.games

    # ---------------------------------

    def get(self, index):

        return self.games[index]

    # ---------------------------------

    def count(self):

        return len(self.games)