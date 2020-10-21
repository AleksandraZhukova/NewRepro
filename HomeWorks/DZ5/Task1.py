#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.

out_f = open("out_file.txt", "w")
str_list = input("Enter text \n")

while True:
    if str_list=="":
        break
    else:
        str_list = input("Enter text \n")
        out_f.writelines(str_list)
out_f.close()

out_f = open("out_file.txt", "r")
content = out_f.readlines()
print(content)
out_f.close()