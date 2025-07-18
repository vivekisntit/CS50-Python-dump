import sys
if len(sys.argv)!=2:
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
elif not(sys.argv[1].endswith(".py")):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1],"r") as x:
            lines=x.readlines()
            k=0
            for line in lines:
                if line.strip().startswith("#") or line.isspace():
                    continue
                else:
                    k+=1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(k)


