mt= [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
while True:
    try:
        date=input("Date:")
        m,d,y=date.split(" ")
        if m.isdigit():
            # print(d)
            continue
        # elif d.isdigit():
        #     print(d)
        #     continue
        elif not(d.isdigit()):
            # print("elif")
            d=int(d.replace(",",""))
            if m in mt and d<31: 
                # print("elif-if")
                m=int(mt.index(m))+1
                break
            else:
                # print(d)
                continue
        else:
            # print(d)
            continue
    except ValueError:
        m,d,y=date.split("/")
        # m=int(m)
        d=int(d)
        if m.isalpha() or m>12 or d>31:
            continue
        else:
            m=int(m)
            break
print(f"{y}-{m:02d}-{d:02d}")