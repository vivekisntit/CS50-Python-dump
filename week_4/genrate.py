# import random
# isit=True
# while isit:
#     choice=random.choice(["up","dn","flat"])  #random.choice()
#     print(choice)
#     if choice=="up":
#         isit=False

# import random
# while True:
#     choice=random.choice(["up","dn","flat"])  #random.choice()
#     print(choice)
#     if choice=="up":
#         break

# from random import choice
# while True:                                   #random.choice()
#     choic=choice(["up","dn","flat"])
#     print(choic)
#     if choic=="up":
#         break

from random import randint                       #random.randint()
while True:
    choic=randint(1,10)
    print(choic)
    if choic==7:
        break

# from random import shuffle
# cards=["jack","jill","brokeup"]
# print(cards[0],"\n")
# shuffle(cards)
# for fate in cards:
#     print(fate)
# print("\n",cards[0])