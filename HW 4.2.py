#lst = [0,1,5,7,9,5]
#lst = [5]
lst = []
if len(lst) == 0:
    print(0)
else:
    a= lst[::2]
    print(a)
    print (lst[-1])
    sum_a=0
    for i in a:
        sum_a += i
    print (sum_a)
    b = sum_a*lst[-1]
    print (b)