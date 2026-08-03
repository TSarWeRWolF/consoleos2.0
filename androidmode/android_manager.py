import os


class AndroidManager:


    def __init__(self):

        self.running = False

        # список Android игр
        self.apps = []


    # -----------------------------

    def start_android(self):

        print("Запуск Android Mode")

        self.running = True


    # -----------------------------

    def install_apk(self, apk):

        if os.path.exists(apk):

            print("APK найден:")
            print(apk)

            # добавляем игру в список
            if apk not in self.apps:
                self.apps.append(apk)

                print("APK добавлен в Android библиотеку")
                print("Android игры:")
                for app in self.apps:
                    print("-", app)


        else:

            print("APK не найден:")
            print(apk)


    # -----------------------------

    def launch_app(self, package):

        print("Запуск Android приложения:")
        print(package)


    # -----------------------------

    def get_apps(self):

        return self.apps