def main():
    msg=input("Enter thine msg...\n")
    print(convert(msg))

def convert(change):
    return (change.replace(":)","🙂").replace(":(","🙁"))

main()

# msg=input("Enter thine msg...\n")
# print(msg.replace(":)","🙂").replace(":(","🙁"))