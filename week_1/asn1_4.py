exp=input("Expression: ")
a,x,b=exp.strip().split()
a=float(a)
b=float(b)
match x:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    