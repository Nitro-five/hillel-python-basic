num_user = int(input('write number:'))

x_ten_thousand, y_ten_thousands = divmod(num_user, 10000)
x_thousands, y_thousands = divmod(y_ten_thousands, 1000)
x_hundred , y_hundred = divmod(y_thousands, 100)
x_ten , y_ten = divmod(y_hundred, 10)

num_revers= y_ten *10
num_revers = num_revers+x_ten
num_revers = num_revers*10
num_revers = num_revers+x_hundred
num_revers = num_revers*10
num_revers = num_revers+x_thousands
num_revers = num_revers*10
num_revers = num_revers+x_ten_thousand

print(num_revers)
