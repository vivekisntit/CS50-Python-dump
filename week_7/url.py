import re
url=input("spotify url:").strip()
artist=re.search(r"^(https?://)?(www\.)?spotify\.com/(.+)",url)
print("Artist:",artist[3])