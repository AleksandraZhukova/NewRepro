#Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.z = 'a + b * i'

    def __str__(self):
        return f"z= {self.x} + {self.y}*i"

    def __call__(self):
        print(f"Your complex number: {self.x} + {self.y}*i")

    def __add__(self, other):
        return ComplexNumber(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        #multiplication=(self.x * other.x - self.y * other.y) + i* (self.x * other.y - self.y * other.x)
        new_x=(self.x * other.x - self.y * other.y)
        new_y=(self.x * other.y - self.y * other.x)

        return ComplexNumber(new_x, new_y)



z1 = ComplexNumber(5, -1)
z2 = ComplexNumber(4, 6)
print(z1)

z1()
z2()

print(z1+z2)
print(z1*z2)

