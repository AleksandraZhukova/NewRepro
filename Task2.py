#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC
from abc import abstractmethod


class Clothes(ABC):

    @staticmethod
    def summ_consumption(bag):
        res = 0
        for staff in bag:
            res += staff.fabric_consumption
        return res

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        consumption=self.size/6.5 + 0.5
        return round(consumption)
        print(f"Coat consumption: {consumption}")


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def fabric_consumption(self):
        consumption=2 * self.height + 0.3
        return round(consumption)
        print(f"Suit consumption: {consumption}")


coat = Coat(500)
suit = Suit(30)

print("Fabric for sewing coats", coat.fabric_consumption)
print("Fabric for sewing suit", suit.fabric_consumption)

bag=[coat, suit]
print("Fabric for all our clothes", Clothes.summ_consumption(bag))