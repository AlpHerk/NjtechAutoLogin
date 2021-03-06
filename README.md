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
2. Windows、Linux、、MacOS、IOS 可配置 python 环境运行脚本进行认证
3. Windows、Android 系统提供相应的软件，[官网下载][WebSite]即可使用
4. Njtech-Home、Njtech 均可认证，认证失败请点击[常见问题](#faq)


-------------------------------

- NjtechLogin-android: 基于 Kotlin 开发的 App 应用 
  > 适用于鸿蒙系统(HarmonyOS) 1.0-3.0，安卓系统 8-12  
  > 适配横屏模式，强烈推荐平板使用 ！！

- NjtechLogin-ios&linux: 基于 Python 开发，pythonista3 运行
  > 此目录下为核心源码，不提供UI界面
  > 适用于IOS平台，下载 pythonista3 配合快捷指令  
  > 需要自行配置快捷指令，后续完善，目前此处仅提供源码  

- NjtechLogin-win-python: 基于 Python、PyQt 开发的 Win 客户端。
  > 有python环境可直接运行 autologin.py  
  > exe 版具有断网重连、开机自启等功能

- NjtechLogin-win-c++: 基于 C++ 语言、Qt 框架 开发的 Win 客户端。  
  > 由于 PyQt 框架开发的客户端体积越来越大，计划利用 Qt 重新开发。  
  > 介时也会重置 Win 客户端版本号，设计更美观丰富的界面，先画饼立flag吧 (●'◡'●)


<br>


## 软件更新日志

<details>
<summary>安卓App更新日志</summary>

V0.0.0 (待修复及待实现)
- [ ] ‌增加账号的自由切换
- [ ] ‌增加快捷键启动服务
- [ ] 增加解锁启动重认证
- [ ] ‌替换透明活动页启动
- [ ] ‌替换全新的动画图标
- [ ] 修复创建页面时地频繁认证
- [ ] 修复平板模式头像显示错误
- [ ] 修复设置Fragment跳转重叠

V1.2.4 (03.14/2022) 
- [x] 适配安卓12(MIUI13闪退问题)

V1.2.1 (01.28/2022)
- [x] ‌优化检查更新地址的解析    

V1.2.0 (12.07/2021)
- [x] ‌增加前台守护服务

V1.1.5 (11.01/2021)
- [x] ‌修复WIFI认证流程及细节
- [x] ‌增加安卓9以下自动连接WIFI特性

V1.1.0 (10.10/2021)
- [x] 优化认证请求处理，提高认证速度
- [x] 修复服务设置数据加载错误

V1.0.0 (09.25/2021)
- [x] ‌实现核心的认证功能
- [x] ‌适配深色与横屏模式

</details>


<details>
<summary>电脑Win版更新日志</summary>

V0.0.0 (待修复及待实现)
- [ ] PyQt写的界面越来越臃肿，计划Qt重写界面
- [ ] 优化开机自启流程，加速软件自启
- [ ] 修复登录窗口阴影缺失
- [ ] 修复单例进程
- [ ] 登录窗口重绘
- [ ] c++重构项目，精简体积
- [ ] 项目重构，版本号重置

V6.1.5 (10.5/2021)
- [x] 美化登录窗口，界面圆角化处理
- [x] 优化启动速度，电脑持续不断网
- [x] 修复异常显示，适配不同分辨率

V6.0.0 (8.30/2021)
- [x] 代码重构，子窗口重写
- [x] 修复图标图片不显示问题

V5.9.0 (6.19/2021)
- [x] 采用双线程，增加登录进度条显示
- [x] 优化登录失败反馈信息，增加重处理进度条

V5.0.0 (6.15/2021)
- [x] 优化请求认证，认证更迅捷
- [x] 增加登录UI，简化登录配置
- [x] 增加联网稳定性，降低认证失败率

</details>


<details>
<summary>IOS认证更新日志</summary>

- [x] 精简python代码(04.11/2021)
- [ ] 创建IOS快捷指令

</details>


<details>
<summary>官方网页维护日志</summary>

- [ ] 补充脚页内容
- [ ] 增加日志更新页内容
- [ ] 增加应用推荐页内容

</details>


<br>


## 常见问题 FAQ <span id="faq"></span>

<details>
<summary>
PC 端，网络认证失败？
</summary>

- ### 认证禁止使用代理，请关闭VPN，游戏加速器等
- 电脑开机优先加载系统组件，认证服务启动较慢，属于正常情况
- 检查开机 WIFI 能否自动连接到 Njtech-Home
- 检查校园网账号是否欠费停机，密码是否正确等
</details>


<details>
<summary>
PC 端，无法打开网页？
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
Android 端，闪退？
</summary>

- 支持安卓8~12版本，过低过高版本可能闪退
- 安卓9具有自动连接wifi等特性，9以上不具有
</details>

