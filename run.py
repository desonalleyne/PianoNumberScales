from random import randint
from time import sleep
import sys,os
from ordinal import ordinal
from scales import scales
scaleLetter = None
num = None
reps = 48

if len(sys.argv) > 2:
    # delay between flashes
    num = int(sys.argv[1]) or 2

    # scale being practiced
    scaleLetter = sys.argv[2].title()
    reps = 48

def mainMenu(scaleLetter, num, reps):
    if len(sys.argv) < 3:
        scaleLetter=input("Please enter a scale. eg: g# or ab or a: ").title()
        num=float(input("Please enter flash interval: "))
        reps=int(input("Please enter number of reps or press enter to continue: "))
        degrees=int(input("Please enter number of keys to use: "))
        reps = 99 if reps == 0 else reps
        
    for lvl in range(degrees,8):
        if lvl == 5:
            reps = 49 
        # selected scale to practice
        scale = scales[scaleLetter]
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(f"Flashing keys in the {scaleLetter} scale")
        print(f"    Interval: {num}s")
        print(f"    Reps: {reps}")
        print(f"    Degree: {lvl}")
        print("    Notes: " + ", ".join(scale[0:8]))
        print("===================")
        print()
        print()

        print('        Position:  Key')
        for r in range(1,lvl+1):
            print('   {} tone of {}:  {}'.format(ordinal(r), scaleLetter, scale[r-1]) )
        input("Press enter to continue... ")
        print()
        print()
        for i in range(reps):
            r=randint(1,lvl)
            print('   {} tone of {}:  '.format(ordinal(r), scaleLetter), end=' ', flush=True)
            sleep(num)
            print(scale[r-1])
            sleep(1)
    mainMenu(scaleLetter, num, reps)

mainMenu(scaleLetter, num, reps)
