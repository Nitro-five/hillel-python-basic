def add_one(some_list):

    str_list = ''.join(map(str, some_list))

    int_list = int(str_list) + 1

    new_list = list(map(int, str(int_list)))
    return new_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
