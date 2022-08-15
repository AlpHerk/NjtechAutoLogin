## 南京工业大学 校园网 自动登录认证 (安卓/苹果/电脑)
## NjtechAutoLogin (Android/IOS/Windows Cross-Platform)
 


## 本项目支持 Android/IOS/Windows 多平台认证

----------------------------------------

1. 本仓库下设 NjtechLogin-* 等多个子目录，分别对应不同平台和系统
2. Linux、MacOS、IOS 可配置 python 环境，运行通用脚本进行认证
3. Linux、MacOS 如需打包软件，可自行下载仓库 Qt 源码并进行编译
4. Android、Windows 系统提供相应的软件，[官网下载][WebSite] 即可使用
5. Njtech-Home、Njtech 均可认证，认证失败请查看 [常见问题](#faq)


 

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

- NjtechLogin-win-c++: 基于 C++ 语言、Qt 框架 开发的跨平台客户端。  
  > 由于 PyQt 框架开发的客户端体积越来越大，计划利用 Qt 重新开发。  
  > 介时也会重置 Win 客户端版本号，设计更美观丰富的界面，先画饼立flag吧 (●'◡'●)

 

 

## 常见问题 FAQ <span id="faq"></span>

----------------------------------------

 
### PC 端，网络认证失败？

- ### 认证禁止使用代理，请关闭VPN，游戏加速器等
- 电脑开机优先加载系统组件，认证服务启动较慢，属于正常情况
- 检查开机 WIFI 能否自动连接到 Njtech-Home
- 检查校园网账号是否欠费停机，密码是否正确等
</details>



### PC 端，无法打开网页？

- ### 检查IP是否有效，重置网络，获取有效IP
- 检查电脑网线接口、网卡驱动是否正常

### Android 端，认证失败？
 

- ### 关闭VPN代理，关闭游戏加速器等 
- 检查账号是否欠费停机，密码是否正确
- 检查手机是否连接到 Njtech-Home
 


 
### Android 端，闪退？
 
- 支持安卓8~12版本，过低过高版本可能闪退
- 安卓9具有自动连接wifi等特性，9以上不具有
 

