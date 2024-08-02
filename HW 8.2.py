def is_palindrome(text):

    text = text.lower().replace(" ", "")
    #print(text)
    text = text.replace(":","")
    #print(text)
    text = text.replace(",","")
    #print(text)
    text = text.replace(".", "")
    #print(text)

    #print(text == text[::-1])
    return text == text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")