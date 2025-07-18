import csv
name=input("Your name?")
favnum=input("What's your favourite number?")
# with open("numero.csv","a") as x:
#     writer=csv.writer(x)
#     writer.writerow([favnum,name])
with open("numero.csv","a") as x:
    writer=csv.DictWriter(x,fieldnames=["number","name"])
    writer.writerow({"name":name, "number":favnum})