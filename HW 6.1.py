import string

user_str_a= input("Print a~Z:")

print(string.ascii_letters)

tum = (string.ascii_letters)
ind_a = tum.index(user_str_a[0])
ind_b = tum.index(user_str_a[2])
print(tum[ind_a: ind_b+1])