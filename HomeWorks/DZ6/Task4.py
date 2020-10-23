#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости

#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"The {self.name} is going. "

    def stop(self):
        return f"The {self.name} has stopped. "

    def turn(self, direction):
        return f"The {self.name} turn to the {direction}. "

    def show_speed(self):
        return f"Now speed is: {self.speed}. "


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"You exceeded the speed limit by {self.speed-60} km per hour. "
        else:
            return f"Speed of {self.name} is normal. "


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"You exceeded the speed limit by {self.speed-40} km per hour. "
        else:
            return f"Speed of {self.name} is normal. "


class PoliceCar(Car):
    def alarm(self):
        return f"Alarm signal!!!. "
    def is_polise_car(self):
        if self.is_police==True:
            return f"It is polise car! "



town_car = TownCar("Wolsvagen", 70, "black", False)
print(town_car.show_speed(),town_car.turn("right"), town_car.stop(),"\n")

town_car = TownCar("Lada Vesta", 40, "yellow", False)
print(town_car.show_speed(), town_car.stop(),"\n")


sport_car = SportCar("Ferrari", 150, "red", False)
print(sport_car.go(), sport_car.show_speed(), sport_car.turn('left'),"\n")

work_car = WorkCar("Kamaz", 55, "grey", False)
print(work_car.go(), work_car.show_speed(), work_car.turn('right'), work_car.stop(),"\n")

police_car = PoliceCar("BMW", 80, "black", True)
print(police_car.go(), police_car.is_polise_car(), police_car.alarm(),"\n")
