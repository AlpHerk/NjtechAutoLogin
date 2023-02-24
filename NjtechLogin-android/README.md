## 基于 Kotlin 开发的安卓App  

> 安卓App，也适用于鸿蒙系统  
> 强烈推荐平板使用 ！！



## 开发问题处理

1. 网络请求处理明文请求 (http://)

在AndroidManifest.xml中添加

```
<application
      ......
      android:usesCleartextTraffic="true"> 
```


2. 通知隐藏状态栏的图标 [链接](
https://stackoverflow.com/questions/11373786/how-to-create-a-notification-without-icon-in-the-statusbar-or-simply-hide-it)

``` kotlin
val noteChannel = NotificationChannel(CHANNEL_ID, CHANNEL_NAME, NotificationManager.IMPORTANCE_UNSPECIFIED)
```
IMPORTANCE_UNSPECIFIED 即可实现