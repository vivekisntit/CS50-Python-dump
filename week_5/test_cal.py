from calc import root
import math

def test_root():
    for x in range(0,10):
        if math.sqrt(x)==root(x):
            print(":)")
        else:
            print("not working bruh....")

def main():
    test_root()

if __name__=="__main__":
    main()