ops = {
    '+' : lambda a,b : a+b,
    '-' : lambda a,b : a-b,
    '/' : lambda a,b : a/b,
    '*' : lambda a,b : a*b,
    '%' : lambda a,b : a%b,
}

import sys
import datetime

fd = open(sys.argv[4], 'a+')
result = ops[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))
today = datetime.datetime.now()
today = today.strftime(f'%Y-%m-%d %H:%M:%S')
fd.write(f'{today} {sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}\n')