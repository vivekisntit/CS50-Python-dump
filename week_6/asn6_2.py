import sys
import pandas as pd
from tabulate import tabulate
k=0
menu=[]
d=[]
od=[]
if len(sys.argv)!=2:
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
elif not(sys.argv[1].endswith(".csv")):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1],"r") as x:
            lines=x.readlines()
            for line in lines:
                if k==0:
                    a,b,c=line.strip().split(",")
                    d=[a,b,c]
                    k+=1
                else:
                    oa,ob,oc=line.strip().split(",")
                    od=[oa,ob,oc]
                    menu.append(od)
        pf=pd.DataFrame(menu)
        # print(menu)
        print(tabulate(pf.style.hide(axis="index"), headers=d, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")





# if k==0:
#     a,b,c=line.strip(",")
#     d=[a,b,c]
#     k==1