import re
import sys

def main():
    # count(input("Text: "))
    print(count(input("Text: ")))

def count(s):
    c=0
    s1=re.sub(r"[^\w\s]","",s)
    d=[]
    d=s1.strip().split(" ")
    # print(d)
    for x in d:
        if re.search(r"^(um)$",x,re.IGNORECASE):
            c+=1
    return c
if __name__ == "__main__":
    main()
    # "[^a-z^0-9]um[^a-z^0-9]?\s?"
    # if re.search(r"um\s?[^a-zA-Z0-9]?",s,re.IGNORECASE):
    #     k=re.sub("um","___",s  )
    #     print(k)
    # else:
    #     print(None)
    # while True:
    #     if re.search(r"um",s):
    #         c+=1
    # return c

