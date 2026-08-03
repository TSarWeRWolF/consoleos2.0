import subprocess

from androidmode.android_manager import AndroidManager


class Launcher:

    def __init__(self):
        self.android = AndroidManager()


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


    # -----------------------------

    def launch_android(self, apk):
        print("Android игра:", apk)

        self.android.start_android()

        self.android.install_apk(apk)

        return None
