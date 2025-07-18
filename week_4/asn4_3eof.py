import sys
nms={}
while True:
    try:
        say=input()
        nms[say]=""
    except EOFError:
        break
    else:
        continue
print("Adieu, adieu, to ", end="")
s=list(nms.keys())
n=len(nms.keys())
if n==1:
    print(s[0])
elif n>1:
    if n==2:
        print(f"{s[0]} and {s[1]}")
    elif n>2:
        i=0
        while i<n:
            if i!=n-1:
                s[i]=s[i].replace(s[i]," "+s[i]+",")
            else:
                s[n-1]=s[n-1].replace(s[n-1]," and "+s[n-1])
            i+=1
        s[0]=s[0].replace(" ","")
        for x in s:
            print(f"{x}", end="")
#

# adieu.py

names = []

try:
    while True:
        name = input()
        names.append(name)
except EOFError:
    pass

print("Adieu, adieu, to ", end="")

n = len(names)
if n == 1:
    print(names[0])
elif n == 2:
    print(f"{names[0]} and {names[1]}")
else:
    # All except last
    print(", ".join(names[:-1]), end="")
    # Oxford comma before the last name
    print(f", and {names[-1]}")


#

# import sys
# nms={}
# while True:
#     try:
#         say=input("Name:")
#         nms[say]=""
#     except EOFError:
#         break
#     else:
#         continue
# print("Adieu, adeiu, to ", end="")
# s=list(nms.keys())
# n=len(nms.keys())
# # print(n)
# # print(s)
# # print(s[n-1].replace(s[n-1],"and "+s[n-1]))
# if n==1:
#     print(s[0])
# elif n>1:
#     if n==2:
#         print(f"{s[0]} and {s[1]}")
#     elif n>2:
#         i=0
#         while i<n:
#             if i!=n-1:
#                 s[i]=s[i].replace(s[i],s[i]+",")
#             else:
#                 s[n-1]=s[n-1].replace(s[n-1],"and "+s[n-1])
#             i+=1
#         # print(s)
#         for x in s:
#             print(f"{x}", end="")
#     # else:
#     #     for x in s:
#     #         print(f"{x}",sep=",", end="")
