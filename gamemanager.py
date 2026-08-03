
# import threading

# from launcher import Launcher
# from input_mapper import InputMapper
#
#
# class GameManager:
#
#     def __init__(self, controller, on_game_finished=None):
#
#         self.launcher = Launcher()
#         self.input = InputMapper(controller)
#
#         self.process = None
#         self.on_game_finished = on_game_finished
#
#     # ------------------------------------
#
#     def launch(self, game):
#
#         # Загружаем профиль управления
#         self.input.load_profile(
#             game["profile"]
#         )
#
#         # Запускаем перевод управления
#         self.input.start()
#
#         # Запускаем игру
#         if game["launcher"] == "steam":
#
#             self.process = self.launcher.launch_steam(
#                 game["appid"]
#             )
#
#         elif game["launcher"] == "wine":
#
#             self.process = self.launcher.launch_wine(
#                 game["path"]
#             )
#
#         elif game["launcher"] == "linux":
#
#             self.process = self.launcher.launch_linux(
#                 game["path"]
#             )
#
#         # Следим за процессом
#         threading.Thread(
#             target=self.wait_game,
#             daemon=True
#         ).start()
#
#     # ------------------------------------
#
#     def wait_game(self):
#
#         if self.process is None:
#             return
#
#         self.process.wait()
#
#         self.input.stop()
#
#         if self.on_game_finished:
#             self.on_game_finished()
#
#         print("Игра закрыта.")

