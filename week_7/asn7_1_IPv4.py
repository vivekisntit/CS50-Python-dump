import re
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    
    if re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$",ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()  

# # a,b,c,d=ip.strip().split(".")
    # if -1<int(a)<256 and -1<int(b)<256 and -1<int(c)<256 and -1<int(d)<256:
    #     return f"valid"
    # else:
    #     return f"invalid"