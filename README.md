<div align="center">

# 南京工业大学 校园网 自动登录 认证服务

</div>

<div align="center">

##  安卓 | Android &emsp;&emsp; 鸿蒙 | Harmony &emsp;&emsp; 苹果 | IOS

## Windows &emsp;&emsp; cross-platform &emsp;&emsp;&ensp; Linux 

</div>




<div align="center">

<!-- 简体中文 | [English](./README.en.md) -->

[官网下载地址][WebSite]&emsp;&emsp;[CSDN项目地址][CsdnPrj]&emsp;&emsp;[联系及反馈][CsdnBlog]

<!-- ![Release Download](https://img.shields.io/github/downloads/AlpHerk/NjtechAutoLogin/total) -->
![仓库大小](https://img.shields.io/github/repo-size/AlpHerk/NjtechAutoLogin?color=5DBD88)
[![最新版](https://img.shields.io/github/v/release/AlpHerk/NjtechAutoLogin)][Latest]
[![许可证](https://img.shields.io/github/license/AlpHerk/NjtechAutoLogin?color=F19D70)](LICENSE)
[![星标数](https://img.shields.io/github/stars/AlpHerk/NjtechAutoLogin?color=DCBC76)][Star]

[![CSDN项目](https://img.shields.io/badge/CSDN-项目地址-blue.svg?color=F0AEA9)][CsdnPrj]
[![联系反馈](https://img.shields.io/badge/联系反馈-无白Herk-blue.svg?color=E18774)][CsdnBlog]

[![官网下载](https://img.shields.io/badge/官网-下载地址-blue.svg?color=00ADEE)][WebSite]

![(●'◡'●)](https://github.com/AlpHerk/NjtechAutoLogin/blob/Windows/docs/images/homepage.jpg)


[Star]:     https://github.com/AlpHerk/NjtechAutoLogin/stargazers
[Latest]:   https://github.com/AlpHerk/NjtechAutoLogin/releases/latest
[WebSite]:  https://alpherk.github.io/NjtechAutoLogin/
[CsdnBlog]: https://blog.csdn.net/Alpherkin
[CsdnPrj]:  https://blog.csdn.net/Alpherkin/article/details/120580798
[HomePage]: https://github.com/AlpHerk/NjtechAutoLogin/blob/Windows/docs/images/homepage.jpg
[IOSQuick]: https://www.icloud.com/shortcuts/ecf46479c1a94404b23925cdc533e5ef

</div>
<br><br>



## 本项目支持 Android/IOS/Windows 多平台认证


本项目发布了 Windows 软件、安卓 apk、IOS 快捷指令，[官网下载][WebSite] 即可使用

<br>

## 使用注意事项

1. 目前的 Windows、Android 软件、IOS 快捷指令只适配了新版的 Njtech-Home 认证，暂 不支持 Njtech 的认证。建议使用 Njtech 时，勾选无感认证，绑定设备，则不用再反复验证密码。

2. Windows 软件如不能正常自启，请重新勾选软件内的 `开机认证`,

3. Android 软件长按图标即可进行认证。屏幕解锁时若无网，则会自动唤醒认证。

4. IOS 快捷指令：运营商，中国移动填 `@cmcc`，中国电信填 `@telecom`。WiFi 请开启自动加入。

5. 其他认证失败的情况，请查看 [常见问题](#faq)

<br>

## 仓库目录说明

> NjtechLogin-android: 基于 Kotlin 语言开发的 App 应用   

- 适用于鸿蒙系统(HarmonyOS) 1.0+，安卓系统 8+
- 适配横屏模式，强烈推荐平板使用 ！！


> ~~NjtechLogin-pyqt: 基于 PyQt 框架 开发的桌面软件(已弃用)~~

- 此目录的项目为前期桌面端 UI 的解决方案，现在已弃用
- 因此，桌面端请直接见 qtcpp 目录的解决方案


> NjtechLogin-python: 基于 Python 语言开发的脚本

- 此目录下为校园网认证的纯 python 代码，无UI界面
- 可运行于 IOS 平台的 pythonista3 软件


> NjtechLogin-qtcpp: 基于 C++ 语言、Qt 框架 开发的跨平台客户端

- 由于 PyQt 框架开发的客户端体积大，故利用 Qt 重新开发 
- Windows，Linux，MacOS 平台也可编译使用



<br>

----------------------------------------

<br>


## 软件更新日志


<details>
<summary>电脑Win版更新日志 (2023.2.18)</summary>

v1.1.2 (2023.2.18)
- [x] 修复更新软件后的自启注册表
- [x] 修复软件运行时的单例模式
- [x] 使用最新网络认证通道 
- [x] 增加了一个注销认证按钮
- [x] 修复部分按钮颜色显示
- [x] 优化登录日志输出显示


v1.0.0 (2022.8.10 最新重置版)
- [x] 采用 Qt/C++ 编写，提高软件响应速度
- [x] 重构了桌面版项目，重置版本号，精简体积 
- [x] 重新设计了软件，美化界面从我做起
- [x] 优化了自启流程，加速开机联网速度
- [x] 总之，这次推倒重做的版本绝对快


v0.6.1.5 (2021.10.5 以下为旧版)
- [x] 美化登录窗口，界面圆角化处理
- [x] 优化启动速度，电脑持续不断网
- [x] 修复异常显示，适配不同分辨率

v0.6.0.0 (2021.8.30)
- [x] 代码重构，子窗口重写
- [x] 修复图标图片不显示问题

v0.5.9.0 (2021.6.19)
- [x] 采用双线程，增加登录进度条显示
- [x] 优化登录失败反馈信息，增加重处理进度条

v0.5.0.0 (2021.6.15)
- [x] 优化请求认证，认证更迅捷
- [x] 增加登录UI，简化登录配置
- [x] 增加联网稳定性，降低认证失败率

</details>


<details>
<summary>安卓App更新日志 (2023.2.18)</summary>


v0.0.0 (待修复及待实现)
- [ ] ‌增加账号的自由切换
- [ ] ‌替换全新的动画图标
- [ ] 修复平板模式头像显示错误
- [ ] 修复设置Fragment跳转重叠

v1.3.2 (2023.2.18)
- [x] 修复 shortcut 功能，桌面长按图标一键认证
- [x] 使用最新网络认证通道，‌增加快捷键启动服务
- [x] 右上角菜单增加了注销认证的功能
- [x] 调整网络守护服务的运行逻辑 
- [x] 简化了认证过程中的 toast 提示 

v1.2.4 (2022.03.14) 
- [x] 修复创建页面时地频繁认证
- [x] 适配安卓12(MIUI13闪退问题)
- [x] 增加解锁启动重认证

v1.2.1 (2022.01.28)
- [x] ‌优化检查更新地址的解析    

v1.2.0 (2021.12.07)
- [x] ‌增加前台守护服务

v1.1.5 (2021.11.01)
- [x] ‌修复WIFI认证流程及细节
- [x] ‌增加安卓9以下自动连接WIFI特性

v1.1.0 (2021.10.10)
- [x] 优化认证请求处理，提高认证速度
- [x] 修复服务设置数据加载错误

v1.0.0 (2021.09.25)
- [x] ‌实现核心的认证功能
- [x] ‌适配深色与横屏模式

</details>




<details>
<summary>IOS认证更新日志 (2023.2.21)</summary>

2023.2.21
- [x] 适配新版认证页的快捷指令 

2021.04.11
- [x] 创建 IOS 快捷指令
- [x] 精简python代码

</details>


<details>
<summary>官方网页维护日志</summary>

- [x] 补充脚页内容
- [x] 增加日志更新页内容
- [x] 增加应用推荐页内容

</details>


<br><br>


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

- 支持安卓8以上版本，过低过高版本可能闪退
- 安卓9具有自动连接wifi等特性，9以上不具有
</details>

## 项目 API 处理说明
- 软件对 GitHub release 页的链接进行检查更新
- 检查更新时提取 release downurl 内的数字作为版本码