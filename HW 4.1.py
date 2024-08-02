#lst=[0,1,0,12,3]
#lst = [0]
#lst=[1,0,13,0,0,0,5]
lst=[9,0,7,31,0,45,0,45,0,45,0,0,96,0]
print(len(lst))

not_zero, zero = [], []

if len(lst)>1:
    for i in lst:
        if i == 0:
            not_zero.append(i)
        else:
            zero.append(i)
    print(zero + not_zero)
else:
    print(lst)
#if len(lst) > 1:
#    for i in range(len(lst) - lst.count(0)):
#        if lst[i] == 0:
#            lst.append(lst.pop(i))
#    print(lst)
#    print(len(lst))
#elif len(lst) <=1:
#   print (lst)


