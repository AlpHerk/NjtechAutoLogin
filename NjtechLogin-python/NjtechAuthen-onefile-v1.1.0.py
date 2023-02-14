#### ✉️ 联系反馈：CSDN@ AlpHerkin(无白|Herk)
#### ✅ 软件官网：https://alpherk.github.io/NjtechAutoLogin/
#### 📢 详细说明：https://blog.csdn.net/Alpherkin/article/details/115599094
#### 🧊 代码版本：v1.0.1 

USR = "2019XXXXXXXX"  # 填入自己的学号
PWD = "XXXXXXXXXXXX"  # 填入自己的密码
COP = "cmcc"          # cmcc/telecom
 

import requests
import re 

ip = ""
url = "http://10.50.255.11/a70.htm"
url_login = f"http://10.50.255.11:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.50.255.11&iTermType=1&mac=00-00-00-00-00-00&ip={ip}&enAdvert=0&queryACIP=0&jsVersion=2.4.3&loginMethod=1"
url_logout = f"http://10.50.255.11:801/eportal/?c=ACSetting&a=Logout&wlanuserip={ip}&wlanacip=10.50.255.1&wlanacname=me60&port=&hostname=10.50.255.11&iTermType=1&session=&queryACIP=0&mac=00-00-00-00-00-00&jsVersion=2.4.3"

session  = requests.session()
resp_a70 = session.get(url=url)
ip = re.search("v46ip=\'(.*?)\'", resp_a70.text).groups()[0]

form = {
    "DDDDD": f",0,{USR}@{COP}",
    "upass": PWD,
    "R1": "0",
    "R2": "0",
    "R3": "0",
    "R6": "0",
    "para": "00",
    "0MKKey": "123456", 
}

session.post(url=url_login, data=form)    # 网络认证
# session.post(url=url_logout, data=form) # 退出认证

