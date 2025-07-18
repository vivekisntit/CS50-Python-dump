amt=50
while amt>=0:
    print("Amount Due: ",amt)
    i=int(input("Insert Coin: "))
    if i==25 or i==10 or i==5:
        amt-=i
print("Change Owed: ",(amt*-1))


# amt = 50
# while amt > 0:
#     print("Amount Due:", amt)
#     i = int(input("Insert Coin: "))
#     if i in [25, 10, 5]:
#         amt -= i

# print("Change Owed:", abs(amt))



# THEY EWJ