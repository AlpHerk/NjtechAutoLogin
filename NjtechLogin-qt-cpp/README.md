
## 问题记录
> connect(manager, &QNetworkAccessManager::finished, this, &AutoLogin::authBack);
> connect(manager, SIGNAL(finished(QNetworkReply*)), &loop, SLOT(quit()));
> 同步与异步冲突，不能同时设置。

> request.setHeader(QNetworkRequest::ContentTypeHeader, "text/html;charset=UTF-8");
> 很重要

