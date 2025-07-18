from asn7_5 import count

def main():
    test_correct()

def test_correct():
    assert count("malan@harvard.edu")=="Valid"
    assert count("malan@@@harvard.edu")=="Invalid"
    assert count("vivek@harvardbussiness..edu")=="Invalid"
    assert count("kaddu")=="Invalid"
    # assert count("yummy")==0
    # assert count("gum")==0

if __name__ == "__main__":
    main()
