class Greetings:
    ...

def min():
    say=input("Greetings:")
    say=say.strip()
    print(value(say))

def value(say):
    say=say.lower()
    val=say.find("hello",0,5)

    if val==0:
        return f"$0"
    elif val==-1 and len(say)>0 and say[0]=='h':
        return f"$20" 
    else:
        return f"$100"


if __name__=="__main__":
    min()