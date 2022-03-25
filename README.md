# 南京工业大学 校园网 自动登录认证 (安卓/苹果/电脑 多平台适用)
# NjtechAutoLogin ( Android/IOS/Windows Cross-Platform )

> [官网下载地址][1]&emsp;&emsp;[CSDN项目地址][2]&emsp;&emsp;[联系及反馈][3]

![软件演示图][0]


## 本项目支持 Android/IOS/Windows 三个平台的上网认证
- 支持 Njtech-Home、Njtech 多设备平台的校园网认证

- NjtechLogin-App: 基于 Kotlin 开发的安卓App
  > 安卓App，适用于鸿蒙系统  
  > 强烈推荐平板使用 ！！

- NjtechLogin-Win: 基于 Python PyQt 开发的PC客户端。
  > 有python环境可直接运行 autologin.py  
  > exe版具有断网重连、开机自启等功能

- NjtechLogin-IOS
  > 适用于IOS平台，下载 pythonista3 配合快捷指令
  > 需要自行配置快捷指令，后续完善，目前此处仅提供源码


[0]: https://github.com/AlpHerk/NjtechAutoLogin/blob/Windows/docs/images/homepage.jpg
[1]: https://alpherk.github.io/NjtechAutoLogin/
[2]: https://blog.csdn.net/Alpherkin/article/details/120580798
[3]: https://blog.csdn.net/Alpherkin
[4]: https://github.com/AlpHerk/NjtechAutoLogin/blob/WebPage/images/homepage.jpg


## 安卓App维护计划：
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


## 电脑Win版维护计划：
- [x] 登录窗口重绘
- [ ] 修复登录窗口阴影缺失
- [ ] 修复单例进程
- [ ] c++重构项目，精简体积
- [ ] 项目重构，版本号重置


## IOS认证维护计划：
- [ ] 核心python代码(21.08.31)
- [ ] 创建快捷指令


## 官方网页维护计划：
- [ ] 补充脚页内容

## FAQ
认证失败：关闭VPN代理
