# just a decoration
def declension_of (word, num_before):
  if num_before > 9 and str(num_before)[-2] == '1': return word + 'ов' # if 11, 12, ..., 111, 112
  num = str(num_before)[-1]
  if   num == '1': return word
  elif num == '2': return word + 'а'
  elif num == '3': return word + 'а'
  elif num == '4': return word + 'а'
  else: return word + 'ов'
  
def get_set_from_input (sep = ','):
  return set(input('Введите слова через {}: '.format(sep)).replace(sep+' ', sep).split(sep))

def get_list_of_chars (min_length = 1):
  result = []
  while len(result) < min_length: 
    result.extend(
      list(input( 'Введите строку длиной {num} {word}: '.format(
                                                                num = min_length - len(result), 
                                                                word = declension_of('символ', min_length - len(result))) ))
    )
    
  return result
    
 def megre_into_dict (keys, values):
  result = {}
  
  i = 0
  for key in keys:
    result[key] = values[i]
    i += 1
    
  return result
 
keys = get_set_from_input()
values = get_list_of_chars(min_length = 1)
final_dict = megre_into_dict(keys, values)
  
print()
print(final_dict)
