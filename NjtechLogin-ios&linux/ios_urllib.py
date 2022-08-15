import urllib.request
import http.cookiejar
from re import search
import threading
from time import sleep

class AutoLoginIOS():

    ## 👤 请配置登录信息 ####################
    ## ✉️ 联系反馈：CSDN@ AlpHerkin(无白Herk)
    ## ✅ 软件官网：https://alpherk.github.io/NjtechAutoLogin/
    ## 📢 详细说明：https://blog.csdn.net/Alpherkin/article/details/120027504
    username = "201921166666" # 填入自己的学号
    password = "yourpassword" # 填入自己的密码
    broadban = "中国移动"   # 中国移动/中国电信
    #######################################


    ## ↓↓↓ 不熟悉python 以下代码谨慎修改 ↓↓↓ ##

    def __init__(self) -> None:
        pass

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
        url = "https://u.njtech.edu.cn/cas/login?service=https://u.njtech.edu.cn/oauth2/authorize?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code&state=njtech&s=f682b396da8eb53db80bb072f5745232"
        useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6)  AppleWebKit/605.1.15 (KHTML, like Gecko)  Version/15.2 Safari/605.1.15"
        requests = urllib.request.Request(url)
        response = urllib.request.urlopen(requests)
        dataInfo = response.read().decode('utf-8')

        lt       = search('lt\" value=\"(.*?)\"',        dataInfo).groups()[0]
        exe      = search('execution\" value=\"(.*?)\"', dataInfo).groups()[0]
        js       = search('jsessionid=(.*?)\">',         dataInfo).groups()[0]
        cookies  = F"JSESSIONID={js}; insert_cookie=97324480"
        posthead = {
            "Host": "u.njtech.edu.cn",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://u.njtech.edu.cn",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": cookies,
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": useragent,
            "Referer": url,
            "Content-Length": "207",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        }
        postdata = {
            "username":    self.username, "password":    self.password,
            "channelshow": self.broadban, "channel":     self.broadban,
            "lt":                     lt, "execution":             exe,
            "_eventId":         "submit", "login":               "登录"}
        request = urllib.request.Request(url, postdata, posthead)  
        response = urllib.request.urlopen(request)  
        # cookies  = http.cookiejar.CookieJar()
        # handler  = urllib.request.HTTPCookieProcessor(cookies)
        # opener   = urllib.request.build_opener(handler)
        # request  = urllib.request.Request(url, postdata, posthead)
        # response = opener.open(request)

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


if __name__ == '__main__':

    auto = AutoLoginIOS()

    auto.toConnect()

    print("执行完毕")
