#Task3
#Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.

a=[x for x in range(20,241,20)]
print(f"Divisible by 20: {a}")

b=[x for x in range(21,241,21)]
print(f"Divisible by 21: {b}")


res=[x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0]
print(f"Result list: {res}")