cam=input("camelCase: ")
for c in cam:
    if c.isupper():
        x=cam.find(c)
        cam=cam.replace(cam[x],"_"+(cam[x]).lower())
        
print(cam)

# cam = input("camelCase: ")
# snake = ""

# for c in cam:
#     if c.isupper():
#         snake += "_" + c.lower()
#     else:
#         snake += c

# print(snake)
