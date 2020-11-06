#Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"Date is {self.date}"

    @classmethod
    def make_date_int(cls, my_date: "Date"):
        try:
            list_int_date = list(map(int, my_date.date.split("-")))
            return f"Int date: {list_int_date}"
        except Exception as err:
            print (err)


    @staticmethod
    def validity(my_date: "Date"):
        list_int_date=list(map(int, my_date.date.split("-")))

        if 1<=list_int_date[0]<=31:
            if 1<=list_int_date[1]<=12:
                return f"There is not date format mistake. Date is {list_int_date}"

        else:
            return f"Wrong date format"



day1 = Date("06-11-2020")
print(day1)
print(Date.make_date_int(day1))
print(Date.validity(day1))


day2 = Date("32-11-2020")
print(Date.validity(day2))

day3 = Date("32-15-2020")
print(Date.validity(day3))

day4 = Date("первое-15-2020")
print(Date.make_date_int(day4))

