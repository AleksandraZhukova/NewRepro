#Task4
#Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"List: {a}")
new_a= [i for i in a if a.count(i) == 1]
print(f"Unique list number: {new_a}.")
#[23, 1, 3, 10, 4, 11]


my_list = list(input("Enter numbers. ").split())
print(f"Your list: {my_list}.")
new_my_list= [i for i in my_list if my_list.count(i) == 1]
print(f"Your unique list number: {new_my_list}.")