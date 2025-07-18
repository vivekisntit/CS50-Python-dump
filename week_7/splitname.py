import re
name=input("Your name:").strip()
y=re.search(r"^(.+), (.+)$",name)
if y:
    last,first=y.groups()
    print(f"hello {first}")
else:
    first,last=name.split(" ")
    print(f"hello {first}")