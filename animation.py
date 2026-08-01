class Animation:

    def __init__(self):

        # Текущая позиция меню
        self.position = 0.0

        # К какой вкладке движемся
        self.target = 0.0

        # Скорость плавного движения
        self.speed = 0.15

    # ----------------------------------

    def move_to(self, index):

        self.target = float(index)

    # ----------------------------------

    def update(self):

        self.position += (
            self.target - self.position
        ) * self.speed

    # ----------------------------------

    def get_position(self):

        return self.position

    # ----------------------------------

    def get_scale(self, index):

        distance = abs(
            self.position - index
        )

        if distance > 1:
            return 1.0

        return 1.25 - (distance * 0.25)

    # ----------------------------------

    def get_offset(self, index):

        return (index - self.position) * 240

    # ----------------------------------

    def get_alpha(self, index):

        distance = abs(
            self.position - index
        )

        if distance > 1:
            return 0.4

        return 1.0 - (distance * 0.6)

    # ----------------------------------

    def finished(self):

        return abs(
            self.position - self.target
        ) < 0.01