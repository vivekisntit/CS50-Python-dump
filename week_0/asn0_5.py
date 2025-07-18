m=input("Amount : ")
print (float(m.removeprefix("$")))

p=input("Tip : ")
print (float(p.removesuffix("%"))/100)