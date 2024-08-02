user_num = int(input('0-864000:'))
#user_num = 1900800
if 0 <= user_num < 8640000:
    print(user_num)
    if user_num <= 60:
        x_sec,y_sec = divmod(user_num,60)
        print(0,' днів, ',0,':',str(x_sec).zfill(2),':',str(y_sec).zfill(2), sep='')
    elif 60 < user_num < 3600:
        x_minute,y_minute=divmod(user_num,60)
        print(0,' днів, ',0,':',str(x_minute).zfill(2),':',str(y_minute).zfill(2), sep='')
    elif 3600 <= user_num < 86400:
        x_hour,y_hour=divmod(user_num,3600)
        x_sec_1,y_sec1 = divmod(y_hour,60)
        print(0,' днів, ',str(x_hour).zfill(2),':',str(x_sec_1).zfill(2),':',str(y_sec1).zfill(2), sep='')
    elif 86400<= user_num <8640000:
        x_day,y_day = divmod(user_num,86400)
        x_hour, y_hour = divmod(y_day, 3600)
        x_sec_1, y_sec1 = divmod(y_hour, 60)

        if x_day == 1 or (x_day > 20 and str(x_day)[-1] == '1'):
            day_ua = ' день'
        elif 2 <= x_day <= 4 or (x_day > 20 and str(x_day)[-1] in '234'):
            day_ua = ' дні'
        else:
            day_ua = ' днів'

        print(f"{x_day} {day_ua}, {str(x_hour).zfill(2)}:{str(x_sec_1).zfill(2)}:{str(y_sec1).zfill(2)}")
else:
    print("your num must be 0~8640000!")