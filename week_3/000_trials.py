# a=0
# while True:
#     try:
#         date=input("Date:")
#         m,d,y=date.split(" ")
#         # d =int(d.replace(",",""))
#         if m.isdigit() or d[1]!=",":
#             # print("hello")
#             continue
#             # raise TypeError
#         elif m in mt:
#             d =int(d.replace(",",""))
#             if m>12 or d>31:
#                 continue
#             else:
#                 m=mt.index(m)+1
#                 break
#     except Exception:
#         m,d,y=date.split("/")
#         if m>12 or d>31 or m.isalpha():
#             continue
#         else:
#             break
# # d =int(d)
# # if a==1:
#     # m=mt.index(m)+1
# print(f"{y}-{int(m):02d}-{int(d):02d}")

# print(f"{y}-{m:03d}-"+"{:02d}".format(d))

# print(f"{x},{y},{z}")
