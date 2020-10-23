#Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, width, length, weight, height):
        self._width = width
        self._length = length
        self.weight = weight
        self.height = height

    def massa(self):
        massa = self._length * self._width * self.weight * self.height
        print(f"For the road we need {massa} tons of asphalt")


new_road = Road(20, 5000, 25, 0.005)
new_road.massa()