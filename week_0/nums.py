# a=input("Enter a.... ")         # 1 way
# # b=input("Enter b.... ")
# # z=int(a)+int(b)
# a=int(input("Enter a.... "))    # 2 way
# b=int(input("Enter b.... "))
# z=a+b
# print(z)                        # 3 way 
# print(int(input("Enter a.... "))+int(input("Enter b.... ")))
# a=float(input("Enter a.... "))   
# b=int(input("Enter b.... "))
# z=a+b
# print(f"{z:.5f}")                 # 1 way to round off
# print(round(z,1))                 # other way to round off
# Create our own function
def hello(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()