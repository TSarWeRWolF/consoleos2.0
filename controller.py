import pygame


class Controller:

    def __init__(self):

        pygame.init()
        pygame.joystick.init()

        self.joystick = None

        if pygame.joystick.get_count() > 0:

            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

            print("Подключен геймпад:")
            print("Название:", self.joystick.get_name())
            print("Оси:", self.joystick.get_numaxes())
            print("Кнопки:", self.joystick.get_numbuttons())
            print("HAT:", self.joystick.get_numhats())

        else:

            print("Геймпад не найден.")

    # -----------------------------

    def update(self):

        pygame.event.pump()

    # -----------------------------

    def left(self):

        if self.joystick is None:
            return False

        if self.joystick.get_numhats() > 0:
            hat = self.joystick.get_hat(0)

            if hat[0] == -1:
                return True

        axis = self.joystick.get_axis(0)

        return axis < -0.6

    # -----------------------------

    def right(self):

        if self.joystick is None:
            return False

        if self.joystick.get_numhats() > 0:
            hat = self.joystick.get_hat(0)

            if hat[0] == 1:
                return True

        axis = self.joystick.get_axis(0)

        return axis > 0.6

    # -----------------------------

    def up(self):

        if self.joystick is None:
            return False

        if self.joystick.get_numhats() > 0:
            hat = self.joystick.get_hat(0)

            if hat[1] == 1:
                return True

        axis = self.joystick.get_axis(1)

        return axis < -0.6

    # -----------------------------

    def down(self):

        if self.joystick is None:
            return False

        if self.joystick.get_numhats() > 0:
            hat = self.joystick.get_hat(0)

            if hat[1] == -1:
                return True

        axis = self.joystick.get_axis(1)

        return axis > 0.6

    # -----------------------------

    def button_a(self):

        if self.joystick is None:
            return False

        return self.joystick.get_button(0)

    # -----------------------------

    def button_b(self):

        if self.joystick is None:
            return False

        return self.joystick.get_button(1)

    # -----------------------------

    def button_x(self):

        if self.joystick is None:
            return False

        return self.joystick.get_button(2)

    # -----------------------------

    def button_y(self):

        if self.joystick is None:
            return False

        return self.joystick.get_button(3)