# 南京工业大学 校园网 自动登录认证 (安卓/苹果/电脑) —— NjtechAutoLogin (Android/IOS/Windows Cross-Platform)

<div align="center">

<!-- 简体中文 | [English](./README.en.md) -->

[官网下载地址][WebSite]&emsp;&emsp;[CSDN项目地址][CsdnPrj]&emsp;&emsp;[联系及反馈][CsdnBlog]

<!-- ![Release Download](https://img.shields.io/github/downloads/AlpHerk/NjtechAutoLogin/total) -->
![仓库大小](https://img.shields.io/github/repo-size/AlpHerk/NjtechAutoLogin?color=5DBD88)
[![最新版](https://img.shields.io/github/v/release/AlpHerk/NjtechAutoLogin)][Latest]
[![许可证](https://img.shields.io/github/license/AlpHerk/NjtechAutoLogin?color=F19D70)](LICENSE)
[![星标数](https://img.shields.io/github/stars/AlpHerk/NjtechAutoLogin?color=DCBC76)][Star]

[![CSDN项目](https://img.shields.io/badge/CSDN-项目地址-blue.svg?color=F0AEA9)][CsdnPrj]
[![联系反馈](https://img.shields.io/badge/联系反馈-昂!无白Herk-blue.svg?color=E18774)][CsdnBlog]

[![官网下载](https://img.shields.io/badge/官网-下载地址-blue.svg?color=00ADEE)][WebSite]

![演示图，能进来都不错了，还想看图 (●'◡'●)](https://github.com/AlpHerk/NjtechAutoLogin/blob/Windows/docs/images/homepage.jpg)

[Star]:     https://github.com/AlpHerk/NjtechAutoLogin/stargazers
[Latest]:   https://github.com/AlpHerk/NjtechAutoLogin/releases/latest
[WebSite]:  https://alpherk.github.io/NjtechAutoLogin/
[CsdnBlog]: https://blog.csdn.net/Alpherkin
[CsdnPrj]:  https://blog.csdn.net/Alpherkin/article/details/120580798
[HomePage]: https://github.com/AlpHerk/NjtechAutoLogin/blob/Windows/docs/images/homepage.jpg

</div><br>


## 本项目支持 Android/IOS/Windows 多平台认证

1. 仓库下设 NjtechLogin-* 等多个子目录，分别对应不同平台和系统
2. Windows、Linux、IOS 等可配置 python 环境运行脚本进行认证
3. Windows、Android 系统提供相应的软件，[点击下载][WebSite]即可使用
4. Njtech-Home、Njtech 均可认证，认证失败请点击[获取帮助](#faq)


-------------------------------

- NjtechLogin-App: 基于 Kotlin 开发的安卓App  
  > 安卓App，适用于鸿蒙系统  
  > 强烈推荐平板使用 ！！

- NjtechLogin-IOS: 基于 Python 开发，pythonista3 运行
  > 适用于IOS平台，下载 pythonista3 配合快捷指令  
  > 需要自行配置快捷指令，后续完善，目前此处仅提供源码

- NjtechLogin-Win-Python: 基于 Python、PyQt 开发的 Win 客户端。
  > 有python环境可直接运行 autologin.py  
  > exe 版具有断网重连、开机自启等功能

- NjtechLogin-Win-C++: 基于 C++ 语言、Qt 框架 开发的 Win 客户端。  
  > 由于 PyQt 框架开发的客户端体积越来越大，计划利用 Qt 重新开发。  
  > 介时也会重置 Win 客户端版本号，设计更美观丰富的界面，先画饼立flag吧 (●'◡'●)


<br>


## 项目维护日志

<details>
<summary>安卓App维护日志</summary>

- [x] ‌核心的认证功能(V1.0.0-09.25)
- [x] ‌深色与横屏模式(V1.0.0-10.08)
- [x] 采用高效的请求处理(V1.1.0-10.10)
- [x] 修复服务设置数据加载错误
- [x] ‌增加前台守护服务(V1.2.0-12.07)
- [x] ‌检查更新地址的解析(V1.2.1-01.28)    
- [x] 适配安卓12(MIUI13闪退 V1.2.4-03.14) 
- [ ] ‌增加账号的自由切换
- [ ] ‌增加快捷键启动服务
- [ ] ‌绘制全新的动画图标
- [ ] ‌设置透明活动页启动
- [ ] 修复‌解锁启动重认证
- [ ] 修复创建页面时地频繁认证
- [ ] 修复平板模式头像显示错误
- [ ] 修复设置Fragment跳转重叠
</details>


<details>
<summary>电脑Win版维护日志</summary>

- [x] 登录窗口重绘
- [ ] 修复登录窗口阴影缺失
- [ ] 修复单例进程
- [ ] c++重构项目，精简体积
- [ ] 项目重构，版本号重置
</details>


<details>
<summary>IOS认证维护日志</summary>

- [ ] 核心python代码(21.08.31)
- [ ] 创建快捷指令
</details>


<details>
<summary>官方网页维护日志</summary>

- [ ] 补充脚页内容
</details>


<br>


## 常见问题 FAQ <span id="faq"></span>

<details>
<summary>
Windows 端，网络认证失败？
</summary>

- ### 认证禁止使用代理，请关闭VPN，游戏加速器等
- 检查开机 WIFI 能否自动连接到 Njtech-Home
- 检查校园网账号是否欠费停机，密码是否正确等
</details>


<details>
<summary>
Windows 端，无法打开网页？
</summary>

- ### 检查IP是否有效，重置网络，获取有效IP
- 检查电脑网线接口、网卡驱动是否正常
</details>


<details>
<summary>
Android 端，认证失败？
</summary>

- ### 关闭VPN代理，关闭游戏加速器等 
- 检查账号是否欠费停机，密码是否正确
- 检查手机是否连接到 Njtech-Home
</details>


<details>
<summary>
安卓 App，闪退？
</summary>

- 支持安卓9~12版本，过低过高版本可能闪退
- 安卓9具有自动连接wifi等特性，9以上不具有
</details>

