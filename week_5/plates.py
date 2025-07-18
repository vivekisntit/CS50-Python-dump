def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False

    chq = False  # Flag to check if number has started
    for char in s:
        if char.isdigit():
            if not chq:
                chq = True
                if char == '0':
                    return False
        elif chq:
            # Letter came after number started
            return False
    return True

if __name__ == "__main__":
    main()
