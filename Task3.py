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