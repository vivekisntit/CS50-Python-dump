import re
class Names:
    def __init__(aa, name, house):
        aa.name=name
        aa.house=house
    @property
    def name(aa):
        return aa._name

    @name.setter
    def name(aa, name):
        if re.search(r"^[a-zA-Z][0-9]",name.strip()):
            aa._name=name
        else:
            raise ValueError("Invalid name")
def process():
    name=input("Your codename:")
    house=input("What's your house:")
    return Names(name, house)

def control():
    info=process()
    info.house="cobra"
    print(f"{info.name} is a {info.house}")

control()