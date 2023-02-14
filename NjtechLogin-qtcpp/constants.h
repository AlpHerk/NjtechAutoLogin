#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <QObject>
#include <QString>
#include <QUrl>


/// 用户数据 软件设置: login_data.ini 数据名称块
const QString DATA_WARN1  = "<注意事项> 此配置文件请勿修改";
const QString DATA_WARN2  = "<注意事项> 否则需重新输入密码";
const QString DATA_PART1  = "USERINFO";
const QString DATA_PART2  = "WORKINFO";

const QString LOGIN_KEY1  = "UserName";    // 学号
const QString LOGIN_KEY2  = "PassWord";    // 密码
const QString LOGIN_KEY3  = "NetCorpCN";   // 宽带中文名
const QString LOGIN_KEY4  = "NetCorpEN";   // 宽带英文名
const QString LOGIN_KEY5  = "NetCorpCode"; // 宽带运营商

const QString SETTING_KEY1= "ReconnectTime";
const QString SETTING_KEY2= "AutoRun";
const QString SETTING_KEY3= "ShowLoginPop";


/// 程序信息
const int     VER_CODE = 110;
const QString VER_NAME = "V 1.1.0";
const QString SOFTNAME = "NjtechAutoLogin";
const QString AUTHOR   = "AlpHerk";

const QString RUNPATH  = "\\HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run";

const char USERAGENT[] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47";
//const char LOGIN_STR[] = "https://u.njtech.edu.cn/cas/login?service=https://u.njtech.edu.cn/oauth2/authorize?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code&state=njtech&s=f682b396da8eb53db80bb072f5745232";
const char LOGIN_STR[] = "http://10.50.255.11";
const QString LOGIN_URL1 = "http://10.50.255.11:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.50.255.11&iTermType=1&mac=00-00-00-00-00-00&ip=";
const QString LOGIN_URL3 = "&enAdvert=0&queryACIP=0&jsVersion=2.4.3&loginMethod=1";

const QString LOGOUT_URL1 = "http://10.50.255.11:801/eportal/?c=ACSetting&a=Logout&wlanuserip=";
const QString LOGOUT_URL3 = "&wlanacip=10.50.255.1&wlanacname=me60&port=&hostname=10.50.255.11&iTermType=1&session=&queryACIP=0&mac=00-00-00-00-00-00&jsVersion=2.4.3";

/// 程序运行依赖数据
const QString USERAGEN = USERAGENT;
const QString VER_Name = QString::number(VER_CODE);

const QString timeForm = "[yy-MM-dd hh:mm:ss] ";
const QString FAILSTR = "加载失败啦，请稍后重试 ...";
const QString ARG_HIDE = "--hide"; //开机自启的运行参数


/// 本项目的相关链接
const QUrl LOGIN_URL   = QUrl(LOGIN_STR);                                           // 认证服务请求地址
const QUrl LOGOT_URL   = QUrl("https://i.njtech.edu.cn/index.php/njtech/logout");   // 退出登录地址
const QUrl CHECK_URL   = QUrl("https://api.github.com/repos/AlpHerk/NjtechAutoLogin/releases/latest");

const QUrl WEB_URL     = QUrl("https://alpherk.github.io/NjtechAutoLogin/");        // 本软件官方网站链接
const QUrl LICENSE_URL = QUrl("https://gitee.com/Alpherk/NjtechAutoLogin/raw/main/LICENSE");
const QUrl MANUL_URL   = QUrl("https://alpherk.github.io/NjtechAutoLogin/prjinfo/usr_manual.md");
const QUrl NOICE_URL   = QUrl("https://alpherk.github.io/NjtechAutoLogin/prjinfo/notice_msg.md");
const QUrl UPDATE_LOG  = QUrl("https://alpherk.github.io/NjtechAutoLogin/prjinfo/update_log.md");
const QUrl USR_AGREEM  = QUrl("https://alpherk.github.io/NjtechAutoLogin/pages/terms.html");
const QUrl PRIV_POLIC  = QUrl("https://alpherk.github.io/NjtechAutoLogin/pages/privacy_policy.html");
const QUrl GITHUB_PRJ  = QUrl("https://github.com/AlpHerk/NjtechAutoLogin");
const QUrl CSDN_URL    = QUrl("https://blog.csdn.net/Alpherkin");                   // 开发者的CSDN博客地址
const QUrl CSDNPRJ_URL = QUrl("https://blog.csdn.net/Alpherkin/article/details/115599094");
const QUrl FEEDBACK    = QUrl("https://support.qq.com/product/424068");             // 产品的反馈地址



#endif  // CONSTANTS_H
