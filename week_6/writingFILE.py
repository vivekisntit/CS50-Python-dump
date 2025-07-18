# names=[]
# for x in range(3):
#     names.append(input("Your name sire.... "))
# for x in sorted(names):
#     print(f"I remember, {x}")
# # print("\n",names) 

# file=open("fwnds.txt","a")
# for x in range(3):
#     # names.append(input("Your name sire.... "))
#     file.write(f"{input("your name...?")}\n")
# file.close()

with open("fwnds.txt","a") as file:
    file.write(f"{input("your name...?")}\n")
file.close()

with open("fwnds.csv","a") as file:
    file.write(f"{input("your name...?")}\n")
file.close()