text = input('введите текст ')

list_of_words = []
word = ""

for char in text:
    if char == ' ':
        if word:
            list_of_words.append(word)
            word = ""
    else:
        word += char

if word:
    list_of_words.append(word)

num = -1


for _ in list_of_words:
    print(list_of_words[num], end=' ')

    num -= 1

print('- зеркальный вид введённой строки')

num = -1

for char in text:
    print(text[num], end = '')

    num -= 1

print('- строка в обратном порядке')