import json
import requests
import sys

if len(sys.argv)!=2:
    sys.exit()
got=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
print(json.dumps(got.json()))

# import json
# import requests
# import sys

# if len(sys.argv)>2:
#     sys.exit()
# got=requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])
# # print(json.dumps(got.json()))
# x=got.json()
# for result in x["results"]:
#     print(result["trackName"])
