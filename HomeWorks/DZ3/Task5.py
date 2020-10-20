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

my_sum ()