import sys, requests

data = sys.argv[1]
url = "https://rockblock.rock7.com/rockblock/MT"
querystring = {"imei":"300234066638420","username":"aubrey@jaliko.com","password":"mak3rspac3","data":data}
response = requests.request("POST", url, params=querystring)
print(response.text)
