lst = [1,2,3,4,5] # можно менять размер списка

a = len(lst)
b = a / 2
c = a / 3
print('list lenght:',a)

if a == 1:

    my_lst = lst
    my_second_lst = []
    lst_sum = [lst, my_second_lst]

    print(lst_sum)

elif a / 3 == c:

    b1 = a / 2
    my_lst = lst[:int(b1+1)]
    my_second_lst = lst[int(b1+1):]
    lst_sum = [my_lst, my_second_lst]

    print(lst_sum)


elif a / 2 == b:
    c1 = a / 2
    my_lst = lst[:int(c1)]
    my_second_lst = lst[int(c1) + 1:]

    #print(lst)
    #print(my_lst)
    #print(my_second_lst)

    lst_sum = [my_lst, my_second_lst]
    print(lst_sum)
