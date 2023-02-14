
## 问题记录
> connect(manager, &QNetworkAccessManager::finished, this, &AutoLogin::authBack);
> connect(manager, SIGNAL(finished(QNetworkReply*)), &loop, SLOT(quit()));
> 同步与异步冲突，不能同时设置。

> request.setHeader(QNetworkRequest::ContentTypeHeader, "text/html;charset=UTF-8");
> 很重要


> 类成员静态变量，需要先在类外部赋值分配内存 [参考链接][1]




[1]:https://blog.csdn.net/qq_37375427/article/details/78747636