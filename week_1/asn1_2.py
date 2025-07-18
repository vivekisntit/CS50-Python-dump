say=input("Greetings: ")
say=say.lower().strip()
val=say.find("hello",0,5)
if val==0:
    print("$0")
elif val==-1 and say[0]=='h':
    print("$20")
else:
    print("$100")