from time import sleep, time
from subprocess import call
from traceback import print_exc
from webbrowser import open_new_tab
from os import getcwd, makedirs, remove, path
from constants import CSDN_PROJECT_URL, LOGINFILE_DIR, LOGINFILE_PATH, WORK_LOG_PATH


def jumpMyCSDN():
    open_new_tab(CSDN_PROJECT_URL)


def mkConfigDir():
    folder = getcwd() + LOGINFILE_DIR
    if not path.exists(folder):
        makedirs(folder)
        return "配置文件夹创建成功"
    else:
        return "配置文件夹已经存在"


def mvConfigFile():
    file = getcwd() + LOGINFILE_PATH
    if path.exists(file):
        remove(file)
        return "已删除错误配置文件"
    else:
        return "登录配置文件不存在"


def saveLogFile():
    log_path = getcwd() + WORK_LOG_PATH
    print_exc(file = open(log_path,'w+'))
    return "日志保存成功"


def isConnected():
    r = call('ping www.baidu.com -n 1', creationflags=0x08000000)
    return True if r==0 else False


def takeTime(func):
    """ 装饰器: 计算函数运行耗时"""
    def decorated(*args):
        startime = time()
        func(*args)
        endtime  = time()
        taketime = round(endtime - startime, 2)
        print(f"--耗时: {taketime} s\n")
        return func
    return decorated


class Toast():
    """ 显示程序运行相关信 toast 信息 """

    def connectInfo():
        r = call('ping www.baidu.com -n 1', creationflags=0x08000000)
        return True if r==0 else False

    def success(spendtime):
        print('\n\n\n  >>> 恭喜您 ，用时%.2f秒 完成认证 ψ(｀∇´)ψ  '%spendtime);sleep(0.5)
        print('\n  >>> 我是 无白Herk ，感谢您的使用 ~\n' )                    ;sleep(0.5)

    def failed():
        print('\n\n  >>>【多次连接失败, 请确认】：                      '  );sleep(0.5)
        print('\n  >>> 1.电脑已连接 WiFi (建议 Njtech-home 勾选自动连接)'  );sleep(0.5)
        print('\n  >>> 2.学号密码正正确，查看目录 Config\config_info.ini'  );sleep(0.5)
        print('\n  >>> 3.以上方法无法解决请联系 CSDN: AlpHerkin\n'        );sleep(600)

    def Logining():
        for i in range(11):
            print('\r\t正在连接：{0}  {1}%'.format('▉▉'*i, (i*10)), end='');sleep(0.05)

    def reConnect(i):
        print('\r\t＞﹏＜ 出错啦 ~ 正在拼命重连中 ~   第{0}次重连 ~ '.format(i+1))

    def Error():
        print("发生未知错误！")