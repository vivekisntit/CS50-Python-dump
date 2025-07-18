import csv
guys=[]
with open("fwnds.csv") as x:
    # for line in x:
    #     name, type=line.strip().split(", ")
    #     data={"name":name,"type":type}
    #     guys.append(data)
    reader =csv.DictReader(x)
    for row in reader:
        guys.append({"name":row["Verdon"], "type":row["Max"]})

for guy in sorted(guys, key=lambda guy: guy["name"]):
    print(f"{guy["name"]} is {guy["type"].strip()}'s hometown")
