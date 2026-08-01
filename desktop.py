import os
import time
import tkinter as tk
from PIL import Image, ImageTk
import cv2

from animation import Animation
from controller import Controller
from menu import Menu
from library import Library

class ConsoleDesktop:

    def draw_library(self):

        game = self.library.current()

        self.canvas.create_text(
            120,
            170,
            text="LIBRARY",
            fill="white",
            font=("Arial", 28, "bold"),
            anchor="w"
        )

        self.canvas.create_text(
            120,
            240,
            text=game["name"],
            fill="#00BFFF",
            font=("Arial", 22),
            anchor="w"
        )


    def __init__(self):

        # Анимация
        self.animation = Animation()

        # Путь к ассетам
        self.assets = "/home/a/PycharmProjects/PythonProject/consoleos/asetsconsoke"

        # Меню
        self.menu = Menu()
        self.library = Library()
        # Геймпад
        self.controller = Controller()
        self.last_input = 0

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
        self.controller.update()

        # Обновление анимации
        self.animation.update()

        current_time = time.time()

        # Задержка между нажатиями
        if current_time - self.last_input > 0.2:

            if self.controller.left():
                self.left()
                self.last_input = current_time

            elif self.controller.right():
                self.right()
                self.last_input = current_time

            # Запуск игры
            elif self.menu.selected == 1 and self.controller.button_a():

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
