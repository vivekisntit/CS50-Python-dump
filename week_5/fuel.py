# while True:
#     try:
#         # fra=input("Fraction:")
#         num, den=fra.split("/")
#         num=int(num)
#         den=int(den)
#         # if num>den:
#         #     den=0
#         # int(num/den)
#     except (ValueError, ZeroDivisionError):
#         continue
#     else:
#         break
# sol=int(num)*100/int(den)
# if 0<=(sol)<=1:
#     return "E"
# elif 100>=(sol)>=99:
#     return "F"
# else:
#     return f"{round(sol)}%"


# def main():
#     while True:
#         try:
#             fra=input("Fraction:")
#             num, den=fra.split("/")
#             num=int(num)
#             den=int(den)
#             # if num>den:
#             #     den=0
#             # int(num/den)
#         except ValueError:
#             continue
#         else:
#             break
#     convert(fra)


# def main():
#     fra=input("Fraction:")
#     x=convert(fra)
#     print(gauge(x))

# def convert(fraction):
#     num, den=fraction.split("/")
#     if not(num.isdigit()) or not(den.isdigit()):
#         raise ValueError
#     if num>den or den==0:
#         raise ZeroDivisionError
#     return int(int(num)*100/int(den))

# def gauge(percentage):
#     if 0<=(percentage)<=1:
#         return "E"
#     elif 100>=(percentage)>=99:
#         return "F"
#     else:
#         return f"{round(percentage)}%"

# if __name__ == "__main__":
#     main()

def main():
    while True:
        try:
            text = input("Fraction: ")
            print(gauge(convert(text)))
            break
        except (ValueError, ZeroDivisionError):
            pass
 
def convert(fraction):
    x = int(fraction.split(sep="/")[0])
    y = int(fraction.split(sep="/")[1])
    if y == 0:
        raise ZeroDivisionError
    elif x > y or x<0 or y<0:
        raise ValueError
    else:
        return int(x / y * 100)
 
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
 
if __name__ == "__main__":
    main()