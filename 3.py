import re


text = input('введите текст ')


list_of_words = re.findall(r'\w+', text.lower())

word_count = {}


for word in list_of_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

top_5_of_the_most_repeated_words = []

for word, count in word_count.items():
    top_5_of_the_most_repeated_words.append([count, word])

top_5_of_the_most_repeated_words.sort(reverse=True)

num = 1

for count, word in top_5_of_the_most_repeated_words[:5]:
    print(f'{num}) {word} - повторяется {count} раз')

    num += 1