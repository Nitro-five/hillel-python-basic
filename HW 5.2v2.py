print('Calc')

user_act = input(" u wanna use  calc print 'Y' :")

while user_act.upper() == 'Y':
    user_first_num = int(input('first number:'))
    user_second_num = int(input('Second number:'))

    action = input('action:,+,-,*,/')

    if action == '+':
        print(user_first_num + user_second_num)
    elif action == '-':
        print(user_first_num - user_second_num)
    elif action == '*':
        print(user_first_num * user_second_num)
    elif action == '/':
        if user_second_num == 0:
            print('You cant divide by zero')
        else:
            print(user_first_num // user_second_num)
    else:
        print('Wrong command!')

    user_act = input(" u wanna use  calc print 'Y' or 'N' to stop :")

    if user_act.upper() == "N":
        break
