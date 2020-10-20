def devide_func(var1, var2):
    if var2==0:
        print("Devide error. Zero")
        return
    else:
        res=var1/var2
        return (f" Result of devide is: {res}")

while True:
    my_var1=float(input("Type first variable "))
    my_var2=float(input("Type second variable "))

    print(devide_func(my_var1, my_var2))
