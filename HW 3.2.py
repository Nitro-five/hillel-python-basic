lst=list(input("input list numbers:"))
#lst = [1, 5, 8, 6, 12]

print(lst)

lst_len = len(lst)
lst_len_minus = lst_len-1

if lst_len_minus >1 :
     pop_lst_4=lst.pop(lst_len_minus)
     pop_lst_0=lst.pop(0)
     insert_lst_0 = lst.insert(0, pop_lst_4)
     insert_lst_4=lst.insert(int(lst_len),pop_lst_0)
     print(lst)
else:
    print(lst)