from asn8_2 import Jar

def test_init():
    jar=Jar()
    assert jar.capacity == 12
    jar=Jar(9)
    assert jar.capacity == 9

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == "🍪"

def test_deposit():
    jar=Jar()
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar=Jar()
    jar.deposit(8)
    jar.withdraw(7)
    assert str(jar) == "🍪"
