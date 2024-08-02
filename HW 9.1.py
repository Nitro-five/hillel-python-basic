def popular_words (text, words):
    text = text.lower()
    #print('lower:', text)
    text = text.split()
    #print('split:', text)
    text_count = {word: 0 for word in words}
    #print(type(text_count))
    for word in text:
        if word in text_count:
            text_count[word] += 1
    return text_count

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
