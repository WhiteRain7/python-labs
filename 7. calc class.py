import random
import math

def try_dec (func):
    def wrap (*args, **kwargs):
        try: return func(*args, **kwargs)
        except: print("You're " + ['retard', 'stupid', 'дебил'][random.randint(0, 2)]); return None
    return wrap


exec('''class calculator:
    def __init__ (self):
        self.vars = []

    def add_var (self, *values): self.vars.extend(values)
    def remove (self, index = -1): self.vars.pop(index)
    
    def clear (self): self.vars.clear()

    def sum (self, *args):
        result = 0
        if args:
            for arg in args: result += arg
        else:
            for arg in self.vars: result += arg
        return result

    def diff (self, a = None, b = None):
        try:
            if a == None: a = self.vars[0]
            if b == None: b = self.vars[1]
        except IndexError:
            print('Not enough values')
            return 0
        else: return a - b

    def mult (self, *args):
        result = 1
        if args:
            for arg in args: result *= arg
        else:
            for arg in self.vars: result *= arg
        return result

    def div (self, a = None, b = None):
        try:
            if a == None: a = self.vars[0]
            if b == None: b = self.vars[1]
        except IndexError:
            print('Not enough values')
            return 0
        else:
            if b == 0:
                print('Division by zero')
                return 1
            else: return a/b

    def power (self, a = None, b = None):
        try:
            if a == None: a = self.vars[0]
            if b == None: b = self.vars[1]
        except IndexError:
            print('Not enough values')
            return 0
        else: return a**b

    def abs (self, a = None):
        try:
            if a == None: a = self.vars[0]
        except IndexError:
            print('Not enough values')
            return 0
        else: return abs(a)

    def rnd (self, a = 1): return random.random()*a

    def fact (self, a = None):
        try:
            if a == None: a = self.vars[0]
        except IndexError:
            print('Not enough values')
            return 0
        else: return math.factorial(a)

    def acos (self, a = None):
        try:
            if a == None: a = self.vars[0]
        except IndexError:
            print('Not enough values')
            return 0
        else: return math.acos(a)

    def help (self):
        for atr in self.__dict__: None if atr.startswith('__') else print(' ~', atr)
'''.replace('def', '@try_dec\n    def'))


def main ():
    calc = calculator()

    print('available functions:')
    calc.help()

    while True:
        print('———————————————————————————————————')
        cmd = input('Function: ')
        values = input('Values: ')
        print('-----------------------------------')
        try: print(eval('calc.{func}({args})'.format(func = cmd, args = values)))
        except: pass

if __name__ == '__main__': main()
