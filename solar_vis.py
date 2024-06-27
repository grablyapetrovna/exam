# coding: utf-8
# license: GPLv3
from solar_objects import *

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране, принимают физические координаты
"""


class VisSolar:
    header_font = "Arial-16"
    """Шрифт в заголовке"""

    window_width = 1000
    """Ширина окна"""

    window_height = 800
    """Высота окна"""

    scale_factor = None
    """Масштабирование экранных координат по отношению к физическим.
    Тип: float
    Мера: количество пикселей на один метр."""

    def calculate_scale_factor(max_distance):
        """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
        global scale_factor
        VisSolar.scale_factor = 0.4 * min(VisSolar.window_height, VisSolar.window_width) / max_distance
        print('Scale factor:', VisSolar.scale_factor)

    def scale_x(x):
        """Возвращает экранную **x** координату по **x** координате модели.
        Принимает вещественное число, возвращает целое число.
        В случае выхода **x** координаты за пределы экрана возвращает
        координату, лежащую за пределами холста.

        Параметры:

        **x** — x-координата модели.
        """

        return int(x * VisSolar.scale_factor) + VisSolar.window_width // 2

    def scale_y(y, orbit):
        """Возвращает экранную **y** координату по **y** координате модели.
        Принимает вещественное число, возвращает целое число.
        В случае выхода **y** координаты за пределы экрана возвращает
        координату, лежащую за пределами холста.
        Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

        Параметры:

        **y** — y-координата модели.
        """
        orbit = orbit
        if orbit % 2 == 0:
            return VisSolar.window_height // 2 - int(y * VisSolar.scale_factor)
        else:
            return int(y * VisSolar.scale_factor) + VisSolar.window_height // 2

    def create_star_image(space, star):
        """Создаёт отображаемый объект звезды.

        Параметры:

        **space** — холст для рисования.
        **star** — объект звезды.
        """

        x = VisSolar.scale_x(star.x)
        y = VisSolar.scale_y(star.y, orbit=star.orbit)
        r = star.R
        star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)

    def create_planet_image(space, planet):
        """Создаёт отображаемый объект планеты.
        Параметры:
        **space** — холст для рисования.
        **planet** — объект планеты.
        """
        x = VisSolar.scale_x(planet.x)
        y = VisSolar.scale_y(planet.y, orbit=planet.orbit)
        r = planet.R
        planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)

    def update_system_name(space, system_name):
        """Создаёт на холсте текст с названием системы небесных тел.
        Если текст уже был, обновляет его содержание.
        Параметры:
        **space** — холст для рисования.
        **system_name** — название системы тел.
        """
        space.create_text(30, 80, tag="header", text=system_name, font=VisSolar.header_font)

    def update_object_position(space, body):
        """Перемещает отображаемый объект на холсте.

        Параметры:

        **space** — холст для рисования.
        **body** — тело, которое нужно переместить.
        """
        x = VisSolar.scale_x(body.x)
        y = VisSolar.scale_y(body.y, orbit=body.orbit)
        r = body.R
        if x + r < 0 or x - r > VisSolar.window_width or y + r < 0 or y - r > VisSolar.window_height:
            space.coords(body.image, VisSolar.window_width + r, VisSolar.window_height + r,
                         VisSolar.window_width + 2 * r, VisSolar.window_height + 2 * r)  # положить за пределы окна
        space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == "__main__":
    print("This module is not for direct call!")
