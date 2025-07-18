# shop={}
# while True:
#     try:
#         i=1
#         mark=input("Enter: ").upper()
#         shop[mark]=i
#         if mark in shop.keys():
#             # print("pass")
#             shop[mark]+=1
#         # print("ass")
#     except EOFError:
#         break
# print(shop)
# shop1=dict(sorted(shop.items()))
# kount=0
# # print(len(shop.keys()))
# print(shop1)
# for x in shop1.keys():
#     for y in shop1.keys():
#         if x==y:
#             # print("iiiii")
#             kount+=1
#         # else:
#         #     # print("eeeee")
#         #     continuez
#     print(f"{kount} {x}")
#     kount=0

shop = {}
while True:
    try:
        i = 1
        mark = input("Enter: ").upper()  # Convert early for consistency
        if mark in shop:
            shop[mark]+=1
        else:
            shop[mark]=i
    except EOFError:
        break

print(shop)

shop1 = dict(sorted(shop.items()))
kount = 0
print(shop1)

for x in shop1.keys():
    print(f"{shop1[x]} {x}")