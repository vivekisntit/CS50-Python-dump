class States:
    def __init__(ff, state, city, army):
        ff.state=state
        ff.city=city
        ff.army=army
    def __str__(ff):
        return f"{ff.city} is in {ff.state}"

def main():
    place=info()
    print(place)
# f"{place.city} is in {place.state}"

def info():
    state=input("What state:")
    city=input("What city:")
    army=input("Army size:")
    return States(state, city, army)

if __name__=="__main__":
    main()