import random as r
import math as m

r.seed(int(input()))
password = str(input())
keys = ['zAg', 'gb', 'N34', 'h@90', 'vql', 'N', 'Z', 'b', 'BsqY', 'ZcX', 'nBn', '1f5H4', 'sCrg', 'Gb', 'CyA', '#$fsq', 'Ho4', 'o!2s', 'z$h', 'am*', 'WgB', 'llkl', '<<jk', 'meMo', 'q|', 'Gm', 'sFgsa', 'oV', '^', 'vN', 'in', 'sId', 'LoV', 'nAt', 'GMB', 'f@1', 'z%6', '|s|', 'wEq']

output = ''
seeds = [ord(i) * m.pow(r.randint(100, 500), len(password)) for i in list(password)]

for i in seeds:
    r.seed(i)
    if i > len(set(password)):
        output += str(r.randint(20, 100))
        output += r.choice(keys)
        r.shuffle(keys)
    else:
        output += r.choice(keys)
        r.shuffle(keys)
        output += str(r.randint(10, 55))
        output += r.choice(keys)

print(output)

#123-password : 84b22b37Gb54llkl57llkl50h@9050am*68N34
#123-wordpass : 43llkl78sFgsa91#$fsq21^79#$fsq95nAt73ZcX24<<jk
#123-pass :29in60sId30nAt96N34
#123-passwork : 84b22b37Gb54llkl57llkl50h@9050am*91z$h

#great dependance of passwords' length...