while True:
    try:
        fra=input("Fraction:")
        num, den=fra.split("/")
        num=int(num)
        den=int(den)
        if num>den:
            den=0
        int(num/den)
    except (ValueError, ZeroDivisionError):
        continue
    else:
        break
sol=int(num)*100/int(den)
if 0<=(sol)<=1:
    print("E")
elif 100>=(sol)>=99:
    print("F")
else:
    print(f"{round(sol)}%")
