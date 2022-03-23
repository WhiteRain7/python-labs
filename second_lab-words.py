words = []
count = []
max_word_len = len('слово')
max_num_len = len('количество')


# entering new words until len becomes 3 or more
while len(words) < 3: words.extend(input('Введите 3 слова через пробел: ').split(' '))

# printing each word in 3 formats
for word in words: 
    if len(word) > max_word_len: max_word_len = len(word)
    print('{0} {1} {2}'.format(word.lower(), word.upper(), word.capitalize()))
print()

# entering the number of each word
for word in range(len(words)): 
    count.append(int(input('Введите количество слова ' + words[word] + ': ')))
    if len(str(count[word])) > max_num_len: max_num_len = len(str(count[word]))
print()

# some constants for table below
len_3 = len('нижний регистр')
len_4 = len('ВЕРХНИЙ РЕГИСТР')
len_5 = len('Как в предложении')

# heading of table (word_[n] - words for the table title, len_[n] - column width)
print(' {word_1:>{len_1}} | {word_2:<{len_2}}  ||  {word_3:^{len_3}} | {word_4:^{len_4}} | {word_5:^{len_5}}'.format(word_1 = 'слово', 
                                                                                                                     word_2 = 'количество',
                                                                                                                     word_3 = 'нижний регистр',
                                                                                                                     word_4 = 'ВЕРХНИЙ РЕГИСТР',
                                                                                                                     word_5 = 'Как в предложении',
                                                                                                                     len_1 = str(max_word_len),
                                                                                                                     len_2 = str(max_num_len),
                                                                                                                     len_3 = str(max(max_word_len, len_3)),
                                                                                                                     len_4 = str(max(max_word_len, len_4)),
                                                                                                                     len_5 = str(max(max_word_len, len_5)),
                                                                                                                     ))
# body of table
for word in range(len(words)):
  print(' {word_1:>{len_1}} | {word_2:<{len_2}}  ||  {word_3:-^{len_3}} | {word_4:-^{len_4}} | {word_5:-^{len_5}}'.format( word_1 = words[word], 
                                                                                                                           word_2 = count[word],
                                                                                                                           word_3 = words[word].lower(),
                                                                                                                           word_4 = words[word].upper(),
                                                                                                                           word_5 = words[word].capitalize(),
                                                                                                                           len_1 = str(max_word_len),
                                                                                                                           len_2 = str(max_num_len),
                                                                                                                           len_3 = str(max(max_word_len, len_3)),
                                                                                                                           len_4 = str(max(max_word_len, len_4)),
                                                                                                                           len_5 = str(max(max_word_len, len_5)),
                                                                                                                           ))
