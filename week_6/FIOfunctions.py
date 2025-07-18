# store=[]

# with open("fwnds.txt") as x:
#     for line in x:
#         store.append(line.rstrip())
# for data in sorted(store):
#     print(f"{data} bhai")

# with open("fwnds.txt") as x:
#     for line in sorted(x, reverse=True):
#         print(f"{line.rstrip()} bhai")

guys=[]
with open("fwnds.csv") as x:
    for line in x:
        name, type=line.strip().split(", ")
        data={"name":name,"type":type}
        guys.append(data)
        # print(guys)

# def giveName(guy):
#     return guy["name"]

# for guy in sorted(guys, key=giveName):
#     print(f"{guy["name"]} seems to be {guy["type"]}")

for guy in sorted(guys, key=lambda guy: guy["type"]):
    print(f"{guy["name"]} is from {guy["type"]}")
