
import subprocess


class Launcher:

    def __init__(self):
        pass

    # -----------------------------

    def launch_linux(self, path):

        return subprocess.Popen(
            [path]
        )

    # -----------------------------

    def launch_wine(self, path):

        return subprocess.Popen(
            [
                "wine",
                path
            ]
        )

    # -----------------------------

    def launch_steam(self, appid):

        return subprocess.Popen(
            [
                "steam",
                f"steam://rungameid/{appid}"
            ]
        )

