def main():
    a=ask()
    b=ask()
    print(f"{a} % {b} is ",a%b)

# def ask():
#     while True:
#         try:
#             x=int(input("What is a no. bruh.... "))
#             # y=int(input("What is y bruh.... "))
#         except ValueError:
#             print("Enter an integer twatface")
#         else: 
#             return x 
            # return also breaks the code, infact it's much stronger than break
#refined version:

def ask():
    while True:
        try:
            return int(input("What is a no. bruh.... "))
        except ValueError:
            pass
            # print("Enter an integer twatface")
            # rather than prompting repetaedly we can just "pass"

main()