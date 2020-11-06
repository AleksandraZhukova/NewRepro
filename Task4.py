#Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

from abc import ABC
from abc import abstractmethod
from collections import Counter


class Store(ABC):
    all_staff=[]
    def __init__(self):
        self.all_staff.append(self)
#При создании экземпляра техники. Она автоматически направляется на склад.


    def __str__(self):
        return self

    @abstractmethod
    def some_func(self):
        pass

    @staticmethod
    def staff_quantity(all_staff):
        result = {i.__class__: all_staff.count(i.__class__) for i in all_staff}
        return result


class OfficeEquipment(Store):

    def __init__(self, producer,  article, quality, price, *args, **kwargs):
        self.producer=producer
        self.article = article
        self.quality = quality
        self.price = price
        super().__init__()

    def some_func(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, copy_quantity, producer,  article, quality, price):
        self.copy_quantity = copy_quantity
        super().__init__(producer,  article, quality, price)

    def __str__(self):
        return f"Printer {self.producer} {self.article}"

    def __call__(self):
        print(f"New printer {self.producer} {self.article}")

    def print(self):
        pass



class Scanner(OfficeEquipment):
    def __init__(self, paper_format, producer,  article, quality, price):
        self.paper_format=paper_format
        super().__init__(producer,  article, quality, price)

    def __str__(self):
        return f"Scanner {self.producer} {self.article}"

    def __call__(self):
        print(f"New scanner {self.producer} {self.article}")

    def scann(self):
        pass


class Xerox(OfficeEquipment):
    def __init__(self, copy_color, producer,  article, quality, price):
        self.copy=copy_color
        super().__init__(producer,  article, quality, price)

    def __str__(self):
        return f"Xerox {self.producer} {self.article}"

    def __call__(self):
        print(f"Xerox {self.producer} {self.article}")

    def xerox(self):
        pass


printer=Printer(2, "Brother", "A654RT", "well", 5100)
scanner=Scanner("A4", "Sumsung", "DY46OP", "bad", 4200)

xerox1=Xerox("B/W", "Xerox", "MKF67J", "well", 5460)
xerox2=Xerox("Color", "hp", "MKBHV8", "not working", 4220)
xerox3=Xerox("B/W", "Brother", "VJH678", "not working", 6570)
xerox4=Xerox("B/W", "Xerox", "MKF67J", "well", 5460)

print(xerox1.quality)

printer()
print(printer)


print(Store.all_staff)
print(Store.staff_quantity(Store.all_staff))