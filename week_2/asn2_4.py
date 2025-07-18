import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    b=0
    c=0
    x=len(s)
    if 1<x<7:
        b+=1
        if s[0].isalpha() and s[1].isalpha():
            b+=1
    else:
        b-=10

    for a in s:
        if a.isalpha() and c<1:
            b+=1
        elif a.isdigit():
            c+=1
            if b==2 and int(a)==0:
                b-=10
            else:
                b+=1
        elif a in string.punctuation:
            b-=10
    if b>=8:
        return True
    else:
        return False

# main()


# # max: 6 || min: 2
# # start: 2 atleast char
# # end: numbers
# # first num: not 0

import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    b = 0
    c = 0
    x = len(s)

    if 1 < x < 7:
        b += 1
        if s[0].isalpha() and s[1].isalpha():
            b += 1
    else:
        b -= 10

    number_started = False  # Track if number part has started

    for i in range(len(s)):
        a = s[i]
        if a.isalpha(): # and c < 1:
            b += 1
        elif a.isdigit():
            if not number_started:
                number_started = True
                if a == '0':
                    b -= 10  # first number can't be 0
            else:
                if not s[i:].isdigit():  # once number starts, rest must be all digits
                    b -= 10
            # c += 1
            b += 1
        elif a in string.punctuation:
            b -= 10

        # If letter appears after number has started → invalid
        if a.isalpha() and number_started:
            b -= 10

    if b >= 8:
        return True
    else:
        return False

main()
