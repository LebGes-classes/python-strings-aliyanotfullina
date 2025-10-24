text = input('введите текст ')

list_of_words = []
word = ""
last_char = ''

for char in text:
    if char == ' ':
       if last_char != ',':
            if word:
                list_of_words.append(word)
                word = ''
    elif char == '.' or char == ',':
        if word:
            list_of_words.append(word)
            word = ""
    else:
        word += char
    last_char = char

if word:
    list_of_words.append(word)

k = 0
ind = 0
num = 0
k_and_ind = []

for word in list_of_words:
    if k < len(word):
        k = len(word)
        ind = num
    num += 1

word = list_of_words[ind]

low_alph = 'abcdefghijklmnopqrstuvwxyz'
high_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

shifr_word = ''

for char_ind in range(k):
    if word[char_ind] in high_alph:
        shifr_word += high_alph[(high_alph.index(word[char_ind]) + k) % 26]
    elif word[char_ind] in low_alph:
        shifr_word += low_alph[(low_alph.index(word[char_ind]) + k) % 26]
    else:
        shifr_word += word[char_ind]

for symb_ind in range(text.index(word)):
    print(text[symb_ind], end='')

print(shifr_word, end='')

for symb_ind in range(text.index(word) + len(word), len(text)):
    print(text[symb_ind], end='')

print(' - зашифрованный текст')
print(k, '- число К')