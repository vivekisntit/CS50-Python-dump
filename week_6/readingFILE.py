# with open("fwnds.txt", "r") as x:
#     lines=x.readlines()
# # for line in lines:
# #     print(f"{line.rstrip()} bhai")
# for line in lines:
#     print(f"{line.rstrip()} bhai")

with open("fwnds.csv") as x:
    lines=x.readlines()
    for line in lines:
        y=line.rstrip().replace(","," is ")
        print(f"{y}....") 