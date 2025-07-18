from random import randint
def main():
    x=get_level()
    i=0
    s=0
    while i<10:
        i+=1
        a=generate_integer(x)
        b=generate_integer(x)
        ans=int(input(f"{a} + {b} ="))
        if ans==a+b:
            s+=1
            continue
        else:
            print("EEE")
            j=0
            while j<2:
                try:
                    ans=int(input(f"{a} + {b} ="))
                    if ans==a+b:
                        s+=1
                        break
                    else:
                        print("EEE")
                        j+=1
                except ValueError:
                    j+=1
                    continue
            if j==2:
                print(f"{a} + {b} = {a + b}")

    print("Score:",s)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(x):
    if x==1:
        return randint(0,9)
    elif x==2:
        return randint(10,99)
    else:
        return randint(100,999)

if __name__ == "__main__":
    main()
    
#####################################################
#####################################################

from random import randint
# def main():
#     x=get_level()
#     i=0
#     s=0
#     while i<4:
#         i+=1
#         a=generate_integer(x)
#         b=generate_integer(x)
#         ans=int(input(f"{a} + {b}="))
#         if ans==a+b:
#             s+=1
#             continue
#         else:
#             j=0
#             while j<3:
#                 print("EEE")
#                 try:
#                     j+=1
#                     ans=int(input(f"{a} + {b}="))
#                     if ans==a+b:
#                         s+=1
#                         break
#                 except ValueError:
#                     j+=1
#                     continue
#             if j==3:
#                 print(f"{a} + {b} = {a + b}")
            
#     print("Score:",s)
# # def get_level():
# #     # a=input("Level:")
# #     # return a
# #     while True:
# #         try:
# #             a=int(input("Level:"))
# #             if a not in range(1,4):
# #                 raise Exception
# #             else:
# #                 # print("h")
# #                 return a
# #         except Exception:
# #             continue

# def get_level():
#     while True:
#         try:
#             level = int(input("Level: "))
#             if level in [1, 2, 3]:
#                 return level
#         except ValueError:
#             pass

# def generate_integer(x):
#     if x==1:
#         return randint(0,9)
#     elif x==2:
#         return randint(10,99)
#     else:
#         return randint(100,999)

# if __name__ == "__main__":
#     main()


# # a=generate_integer(get_level())
#     # a=int(get_level())

# ######GPT#######

# # import random

# # def main():
# #     level = get_level()
# #     score = play_game(level)
# #     print(f"Score: {score}/10")

# # def get_level():
# #     while True:
# #         try:
# #             level = int(input("Level: "))
# #             if level in [1, 2, 3]:
# #                 return level
# #         except ValueError:
# #             pass

# # def generate_integer(level):
# #     if level not in [1, 2, 3]:
# #         raise ValueError("Invalid level")
# #     if level == 1:
# #         return random.randint(0, 9)
# #     elif level == 2:
# #         return random.randint(10, 99)
# #     else:
# #         return random.randint(100, 999)

# # def play_round(level):
# #     x = generate_integer(level)
# #     y = generate_integer(level)
# #     correct_answer = x + y
# #     tries = 0
# #     while tries < 3:
# #         try:
# #             answer = int(input(f"{x} + {y} = "))
# #             if answer == correct_answer:
# #                 return True
# #             else:
# #                 print("EEE")
# #                 tries += 1
# #         except ValueError:
# #             print("EEE")
# #             tries += 1
# #     print(correct_answer)
# #     return False

# # def play_game(level):
# #     score = 0
# #     for _ in range(10):
# #         if play_round(level):
# #             score += 1
# #     return score

# # if __name__ == "__main__":
# #     main()
