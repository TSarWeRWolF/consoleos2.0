import os
import time
import tkinter as tk
from PIL import Image, ImageTk
import cv2

from animation import Animation
from controller import Controller
from menu import Menu
from library import Library
from browser import Browser

class ConsoleDesktop:

    def game_finished(self):

        self.game_running = False
        self.game_running = True
        print("Игра запущена, меню заблокировано")

        self.library.launch()


        print("Игра закрыта, меню разблокировано")
        self.game_running = False



    def draw_library(self):

        self.canvas.create_text(
            120,
            170,
            text="LIBRARY",
            fill="white",
            font=("Arial", 28, "bold"),
            anchor="w"
        )

        y = 240

        for i in range(self.library.games.count()):

            game = self.library.games.get(i)

            color = "white"

            if i == self.library.selected:
                color = "#00BFFF"

            self.canvas.create_text(
                120,
                y,
                text=game["name"],
                fill=color,
                font=("Arial", 22),
                anchor="w"
            )

            y += 45


    def __init__(self):

        self.browser = Browser()
        # Анимация
        self.animation = Animation()

        # Путь к ассетам
        self.assets = "/home/a/PycharmProjects/PythonProject/consoleos/asetsconsoke"

        # Меню
        # Меню
        self.menu = Menu()

        # Геймпад
        self.controller = Controller()

        # Библиотека
        self.library = Library()

        self.last_input = 0
        self.game_running = False

        # Окно
        self.window = tk.Tk()
        self.window.title("Console OS")
        self.window.attributes("-fullscreen", True)
        self.window.configure(bg="black")
        self.window.focus_force()

        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()

        self.canvas = tk.Canvas(
            self.window,
            width=self.width,
            height=self.height,
            highlightthickness=0,
            bg="black"
        )

        self.canvas.pack(fill="both", expand=True)

        # ---------- Видео ----------
        self.video = cv2.VideoCapture(
            os.path.join(self.assets, "theme.mp4")
        )

        # ---------- Иконки ----------
        self.home_icon = Image.open(
            os.path.join(self.assets, "home.png")
        )

        self.games_icon = Image.open(
            os.path.join(self.assets, "games.png")
        )

        self.browser_icon = Image.open(
            os.path.join(self.assets, "browser.png")
        )

        self.browser_icon = self.browser_icon.resize((64, 64))

        self.browser_icon = ImageTk.PhotoImage(self.browser_icon)

        self.home_icon = self.home_icon.resize((64, 64))
        self.games_icon = self.games_icon.resize((64, 64))

        self.home_icon = ImageTk.PhotoImage(self.home_icon)
        self.games_icon = ImageTk.PhotoImage(self.games_icon)

        # Управление клавиатурой
        self.window.bind("<Left>", self.left)
        self.window.bind("<Right>", self.right)
        self.window.bind("<Escape>", lambda e: self.window.destroy())

    # =======================
    # Переключение вкладок
    # =======================

    def left(self, event=None):

        self.menu.left()
        self.animation.move_to(self.menu.selected)

    def right(self, event=None):

        self.menu.right()
        self.animation.move_to(self.menu.selected)

    # =======================
    # Видео
    # =======================

    def draw_video(self):

        ok, frame = self.video.read()

        if not ok:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ok, frame = self.video.read()

        if ok:

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frame = cv2.resize(
                frame,
                (self.width, self.height)
            )

            image = Image.fromarray(frame)

            self.background = ImageTk.PhotoImage(image)

            self.canvas.create_image(
                0,
                0,
                image=self.background,
                anchor="nw"
            )

    # =======================
    # Верхнее меню
    # =======================

    def draw_menu(self):

        x = 80 + self.animation.get_offset(0)

        color = "#00BFFF" if self.menu.selected == 0 else "white"

        self.canvas.create_image(
            x,
            55,
            image=self.home_icon
        )

        self.canvas.create_text(
            x + 50,
            55,
            text="HOME",
            fill=color,
            font=("Arial", 22, "bold"),
            anchor="w"
        )

        x = 560 + self.animation.get_offset(2)

        color = "#00BFFF" if self.menu.selected == 2 else "white"

        self.canvas.create_image(
            x,
            55,
            image=self.browser_icon
        )

        self.canvas.create_text(
            x + 50,
            55,
            text="BROWSER",
            fill=color,
            font=("Arial", 22, "bold"),
            anchor="w"
        )



        x = 320 + self.animation.get_offset(1)

        color = "#00BFFF" if self.menu.selected == 1 else "white"

        self.canvas.create_image(
            x,
            55,
            image=self.games_icon
        )

        self.canvas.create_text(
            x + 50,
            55,
            text="GAMES",
            fill=color,
            font=("Arial", 22, "bold"),
            anchor="w"
        )

    # =======================
    # Обновление экрана
    # =======================

    def update(self):

        # Обновление геймпада
        if not self.game_running:
            self.controller.update()

        # Обновление анимации
        self.animation.update()

        current_time = time.time()

        # Задержка между нажатиями
        if not self.game_running and current_time - self.last_input > 0.2:

            if self.controller.left():
                self.left()
                self.last_input = current_time

            elif self.controller.right():
                self.right()
                self.last_input = current_time

            # Переключение игр
            elif self.menu.selected == 1 and self.controller.up():

                self.library.previous()
                self.last_input = current_time

            elif self.menu.selected == 1 and self.controller.down():

                self.library.next()
                self.last_input = current_time





            # Запуск игры
            elif self.menu.selected == 1 and self.controller.button_a():

                self.game_running = True

                self.library.launch()

                self.last_input = current_time

        # Очистка экрана
        self.canvas.delete("all")

        # Отрисовка
        self.draw_video()
        self.draw_menu()

        if self.menu.selected == 1:
            self.draw_library()

        # Следующий кадр
        self.window.after(
            16,
            self.update
        )

    # =======================
    # Запуск
    # =======================

    def run(self):

        self.update()
        self.window.mainloop()





