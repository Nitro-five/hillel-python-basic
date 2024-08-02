import string
import keyword

user_str = input()
#user_str='assert_exception'

if user_str[0].isdigit():
    print('digit',False)
elif user_str[0].istitle():
    print('title', False)
elif user_str == '__' or user_str=='___':
    print(False)
elif any(i.isupper() for i in user_str):
    print('upper', False)
elif keyword.iskeyword(user_str):
    print('keyword',False)
elif any(i.isspace() for i in user_str):
    print('space',False)
elif any(i in string.punctuation and i != '_' for i in user_str):
    print("punctuation or space", False)
else:
    print(True)







