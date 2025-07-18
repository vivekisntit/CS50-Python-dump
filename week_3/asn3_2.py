menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
bill = 0.00
while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            bill += menu[item]
            print(f"Total: ${bill:.2f}")
    except EOFError:
        break


# menu = {
#             "Baja Taco": 4.25,
#             "Burrito": 7.50,
#             "Bowl": 8.50,
#             "Nachos": 11.00,
#             "Quesadilla": 8.50,
#             "Super Burrito": 8.50,
#             "Super Quesadilla": 9.50,
#             "Taco": 3.00,
#             "Tortilla Salad": 8.00
#         }
# bill=0
# count=0
# while True:
#     try:
#         # print(f"tooootal: ${bill}")
#         ask=input("Item:")
#         # for x in menu.keys():
#         #     if x.lower()!=ask:
#         for x in menu.keys():
#             if x.lower()!=ask:
                
#                 val=menu[ask]       #kyuki menu me to ask kahi milega hi nhi
#             else:                   #menu me to keval x se milega kuch bhi
#                 bill+=menu[x]
#                 # print("else")
#                 print(f"Total: ${bill}")
#     except (KeyError, EOFError):
#         continue
#     else:
#         break

# # print("if")
#                 # print(x)
#                 # count+=1
#                 # continue