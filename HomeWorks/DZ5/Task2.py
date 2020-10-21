#Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

import sys

file_name = open("out_file.txt", "r")
lines = 0
words = 0

for line in file_name:
    lines += 1
    words=0
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

    print(f"Quality of words in {lines} lines: {words}")

print("Quality of lines in text:", lines)

file_name.close()