import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    indication_tag = False
    cleaned_text = ''

    for i in html:
        if i == '<':
            indication_tag = True
        elif i == '>':
            indication_tag = False
        elif not indication_tag:
            cleaned_text += i


    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)

    print(f"cleaned text in file {result_file}")

delete_html_tags('draft.html', 'cleaned.txt')
