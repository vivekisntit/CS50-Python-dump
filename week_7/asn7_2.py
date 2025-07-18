import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    link=re.search(r"(https?://)(www\.)?(youtube\.com/embed/(.+)gG0)",s)
    if link is None or not(s.startswith("<iframe ")):
        return None
    elif link[2] is None:
        ans="https://"+link[3]
        v=ans.replace("youtube.com/embed/","youtu.be/")
        return v
    else:
        ans="https://"+link[2]+link[3]
        v=ans.replace("www.youtube.com/embed/","youtu.be/")
        return v

if __name__ == "__main__":
    main()


# import re

# def parse(s):
#     m = re.search(r"(https?://)(www\.)?(youtube\.com/embed/(.+)gG0)",s)
#     print(m)
#     return f'https://youtu.be/{m.group(2)}' if m!=None and s.startswith("<iframe ") else None
    
# print(parse(input("HTML: ")))
# doesn't work......chatgpt ka h



# re.sub(r"youtube\.com/embed/","youtu\.be/",s)
# v=ans.replace("www.youtube.com/embed/","youtu.be")

# import re

# def main():
#     print(parse(input("HTML: ")))

# def parse(s):
#     # match = re.search(r'https?://www\.youtube\.com/embed/([a-zA-Z0-9_-])', s)
#     match=re.search(r'(.+)"https?://w?w?w?.?youtube\.com/embed/(.+)"(.+)',s)
#     print(match)
#     if match:
#         video_id = match.group(2)
#         return f"https://youtu.be/{video_id}"
#     return None

# if __name__ == "__main__":
#     main()
