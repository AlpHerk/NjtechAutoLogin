from asyncio.windows_events import NULL
import re
import sys
import requests as rq
import threading
from time import sleep

class AutoLogin():

    ## 👤 请配置登录信息 ####################
    ## ✉️ 联系反馈：CSDN@ AlpHerkin(无白Herk)
    ## ✅ 软件官网：https://alpherk.github.io/NjtechAutoLogin/
    ## 📢 详细说明：https://blog.csdn.net/Alpherkin/article/details/120027504
    username = "201921166666" # 填入自己的学号
    password = "yourpassword" # 填入自己的密码
    broadban = "中国移动"   # 中国移动/中国电信
    #######################################


    ## ↓↓↓ 不熟悉python 以下代码谨慎修改 ↓↓↓ ##

    def __init__(self):
        self.__getLoginData()

    def __getLoginData(self):
        errorflag = 0
        if not(self.username and self.password): errorflag = 1
        if   self.broadban == '中国移动': self.bandabbr = '@cmcc'
        elif self.broadban == '中国电信': self.bandabbr = '@telecom'
        else: errorflag = 2
        if errorflag == 1: print("请输入正确的学号和密码！")
        if errorflag == 2: print("请输入正确的运营商(中国移动/中国电信)")
        if errorflag: sys.exit(0)

    def __requestLogin(self):
        resp = rq.get(url=LOGINURL, headers=GETHEADER)
        lt   = re.search('lt\" value=\"(.*?)\"',        resp.text).groups()[0]
        exe  = re.search('execution\" value=\"(.*?)\"', resp.text).groups()[0]
        form = {
            "username":    self.username,         "password":    self.password,
            "channelshow": self.broadban,         "channel":     self.bandabbr,
            "lt":                     lt,         "execution":             exe,
            "_eventId":         "submit",         "login":               "登录"}
        rq.post(url=LOGINURL, headers=PSTHEADER, data=form, cookies=resp.cookies)

    def __loginThread(self):
        threads = []
        threads.append(threading.Thread(target=self.__progressBar))
        threads.append(threading.Thread(target=self.__requestLogin))
        for t in threads: t.start()
        for t in threads: t.join()

    def __progressBar(self):
        for i in range(11):
            print('\r正在连接：{0} {1}%'.format('▉▉'*i, (i*10)), end='');sleep(0.05)

    def __isConnectNet(self):
        try: rq.get("https://www.baidu.com", headers=GETHEADER, timeout=2)
        except: return False
        return True

    def toConnect(self):
        self.__loginThread()
        for _ in range(3):
            if self.__isConnectNet(): 
                print("\n认证成功，请畅享网络~")
                break
            else: self.__loginThread()
            print("\n认证失败，请检查账号状态！")


################## 全局常量 请勿修改 ##################
LOGINURL  = "https://u.njtech.edu.cn/cas/login?service=https://u.njtech.edu.cn/oauth2/authorize?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code&state=njtech&s=f682b396da8eb53db80bb072f5745232"
USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"
GETHEADER = {'User-Agent': USERAGENT}
PSTHEADER = {
    "Host": "u.njtech.edu.cn",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://u.njtech.edu.cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": USERAGENT,
    "Referer":    LOGINURL,
    "Content-Length": "207",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
} ############### 全局常量 请勿修改 ###################


if __name__ == '__main__':
 
    login = AutoLogin()
    
    login.toConnect()
