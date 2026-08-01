import threading
import time

from pynput.keyboard import Controller, Key

from controller import Controller


class InputMapper:

    def __init__(self):

        self.controller = Controller()
        self.keyboard = Controller()

        self.running = False

        self.keys = {
            "w": False,
            "a": False,
            "s": False,
            "d": False
        }

    # -----------------------------

    def press(self, name):

        if not self.keys[name]:

            self.keyboard.press(name)
            self.keys[name] = True

    # -----------------------------

    def release(self, name):

        if self.keys[name]:

            self.keyboard.release(name)
            self.keys[name] = False

    # -----------------------------

    def update(self):

        while self.running:

            self.controller.update()

            # W
            if self.controller.up():
                self.press("w")
            else:
                self.release("w")

            # S
            if self.controller.down():
                self.press("s")
            else:
                self.release("s")

            # A
            if self.controller.left():
                self.press("a")
            else:
                self.release("a")

            # D
            if self.controller.right():
                self.press("d")
            else:
                self.release("d")

            # Прыжок
            if self.controller.button_a():
                self.keyboard.press(Key.space)
            else:
                self.keyboard.release(Key.space)

            # Меню
            if self.controller.button_b():
                self.keyboard.press(Key.esc)
            else:
                self.keyboard.release(Key.esc)

            time.sleep(0.01)

    # -----------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        threading.Thread(
            target=self.update,
            daemon=True
        ).start()

    # -----------------------------

    def stop(self):

        self.running = False