import re
mail=input("Enter college email:")
if re.search(r"^[0-9]+@[^@]+\.in$",mail):
    print("valid")
else:
    print("Invalid")