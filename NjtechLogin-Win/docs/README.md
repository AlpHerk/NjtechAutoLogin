``` —————————————————————— 软件打包命令 ——————————————————————

pyinstaller NjtechAutologin.py -w --clean -i pyqtui\icons\NJtech02.ico --log-level WARN --hidden-import PyQt5.sip --noconfirm -p service -p windo -p windo\ui_init

pyinstaller autologin.py -w --clean -i pyqtui\icons\autologin.ico --log-level WARN --noconfirm -p service

pyi-makespec -w xxx.py

pyinstaller -D xxx.spec

```
 


# **【南工大上网认证 项目开发日志】**  

[🔗CSDN项目地址][CSDN_URL]  



## **项目开发命名规范：**  

- > 1.用户软件压缩包名：大驼峰命名 NjtechAutologin.zip
    2.打包的主程序名称：大驼峰命名 NjtechAutologin.exe
    3.打包的子程序名称：全小写命名 autologin.exe

- > 1.源码运行产生库：config  
    2.软件发布文件夹：dist  
    3.后端服务文件库：service  
    4.软件前端界面UI：window

- > 1.类名：大驼峰    WinLogin()
    2.函数：小驼峰    requestLogin()
    3.变量：小写下划线 post_data 
    4.控件：小写下划线 btn_login



## **软件运行测试日志**

- > 用户登录文件的读写 ✔

- > 修复软件执行路径问题，读写找不到文件 ✔  
    pyinstaller打包：--specpath dir 打包无图标 ❓



## **开发记录**

- 21.10.3晚  
  软件打包遇到无图标问题，以为PS处理了icon图片产生的问题，下载图标制作软件误装全家！
- 21.10.4早
  全家桶弹窗，C盘大清理。无法访问外网，回滚系统，重装驱动。冥思苦想，删除上网认证cookies，问题解决！
- 22.1.23早
  增加检查更新功能


## BootStrap 框架使用
- 使用框架时尽量使用框架样式，少些CSS，保持风格统一
- 行内样式、行内块、块级样式


[CSDN_URL]:https://blog.csdn.net/Alpherkin/article/details/115599094
