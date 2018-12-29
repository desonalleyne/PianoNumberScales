from random import randint
from time import sleep
import sys
from ordinal import ordinal
from scales import scales

# delay between flashes
num = int(sys.argv[1]) or 2

# scale being practiced
scaleLetter = sys.argv[2].upper() or 'C'

# selected scale to practice
scale = scales[scaleLetter]

while 1:
    r=randint(1,7)
    print('   {} tone of {}:  '.format(ordinal(r), scaleLetter), end=' ', flush=True)
    sleep(num)
    print(scale[r-1])
    sleep(1)
