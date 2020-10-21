#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open("out_file.txt", "r") as my_file:
    salary = []
    less_salary = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           less_salary.append(i[0])
        salary.append(i[1])

    avr_salary=sum(map(int, salary)) / len(salary)


print(f"Salary less then 20.000: {less_salary}.\nAverage salary: {avr_salary}")