from random import randint
from time import sleep
import sys
from ordinal import ordinal

num = int(sys.argv[1]) or 2
scaleLetter = sys.argv[2].upper() or 'C'
print(num)
scales={'C': ['C','D','E','F','G','A','B'], 'F': ['F','G','A','Bb','C','D','E']}
scale = scales[scaleLetter]
while 1:
    r=randint(1,7)
    print('   {} tone of {}:  '.format(ordinal(r), scaleLetter), end=' ', flush=True)
    sleep(num)
    print(scale[r-1])
    sleep(1)
