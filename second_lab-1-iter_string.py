i = 0

string = input()

for char in string:
	i += 1
	if i == 3 or i == len(string): continue
	if char == 'c' or char == 'с': print('Буква c на {}-ом месте'.format(i))
