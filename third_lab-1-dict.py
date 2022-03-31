# just a decoration
def declension_of (word, num_before):
  if num_before > 9 and str(num_before)[-2] == '1': return word + 'ов' # if 11, 12, ..., 111, 112
  num = str(num_before)[-1]
  if   num == '1': return word
  elif num == '2': return word + 'а'
  elif num == '3': return word + 'а'
  elif num == '4': return word + 'а'
  else: return word + 'ов'

 
keys = set(input('Введите слова через запятую: ').replace(', ', ',').split(','))

values = []
while len(values) < len(keys): 
  values.extend(
    list(input( 'Введите строку длиной {num} {word}: '.format(
                                                              num = len(keys) - len(values), 
                                                              word = declension_of('символ', len(keys) - len(values))) ))
  )
  
final_dict = {}
i = 0
for key in keys:
  final_dict[key] = values[i]
  i += 1
  
print()
print(final_dict)
