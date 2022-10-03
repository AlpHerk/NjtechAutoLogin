#### ✉️ 联系反馈：CSDN@ AlpHerkin(无白|Herk)
#### ✅ 软件官网：https://alpherk.github.io/NjtechAutoLogin/
#### 📢 详细说明：https://blog.csdn.net/Alpherkin/article/details/115599094
#### 🧊 代码版本：v1.0.1 


USR = "2019XXXXXXXX"  # 填入自己的学号
PWD = "XXXXXXXXXXXX"  # 填入自己的密码
COP = "中国移动"       # 中国移动/中国电信

"""

软件介绍
    此脚本为单文件，仅需安装了依赖模块、填写账号即可
    代码在原基础上增加了验证码识别，其他功能不变

使用步骤
 1. 在电脑上下载 python 安装包，链接：https://www.python.org/downloads/release
 2. 在控制台安装依赖
        pip install ddddocr
        pip install requests 
 3. 在最上方XXX处填写学号/密码/宽带
 4. 百度：开机启动 python 脚本
 5. 如果开机弹黑窗嫌烦，脚本后缀改为 .pyw
 6. 更详细的说明及疑惑，可私信我的 CSDN

其他说明
    若后期校园网验证码仍简单，会考虑更新 C++版的桌面软件、安卓App
    我会尽力保存软件体积小而美，不过现阶段只能采用这种脚本代码
    当然，得等我从考研狗进化后才能更新了

    欢迎关注我的 CSDN @AlpHerkin, GitHub @AlpHerk
    请收藏软件官网，也许哪天就突然更新了呢
    
"""

import re 
import ddddocr 
import requests
import threading
from time import sleep
requests.packages.urllib3.disable_warnings() 
# from library import requests

class AutoLogin():
    """ 参数：学号、密码、运营商
    """

    def __init__(self, usr, pwd, brand): 
        self.username = usr
        self.password = pwd
        self.brancorp = brand
        if   self.brancorp == '中国移动': self.bandabbr = '@cmcc'
        elif self.brancorp == '中国电信': self.bandabbr = '@telecom'

    def postLogin(self):
        """ 校园网认证核心代码 """
        resp = requests.get(url=LOGINURL,  headers=PSTHEADER,    verify=False)
        res2 = requests.get(url=CAPTCHURL, cookies=resp.cookies, verify=False)
        ocr  = ddddocr.DdddOcr(beta=True,  show_ad=False)          # 识别验证码
        capt = ocr.classification(res2.content)

        lt   = re.search('lt\" value=\"(.*?)\"',        resp.text).groups()[0]
        exe  = re.search('execution\" value=\"(.*?)\"', resp.text).groups()[0]
        form = {
            "username":    self.username,      "password":         self.password,
            "channelshow": self.brancorp,      "channel":     self.bandabbr,
            "lt":                 lt,     "execution":              exe,
            "_eventId":     "submit",     "captcha":              capt}
        requests.post(url=LOGINURL, headers=PSTHEADER, data=form, cookies=resp.cookies, verify=False)

    def loginThread(self):
        threads = []
        threads.append(threading.Thread(target=self.postLogin))
        threads.append(threading.Thread(target=self.__progressBar))
        for t in threads: t.start()
        for t in threads: t.join()

    def __progressBar(self):
        for i in range(11):
            print('\r正在连接：{0} {1}%'.format('▉▉'*i, (i*10)), end='');sleep(0.05)

    def isConnectNet(self):
        try: requests.get("https://www.baidu.com", headers=PSTHEADER, timeout=2, verify=False)
        except: return False
        return True

    def toConnect(self):
        # 第一次进行快速认证
        self.loginThread()

        # 进行稳定性检测
        for _ in range(5):
            try:
                if self.isConnectNet(): 
                    print("\n认证成功，请畅享网络~")
                    break
                else: self.loginThread()
            except: pass
            print("\n认证失败，请检查账号状态！")


################## 全局常量 请勿修改 ##################
LOGINURL  = "https://u.njtech.edu.cn/cas/login?service=https://u.njtech.edu.cn/oauth2/authorize?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code&state=njtech&s=f682b396da8eb53db80bb072f5745232"
CAPTCHURL = "https://u.njtech.edu.cn/cas/captcha.jpg"
USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15" 
PSTHEADER = {
    "Host": "u.njtech.edu.cn",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://u.njtech.edu.cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": USERAGENT,
    "Referer":    LOGINURL, 
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
} ############### 全局常量 请勿修改 ###################


if __name__ == '__main__':
   
    login = AutoLogin(USR, PWD, COP)

    login.toConnect()
  
