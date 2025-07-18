def main():
    time=input("What time is it? ")
    return convert(time)
def convert(tm):
    fs,ls=tm.split(":")
    s=float(fs)+float(ls)/60
    return s
t=main()
if 7<=t<=8:
    print("breakfast time")
elif 12<=t<=13:
    print("lunch time")
elif 18<=t<=19:
    print("dinner time")
 