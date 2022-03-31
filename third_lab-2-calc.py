import random
import math

ops = {
  '+':    [2, lambda x, y: x + y             ],
  '-':    [2, lambda x, y: x - y             ],
  '*':    [2, lambda x, y: x * y             ],
  '/':    [2, lambda x, y: x / y             ],
  '^':    [2, lambda x, y: x ** y            ],
  '||':   [1, lambda x   : abs(x)            ],
  'rnd':  [0, lambda     : random.random()   ],
  '!':    [1, lambda x   : math.factorial(x) ],
  'acos': [1, lambda x   : math.acos(x)      ]
}

op = input('Введите операцию ({}): '.format(', '.join(ops.keys())))

a = ops.get(op)
if a: print(a[1](*[int(input('Введите аргумент {}: '.format(i+1))) for i in range(a[0])]))
else: print('Операция недоступна')
