from datetime import date
import inflect
import sys

p=inflect.engine()

def main():
    dt=input("Date of Birth:")
    try:
        dob=date.fromisoformat(dt)
    except ValueError:
        sys.exit("Invalid date")
    now=date.today()
    mins=(now-dob).days*24*60
    print((word(mins)).capitalize()+" minutes")

def word(mins):
    final=p.number_to_words(mins, andword="")
    return final

if __name__ == "__main__":
    main()


# from datetime import date
# import inflect
# import sys

# p=inflect.engine()
# def main():
#     dt=input("Date of Birth:")
#     try:
#         dob=date.fromisoformat(dt)
#     except ValueError:
#         sys.exit("Invalid date")
#     now=date.today()
#     mins=(now-dob).days*24*60
#     # print(mins)
#     print((word(mins)).capitalize()+" minutes")  

# def word(mins):
#     # k=int(span(s.year,v.year))
#     # total=(int(v.year-s.year-k)*365*24*60+k*366*24*60)+(abs(s.month-v.month)*30*24*60)+(abs(s.day-v.day)*24*60)
#     # p=num2words(mins).replace("and ","")
#     # q=p.replace(",","#",1)
#     # x=(q.replace(",","")).replace("#",",")4
#     final=p.number_to_words(mins, andword="")
#     return final

# # def span(a, b):
# #     def leaps(y):
# #         return y // 4 - y // 100 + y // 400
# #     return leaps(b) - leaps(a - 1)

# if __name__ == "__main__":
#     main()


# from datetime import date, datetime
# from num2words import num2words
# import sys

# def main():
#     dt=input("Date of Birth:")
#     try:
#         s=datetime.strptime(dt,"%Y-%m-%d")
#     except ValueError:
#         sys.exit("Invalid date")
#     v=date.today()
#     p=num2words(calc(s,v)).replace("and ","")
#     q=p.replace(",","#",1)
#     print((q.replace(",","")).replace("#",",")+" minutes")

# def calc(s,v):
#     k=int(span(s.year,v.year))
#     total=(int(v.year-s.year-k)*365*24*60+k*366*24*60)+(abs(s.month-v.month)*30*24*60)+(abs(s.day-v.day)*24*60)
#     return total

# def span(a, b):
#     def leaps(y):
#         return y // 4 - y // 100 + y // 400
#     return leaps(b) - leaps(a - 1)

# if __name__ == "__main__":
#     main()
