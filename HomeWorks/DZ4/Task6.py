#Task6
#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from time import sleep
from itertools import count
from itertools import cycle

#Part1
for i in count(int(input('Enter first number '))):
    print(i)
    sleep(0.3)
    if i==100:
        print("End program")
        break


#Part2
my_list = [2, 2, 7, 23, 1, 44, 3, 2, 10, 7, 4, 11, 0, "new circle"]
count=0
for el in cycle(my_list):
    if count==20:
        print("End program")
        break
    print(el)
    count+=1
    sleep(0.3)
