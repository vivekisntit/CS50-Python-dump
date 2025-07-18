#### final correct ####

import sys
from pyfiglet import Figlet
x=Figlet()
if len(sys.argv)==2:
    sys.exit("Invalid usage")
elif len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[1]=='--font'):
    if  sys.argv[2] in x.getFonts():
        ask=input("Input:")
        x.setFont(font=sys.argv[2])
        print(x.renderText(ask))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")




# import sys
# import pyfiglet
# from pyfiglet import Figlet
# # print(pyfiglet.figlet_format("EmpirE"))
# # c=Figlet()
# ask=input("Input:")
# if len(sys.argv)==1:
#     print(pyfiglet.figlet_format(ask))
# elif len(sys.argv)==3:
#     if (sys.argv[1]=='-f' or sys.argv[1]=='--font') and sys.argv[2]==Figlet().getFonts():
#         print(pyfiglet.figlet_format(ask, font=sys.argv[3]))
# else:
#     sys.exit


# import sys
# # import pyfiglet
# from pyfiglet import Figlet
# # print(pyfiglet.figlet_format("EmpirE"))
# x=Figlet()
# # ask=input("Input:")
# if len(sys.argv)==1:
#     # x.setFont(font="")
#     ask=input("Input:")
#     print(x.renderText(ask))
# elif len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[1]=='--font'):
#     if  sys.argv[2] in x.getFonts():
#         x.setFont(font=sys.argv[2])
#         ask=input("Input:")
#         print(x.renderText(ask))
# else:
#     sys.exit("Invalid usage")



# # x.getFonts()
#         # x.setFont(font=sys.argv[2])
#         # sys.argv[2]==x.getFonts()
#         print(x.renderText(ask))

