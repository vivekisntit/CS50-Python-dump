from random import randint
import sys
while True:
    try:
        a=int(input("Level:"))
        if(a<0):
            raise Exception
    except Exception:
        continue
    else:
        break
c=randint(1,a)
while True:
    try:
        g=int(input("Guess:"))
        while True:
            if g<0:
                raise Exception
            elif g>c:
                print("Too large!")
                raise Exception
            elif g<c:
                print("Too small!")
                raise Exception
            else:
                sys.exit("Just right!")
    except Exception:
        continue 