import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    y=re.search(r"(\d?\d):?(\d?\d)?\s([A-Z][A-Z]) to (\d?\d):?(\d?\d)?\s([A-Z][A-Z])",s)
    if y==None:
        raise ValueError
    h=([int(y[1]),int(y[4])])
    m=[y[2],y[5]]
    m1=[0 if x is None else x for x in m]
    if not(all(a<13 for a in h)) or not(all(int(b)<60 for b in m1)):
        raise ValueError
    else:
        if y[3]=="PM":
            h[0]=h[0]+12 if h[0]!=12 else 12
        elif y[6]=="PM":
            h[1]=h[1]+12 if h[1]!=12 else 12
        h[0]=0 if (y[3]=="AM"  and h[0]==12) else h[0]
        h[1]=0 if (y[6]=="AM"  and h[1]==12) else h[1]
    return f"{h[0]:02d}:{int(m1[0]):02d} to {h[1]:02d}:{int(m1[1]):02d}"
if __name__ == "__main__":
    main()    
    # print(y[1])
    # print(y[2])
    # print(y[3])
    # print(y[4])
    # print(y[5])
    # print(y[6])
    # print(y)

# if (all(a>12 for a in h)) or (all(int(b)>59 for b in m1)):
#         raise ValueError
