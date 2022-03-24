import json
from requests import get
from PyQt6.QtCore import QThread, pyqtSignal
from constants import VERSION_CODE, VERSION_NAME
from constants import USERAGENT, CHECK_URL


def checkUpdate():
    """ 返回最新的版本名，版本号 """
    version_name = VERSION_NAME
    version_code = VERSION_CODE

    get_header = {'User-Agent': USERAGENT}
    
    try:
        get_json = get(url=CHECK_URL, headers=get_header).text
        jsondata = json.loads(get_json)
        
        curVerCode = jsondata["windows"]["versionCode"]
        curVerName = jsondata["windows"]["versionName"]

        if (version_code < curVerCode):
            version_code = curVerCode
            version_name = curVerName

    except: pass

    if (version_code == VERSION_CODE):
        """ 当前为最新版 """
        version_code = 0

    return version_name, version_code


class BackThread(QThread):
    """ 后台检查版本更新 """
    update_info = pyqtSignal(str, str)

    def run(self):

        version_name, version_code = checkUpdate()
        if (version_code == 0):
            self.update_info.emit(version_name, "确定")
        else:
            self.update_info.emit(version_name, "下载")


if __name__ == '__main__':

    print(checkUpdate())