package alpherk.njtechlogin.util
import android.util.Log
import okhttp3.FormBody
import okhttp3.Request

object AutoLogin {
    private const val ip = ""
    private const val url_a70htm = "http://10.50.255.11"

    private fun getIP(): String? {
        val request1 = Request.Builder().url(url_a70htm)
            .addHeader("Connection", "keep-alive")
            .addHeader("Content-Type", "text/html; charset=gbk")
            .addHeader("Upgrade-Insecure-Requests", "1")
            .addHeader("User-Agent", "Mozilla/5.0 (Linux; U; Android 11; zh-cn; Redmi K20 Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36")
            .addHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
            .addHeader("Accept-Encoding", "gzip, deflate")
            .addHeader("Accept-Language", "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7")
            .addHeader("Host", "10.50.255.11")
            .build()

        val response = NetUtil.client.newCall(request1).execute()
        val respBody = response.body?.string()

        return respBody?.let { Regex("v46ip=\'(.*?)\'").find(it)!!.groupValues[1] }
    }

    private fun postRequest(UserData: List<String>) {
        val (username, password, netCompany) = UserData
        val ipLocal = getIP()
        val urlLogin = "http://10.50.255.11:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.50.255.11&iTermType=2&wlanuserip=$ipLocal&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip=$ipLocal&enAdvert=0&queryACIP=0&jsVersion=2.4.3&loginMethod=1"
        var channel = ""
        if (netCompany == "1") {
            channel = "@cmcc"
        } else if (netCompany == "2") {
            channel = "@telecom"
        }

        val requestBody = FormBody.Builder()
            .add("DDDDD", ",0,$username$channel")
            .add("upass", password)
            .add("R1", "0")
            .add("R2", "0")
            .add("R3", "0")
            .add("R6", "0")
            .add("para", "00")
            .add("0MKKey", "123456")
            .build()

        val request = Request.Builder().url(urlLogin)
            .addHeader("Cache-Control", "max-age=0")
            .addHeader("Upgrade-Insecure-Requests", "1")
            .addHeader("Content-Type", "application/x-www-form-urlencoded")
            .addHeader("User-Agent", "Mozilla/5.0 (Linux; U; Android 11; zh-cn; Redmi K20 Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36")
            .addHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
            .addHeader("Referer", "http://10.50.255.11/")
            .addHeader("Accept-Encoding", "gzip, deflate")
            .addHeader("Accept-Language", "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7")
            .post(requestBody).build()

        val response = NetUtil.client.newCall(request).execute()
        Log.d("HERKS", "获取ip地址 ")
    }

    fun askLogin(UserData: List<String>): Boolean {
        return try {
            postRequest(UserData)
            NetUtil.pingNetwork()
            true
        } catch (e:Exception) {
            false
        }
    }
}

// @deprecated
object AutoLoginDeprecated {
    private const val hostURL = "https://u.njtech.edu.cn/cas/login"
    private const val param   = "?service=https://u.njtech.edu.cn/oauth2/authorize?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code&state=njtech&s=f682b396da8eb53db80bb072f5745232"
    private const val getsURL = "$hostURL$param"

    private fun getParam(): List<String> {
        val request  = Request.Builder().url(getsURL).build()
        val response = NetUtil.client.newCall(request).execute()
        val respBody = response.body?.string()

        val param1 = "lt\" value=\"(.*?)\""
        val param2 = "execution\" value=\"(.*?)\""
        val param3 = "jsessionid=(.*?)\">"
        val lt  = respBody?.let { Regex(param1).find(it)!!.groupValues[1] }
        val exe = respBody?.let { Regex(param2).find(it)!!.groupValues[1] }
        val js  = respBody?.let { Regex(param3).find(it)!!.groupValues[1] }

        val cookies  = "JSESSIONID=${js}; insert_cookie=67313298"
        val postsURL = "$hostURL;jsessionid=${js}$param"

        return listOf(lt!!, exe!!, cookies, postsURL)
    }

    private fun postRequest(UserData: List<String>) {
        val (username, password, netCompany) = UserData
        val (lt, exe, cookies, postsURL) = getParam()
        var channelshow = "中国移动"
        var channel = "@cmcc"
        if (netCompany == "2") {
            channelshow = "中国电信"
            channel = "@telecom"
        }
        val requestBody = FormBody.Builder()
            .add("username", username)
            .add("password", password)
            .add("channelshow", channelshow)
            .add("channel", channel)
            .add("lt", lt)
            .add("execution", exe)
            .add("_eventId", "submit")
            .add("submit", "登录")
            .build()

        val request = Request.Builder().url(postsURL)
            .addHeader("Host", "u.njtech.edu.cn")
            .addHeader("Connection", "keep-alive")
            .addHeader("Content-Length", "213")
            .addHeader("Cache-Control", "max-age=0")
            .addHeader("Upgrade-Insecure-Requests", "1")
            .addHeader("Origin", "https://u.njtech.edu.cn")
            .addHeader("Content-Type", "application/x-www-form-urlencoded")
            .addHeader("User-Agent", "Mozilla/5.0 (Linux; U; Android 11; zh-cn; Redmi K20 Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36")
            .addHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
            .addHeader("Accept-Encoding", "gzip, deflate, br")
            .addHeader("Accept-Language", "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7")
            .addHeader("Sec-Fetch-Site", "same-origin")
            .addHeader("Sec-Fetch-Mode", "navigate")
            .addHeader("Sec-Fetch-User", "?1")
            .addHeader("Sec-Fetch-Dest", "document")
            .addHeader("Save-Data", "on")
            .addHeader("Referer", getsURL)
            .addHeader("Cookie", cookies)
            .post(requestBody).build()

        NetUtil.client.newCall(request).execute()
    }

    fun askLogin(UserData: List<String>): Boolean {
        return try { postRequest(UserData)
            NetUtil.pingNetwork()
            true
        } catch (e:Exception) {
            false
        }
    }

}
















