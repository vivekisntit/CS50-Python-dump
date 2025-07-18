import sys
try:
    print("how u doin", sys.argv[2])
except IndexError:
    print("u alr fam")

# import sys
# if len(sys.argv)<3:
#     sys.exit("u mumblin or wt?")
# elif len(sys.argv)>3:
#     sys.exit("sehr laut bruh.....")
# else:
#     for ar in sys.argv:
#         print("how u doin",ar)

# import sys
# if len(sys.argv)<3:
#     sys.exit("u mumblin or wt?")
# elif len(sys.argv)>3:
#     sys.exit("sehr laut bruh.....")
# else:
#     for ar in sys.argv[1:]:                 # new
#         print("how u doin",ar)
