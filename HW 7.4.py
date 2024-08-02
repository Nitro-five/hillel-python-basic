
def common_elements():
    mult_3 = {i for i in range(100) if i % 3 == 0}
    mult_5 = {i for i in range(100) if i % 5 == 0}
    #print(mult_3)
    #print(mult_5)

    crossing_3_5 = mult_3 & mult_5
    #print(crossing_3_5)

    return crossing_3_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')