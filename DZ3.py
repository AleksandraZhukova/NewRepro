#Task1

def devide_func(var1, var2):
    if var2=0:
        print("Devide error. Zero")
        return
    else:
        res=var1/var2
        return (f" Reesult of devide is: {res}")

while True:
    my_var1=float(input("Type first variable"))
    my_var2=float(input("Type second variable"))

    print(devide_func(my_var1, my_var2))



#Task2

def presonal_dates(name, surname, year, city, email, phone_number):
    dates=(f"Ваши персональные данные: {name} {surname}, {year} {city} {email} {phone_number}.")
    return dates




my_name=input("Type your name: ")
my_surname=input("Type your surnasme: ")
my_year=input("Type your birth year: ")
my_city=input("Type your city of residence: ")
my_email=input("Type your email: ")
my_phone_number=input("Type your phone number: ")

print(presonal_dates(my_name, my_surname, my_year, my_city, my_email, my_phone_number))

print(presonal_dates("Vasily", "Petrov", city="Moscow", email="vasily.petrov@yandex.ru", year="1876", phone_number="8(916)111-22-33"))


#Task3

def my_func(var1, var2, var3):
    a=[var1, var2, var3]
    res=sum(a)-min(a)
    return res

while True:
    my_var1=float(input("Type first variable "))
    my_var2=float(input("Type second variable "))
    my_var3=float(input("Type third variable "))

    print(my_func(my_var1, my_var2, my_var3))



#Task4.1 Method

def my_func(var1, var2):
    res=x**y
    return res


while True:
    x = float(input("Type + variable "))
    y = float(input("Type - variable "))

    print(my_func(x, y))

#Task4.2 Method

def my_func(var1, var2):
    res = 1
    i = 1
    while i <= abs(y):
        res = res * (1 / x)
        i += 1
    return res

while True:
    x=float(input("Type plus variable"))
    y=float(input("Type minus variable"))

    print(my_func(x, y))



#Task5

def my_sum ():
    sum_res = 0
    ex = True
    while ex == True:
        new_sum=0
        numbers = input("Type numbers. For break type q or Q ").split()
        for i in range(len(numbers)):
            if numbers[i] == 'q' or numbers[i] == 'Q':
                ex = False
                break
            else:
                new_sum = new_sum + int(numbers[i])
        sum_res = sum_res + new_sum
        print(f"Sum: {sum_res}")
    return sum_res
    print(f"End of program. Your result: {sum_res}")

my_sum()

#Task6

def int_func(text):
    text=text.title()
    return text

my_text=input("Type word. ")
print(int_func(my_text))


my_huge_text=input("Type text. ")
print(int_func(my_huge_text))




