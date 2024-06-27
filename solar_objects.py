class SpaceObject:
    def __init__(self, object_type, R, color, m, x, y, Vx, Vy, orbit):
        self.type = object_type
        self.R = R
        self.color = color
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = 0
        self.Fy = 0
        self.image = None
        self.orbit = orbit


class Star(SpaceObject):
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self, R, color, m, x, y, Vx, Vy, orbit):
        super().__init__('star', R, color, m, x, y, Vx, Vy, orbit)


class Planet(SpaceObject):
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, R, color, m, x, y, Vx, Vy, orbit):
        super().__init__('planet', R, color, m, x, y, Vx, Vy, orbit)