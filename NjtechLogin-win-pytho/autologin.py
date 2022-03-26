from configparser import ConfigParser
from os.path import dirname, realpath
from re import search
from sys import argv
from threading import Thread
from time import sleep, time

from requests import get, post

from service import utils
from service.constants import *
from service.utils import Toast

################## 南工大自动登录 ####################

class AutoLogin:

    def __init__(self):
        try: self.__getLoginData()
        except: utils.saveLogFile()

    def __getLoginData(self):
        self.info = {}
        self.config = ConfigParser()
        self.config.read(dirname(realpath(argv[0])) + LOGINFILE_PATH, encoding='utf-8')
        self.info['cnt'] = int(self.config[LOGIN_PART_2][LOGIN_DATA_5].strip())
        self.info['usr'] = self.config[LOGIN_PART_1][LOGIN_DATA_1].strip()
        self.info['pwd'] = self.config[LOGIN_PART_1][LOGIN_DATA_2].strip()
        self.info['shw'] = self.config[LOGIN_PART_1][LOGIN_DATA_3].strip()
        if   self.info['shw'] == '中国移动':   self.info['nel'] = '@cmcc'
        elif self.info['shw'] == '中国电信':   self.info['nel'] = '@telecom'

    def __requestLogin(self):
        ############ 发送get请求, 获取post所需数据 ##########
        resp = get(url=LOGIN_URL, headers=HEADERS)
        lt   = search('lt\" value=\"(.*?)\"',        resp.text).groups()[0]
        exe  = search('execution\" value=\"(.*?)\"', resp.text).groups()[0]
        ############# 发送post请求, 完成认证 ################
        form = {
            "username":    self.info['usr'],
            "password":    self.info['pwd'],
            "channelshow": self.info['shw'],
            "channel":     self.info['nel'],
            "lt":                        lt,
            "execution":                exe,
            "_eventId":            "submit",
            "login":                 "登录"}
        post(url=LOGIN_URL, headers=HEADERS, data=form, cookies=resp.cookies)

    def __loginThread(self):
        threads = []
        threads.append(Thread(target=self.__requestLogin))
        threads.append(Thread(target=Toast.Logining))
        for t in threads: t.start()
        for t in threads: t.join()
        return Toast.connectInfo()

    def toConnect(self):
        for i in range(11):
            if self.__loginThread(): break
        if i >= 10: Toast.failed()

    def intervalConnect(self):
        while self.info['cnt'] > -1:
            if not utils.isConnected:
                self.toConnect()
            print(F"运行中, 间隔{self.info['cnt']}s检测")
            sleep(self.info['cnt'])
        print("重连间隔时间 < 0, 程序退出")


if __name__ == '__main__':

    start = time()

    login = AutoLogin()
    login.toConnect()

    end = time()

    Toast.success(end-start)
    
    login.intervalConnect()




