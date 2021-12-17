import random as r
import math as m

r.seed(int(input()))
password = str(input())
keys = ['zAg', 'gb', 'N34', 'h@90', 'vql', 'N', 'Z', 'b', 'BsqY', 'ZcX', 'nBn', '1f5H4', 'sCrg', 'Gb', 'CyA', '#$fsq', 'Ho4', 'o!2s', 'z$h', 'am*', 'WgB', 'llkl', '<<jk', 'meMo', 'q|', 'Gm', 'sFgsa', 'oV', '^', 'vN', 'in', 'sId', 'LoV', 'nAt', 'GMB', 'f@1', 'z%6', '|s|', 'wEq']

output = ''
seeds = [ord(i) * m.sqrt(r.randint(100, 500)) for i in set(password)]

for i in seeds:
    r.seed(i)
    if i > len(set(password)):
        output += r.choice(list(set(password)))
        output += str(r.randint(20, 100))
        output += r.choice(keys)
        r.shuffle(keys)
    else:
        output += r.choice(keys)
        r.shuffle(keys)
        output += str(r.randint(10, 55))
        output += r.choice(keys)

print(output)

#123-password : d72CyAr46h@90a95sIdo41q|w90z%6r77nAtw51ino54N
#123-wordpass : o95gbr76z%6p45Gbs50wEqd100h@90d64wEqa96CyAo32sFgsa
#123-pass : a72CyAa72WgBp95Gma41sCrg

#123-password : r77sIdr63q|d99nBnw41h@90d33q|r831f5H4d51Gm
#123-wordpass : p72CyAr38meMoa95Zd50vqlp62gbw64q|p66LoV
#123-pass : a100sFgsas72vNa82f@1