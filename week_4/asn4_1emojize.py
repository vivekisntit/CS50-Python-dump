import emoji
say=input("Input:")
for x in say.split(" "):
    print((emoji.emojize(x, language='alias')), end=" ")
