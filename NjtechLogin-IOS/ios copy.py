import threading
from re import search
from time import sleep
from requests import get, post


class AutoLogin():

    """ 自行配置以下属性 """
    username = "20192114" # 填入自己的学号
    password = "66666666" # 填入自己的密码
    broadban = "中国移动"  # 宽带运营商：中国移动/中国电信


    def __init__(self):

        try: self.getLoginData()
        except: print("请正确配置校园网账号信息!")


    def getLoginData(self):

        if   self.broadban == '中国移动': self.bandabbr = '@cmcc'
        elif self.broadban == '中国电信': self.bandabbr = '@telecom'


    def requestLogin(self):
 
        ############ 发送get请求, 获取post所需数据 ##########
        url = "https://u.njtech.edu.cn/cas/login?service=https://u.njtech.edu.cn/oauth2/authorize?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code&state=njtech&s=f682b396da8eb53db80bb072f5745232"
        useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"
        get_head  = {'User-Agent':            useragent}
        resp = get(url=url, headers=get_head).text

        lt        = search('lt\" value=\"(.*?)\"',        resp).groups()[0]
        exe       = search('execution\" value=\"(.*?)\"', resp).groups()[0]
        js        = search('jsessionid=(.*?)\">',         resp).groups()[0]
        cookies   = F"JSESSIONID={js}; insert_cookie=97324480"

        ############# 发送post请求, 完成认证 ################
        post_urls = F"{url_bases};jsessionid={js}?service={url_query}"
        post_head = {
            "Host": "u.njtech.edu.cn",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://u.njtech.edu.cn",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": cookies,
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": useragent,
            "Referer": url_query,
            "Content-Length": "207",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        }
        post_data = {
            "username":    self.username,
            "password":    self.password,
            "channelshow": self.broadban,
            "channel":     self.bandabbr,
            "lt":                     lt,
            "execution":             exe,
            "_eventId":         "submit",
            "login":               "登录"}
        post(url=post_urls, headers=post_head, data=post_data)


    def toConnect(self):
        threads = []
        threads.append(threading.Thread(target=self.requestLogin))
        threads.append(threading.Thread(target=self.connectionProcessBar))
        for t in threads: t.start()
        for t in threads: t.join()
 
 
    def connectionProcessBar(self):
        for i in range(11):
            print('\r\t正在连接：{0}  {1}%'.format('▉▉'*i, (i*10)), end='');sleep(0.05)
 
 
if __name__ == '__main__':
 
    login = AutoLogin()
    login.toConnect()
 