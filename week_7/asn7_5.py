import validators
def main():
    print(count(input("What's your email address?")))

def count(s):
    if validators.email(s):
        return f"Valid"
    else:
        return f"Invalid"
if __name__ == "__main__":
    main()