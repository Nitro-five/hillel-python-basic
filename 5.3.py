import  string

user_str = input('your str:')

for i in string.punctuation:
    if i in user_str:
        user_str = user_str.replace(i,'')
        user_str = user_str.title()
print(user_str)


del_space = user_str.split()
del_space = ''.join(del_space)

print(del_space)

if len(del_space) <= 140:
    hashtag = '#'+''.join(del_space)
    print(hashtag)
elif len(del_space) > 140:
    hashtag = '#' + ''.join(del_space[:140])
    print(hashtag)
else:
    print('something going wrong')
