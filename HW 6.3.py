user_num = int(input("Your number: "))
#user_num= 1
while user_num > 9:
    one_num = 1
    int_num = user_num

    while int_num > 0:
        digit = int_num % 10
        one_num *= digit
        int_num //= 10

    user_num = one_num

print(user_num)
