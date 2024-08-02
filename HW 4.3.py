import random

lst_random = [random.randint(1,100) for i in range(random.randint(3,10))]

print(lst_random)
new_lst = []

for i in lst_random :
    if i == lst_random[0] :
        new_lst.append(i)
    elif i == lst_random[2]:
        new_lst.append(i)
    elif i == lst_random[-2]:
        new_lst.append(i)
print(new_lst)
