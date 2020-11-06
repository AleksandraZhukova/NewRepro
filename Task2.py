#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyErrorClass(ZeroDivisionError):
    def __init__(self, text, *args, **kwargs):
        self.text= text



def devide(a, b):
    if b==0:
        raise MyErrorClass("You try devide to zero!")
    else:
        c=a/b
        return c

my_a=int(input("Enter number"))
my_b=int(input("Enter number"))

try:
    print(devide(my_a, my_b))
except MyErrorClass as err:
    print (err)



