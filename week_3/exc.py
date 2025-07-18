# try:
#     x=int(input("What is x bruh.... "))
#     y=int(input("What is y bruh.... "))
# except ValueError:
#     print("Enter an integer twatface")
# else:
#     print(f"{x} % {y} is ",x%y)
    # if "except" catches error "else" won't execute

# print(f"{x} % {y} is ",x%y)  # here it would execute and give NameError

while True:
    try:
        x=int(input("What is x bruh.... "))
        y=int(input("What is y bruh.... "))
    except ValueError:
        # print("Enter an integer twatface")
        continue
    else: 
        break
print(f"{x} % {y} is ",x%y)
# keeps on asking