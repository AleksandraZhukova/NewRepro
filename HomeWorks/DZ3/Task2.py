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