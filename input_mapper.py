# import threading
# import time
#
# from pynput.keyboard import Controller as KeyboardController, Key
#
# from profiles import Profiles
#
#
# class InputMapper:
#
#     def __init__(self, controller):
#
#         # Используем общий Controller
#         self.controller = controller
#
#         # Клавиатура
#         self.keyboard = KeyboardController()
#
#         # Профили
#         self.profiles = Profiles()
#         self.profile = self.profiles.get("morrowind")
#
#         self.running = False
#
#         self.keys = {
#             "w": False,
#             "a": False,
#             "s": False,
#             "d": False
#         }
#
#     # ------------------------------------------------
#
#     def load_profile(self, name):
#
#         if self.profiles.exists(name):
#             self.profile = self.profiles.get(name)
#             print(f"Загружен профиль: {name}")
#
#     # ------------------------------------------------
#
#     def get_key(self, name):
#
#         value = self.profile[name]
#
#         special = {
#             "SPACE": Key.space,
#             "ESCAPE": Key.esc,
#             "ENTER": Key.enter,
#             "TAB": Key.tab,
#             "SHIFT": Key.shift,
#             "CTRL": Key.ctrl,
#             "CONTROL": Key.ctrl,
#             "ALT": Key.alt
#         }
#
#         return special.get(value, value.lower())
#
#     # ------------------------------------------------
#
#     def press(self, name):
#
#         key = self.get_key(name)
#
#         if isinstance(key, str):
#
#             if not self.keys.get(key, False):
#                 self.keyboard.press(key)
#                 self.keys[key] = True
#
#         else:
#
#             self.keyboard.press(key)
#
#     # ------------------------------------------------
#
#     def release(self, name):
#
#         key = self.get_key(name)
#
#         if isinstance(key, str):
#
#             if self.keys.get(key, False):
#                 self.keyboard.release(key)
#                 self.keys[key] = False
#
#         else:
#
#             self.keyboard.release(key)
#
#     # ------------------------------------------------
#
#     def update(self):
#
#         while self.running:
#
#             self.controller.update()
#
#             # Вверх
#             if self.controller.up():
#                 self.press("UP")
#             else:
#                 self.release("UP")
#
#             # Вниз
#             if self.controller.down():
#                 self.press("DOWN")
#             else:
#                 self.release("DOWN")
#
#             # Влево
#             if self.controller.left():
#                 self.press("LEFT")
#             else:
#                 self.release("LEFT")
#
#             # Вправо
#             if self.controller.right():
#                 self.press("RIGHT")
#             else:
#                 self.release("RIGHT")
#
#             # Кнопка A
#             if self.controller.button_a():
#                 self.press("A")
#             else:
#                 self.release("A")
#
#             # Кнопка B
#             if self.controller.button_b():
#                 self.press("B")
#             else:
#                 self.release("B")
#
#             # Кнопка X
#             if self.controller.button_x():
#                 self.press("X")
#             else:
#                 self.release("X")
#
#             # Кнопка Y
#             if self.controller.button_y():
#                 self.press("Y")
#             else:
#                 self.release("Y")
#
#             time.sleep(0.01)
#
#     # ------------------------------------------------
#
#     def start(self):
#
#         if self.running:
#             return
#
#         self.running = True
#
#         threading.Thread(
#             target=self.update,
#             daemon=True
#         ).start()
#
#     # ------------------------------------------------
#
#     def stop(self):
#
#         self.running = False