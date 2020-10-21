#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summ():
    try:
        with open("out_file.txt", "w+") as file_obj:
            numbers = input("Enter numbers\n")
            file_obj.writelines(numbers)
            numbers = numbers.split()

            print(sum(map(int, numbers)))
    except ValueError:
        print("Input Error")


summ()