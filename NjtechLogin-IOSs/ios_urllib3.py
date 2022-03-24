import requests
req = requests.request('GET', 'http://httpbin.org/get')
if req.status_code: print("成功！！")
print(requests.get("https://gitee.com/mersakk/stash/raw/master/getstash.py").text)