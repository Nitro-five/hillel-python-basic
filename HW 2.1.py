num_user = int(input('write number:'))

x_thousands, y_thousands = divmod(num_user, 1000)

#print((x_thousands,y_thousands))

x_hundred , y_hundred = divmod(y_thousands, 100)
#print(x_hundred, y_hundred)

x_ten , y_ten = divmod(y_hundred, 10)
#print(x_ten, y_ten)

print(x_thousands)
print(x_hundred)
print((x_ten))
print((y_ten))


