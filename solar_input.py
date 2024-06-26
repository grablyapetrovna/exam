# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    if len(line.strip()) == 0 or line[0] == '#':
        return ""
    line = line.split()
    line[0] = line[0].lower()
    if line[0] == "star":
        star.R = float(line[1])
        star.color = line[2]
        star.m = float(line[3])
        star.x = float(line[4])
        star.y = float(line[5])
        star.Vx = float(line[6])
        star.Vy = float(line[7])

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    data = line.split()[1:]
    planet.r = int(data[0])
    planet.color = data[1]
    planet.m = float(data[2])
    planet.x = float(data[3])
    planet.y = float(data[4])
    planet.Vx = float(data[5])
    planet.Vy = float(data[6])

def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        i = 1
        for obj in space_objects:
            print(f"Объект номер {i} : Тип-{obj.type} Радиус-{obj.R} Цвет-{obj.color} Масса-{obj.m} ",
                  f"Кордината х-{obj.x} Кордината y- {obj.y} Скорость по х-{obj.Vx} Скорость по y-{obj.Vy}"
                  , file=out_file, end="\n\n")
            i += 1

if __name__ == "__main__":
    print("This module is not for direct call!")
