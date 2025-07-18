import sys
import csv
f2=[]
if len(sys.argv)!=3:
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
elif not(sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1],"r") as x:
            read =csv.DictReader(x)
            for r in read:
                y,x=r["name"].split(", ")
                f2.append({"first":x, "last":y, "house":r["house"]})
    except FileNotFoundError:
        sys.exit("Could not read",sys.argv[1])

    try:
        with open(sys.argv[2],"w", newline="") as y:
            hed=["first","last","house"]
            f3=csv.DictWriter(y,fieldnames=hed)
            f3.writeheader()
            f3.writerows(f2)
    except FileNotFoundError:
        sys.exit("Could not read",sys.argv[2])


# import csv
# guys=[]
# with open("before.csv") as x:
#     reader =csv.DictReader(x)
#     for row in reader:
#         x,y=row["name"].split(", ")
#         guys.append({"name":y, "type":row["house"]})

# for guy in sorted(guys, key=lambda guy: guy["type"]):
#     print(f"{guy["name"]} is {guy["type"].strip()}")