msg=input("Input: ")
for c in msg:
    if c.lower() in ["a","e","i","o","u"]:
        msg=msg.replace(c,"")
print("output:",msg.strip())
