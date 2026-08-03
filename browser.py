import subprocess


class Browser:

    def open(self):
        try:
            subprocess.Popen(["google-chrome"])
            print("Chrome запущен")

        except Exception as e:
            print("Ошибка запуска браузера:", e)