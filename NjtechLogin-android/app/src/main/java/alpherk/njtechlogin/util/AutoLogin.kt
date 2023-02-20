package alpherk.njtechlogin.util
import android.util.Log
import okhttp3.FormBody
import okhttp3.Request
import java.net.Inet4Address
import java.net.NetworkInterface

object AutoLogin {



    /**
     * 发送校园网认证请求
     */
    private fun loginNet(UserData: List<String>): String? {
        val (username, password, netCompany) = UserData

        val ipLocal = NetUtil.getIpFormNet()

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

        return try {
            val resp = NetUtil.client.newCall(request).execute()
            resp.request.url.toString()
        } catch (ex: Exception) {
            Log.d("Herkin", "认证失败：无法接入学校内网")
            null
        }

    }

    fun askLogin(UserData: List<String>): Pair<Boolean, String> {
        val res = loginNet(UserData)

        if (res != null) {
            return if (!res.contains("ACLogOut")) {
                Log.d("Herkin", "认证结果: $res")
                Pair(true,  "✅ 认证成功，开始冲浪 ~")
            }
            else if (res.contains("ACLogOut=1")) {
                Pair(true,  "🟧 认证已注销，网络断开")
            }
            else if (res.contains("ACLogOut=2")) {
                Pair(true,  "🟧 注销失败，请勿反复注销")
            }
            else if (res.contains("ACLogOut=5&RetCode=1&ErrorMsg=bGRhcCBhdXRoIGVycm9y")) {
                Pair(false, "🔴 账号或密码错误（ldap校验）")
            }
            else if (res.contains("ACLogOut=5&RetCode=1&ErrorMsg=dXNlcmlkIGVycm9yMQ"  )) {
                Pair(false, "🔴 请选择正确的运营商，移动/电信！")
            }
            else if (res.contains("ACLogOut=5&RetCode=1")) {
                Pair(true,  "🔴️ AC认证失败")
            }
            else if (res.contains("ACLogOut=5&RetCode=2")) {
                Pair(true,  "ℹ️ 终端 IP 已经在线")
            }
            else {
                Log.d("Herkin", "认证结果: 未知 $res")
                Pair(false,  "🔴 认证失败，未知重定向链接")
            }
        } else {
            return Pair(false, "ℹ️ 请用 WiFi 数据认证")
        }
    }

}

/**
 * 认证注销类
 */
object LogoutNet {

    /** 从本地获取 IPv4 地址
     *
     */
    private fun getIp4fromLocal(): String? {
        try {
            val inter = NetworkInterface.getNetworkInterfaces()
            while (inter.hasMoreElements()) {
                val enumIpAdd = inter.nextElement().inetAddresses
                while (enumIpAdd.hasMoreElements()) {
                    val inetAddress = enumIpAdd.nextElement()
                    if (!inetAddress.isLoopbackAddress && inetAddress is Inet4Address) {
                        Log.d("HERKIN", "本机 ip 为：${inetAddress.getHostAddress()}")
                        return inetAddress.getHostAddress()?.toString()
                    }
                }
            }
        } catch (ex: Exception) {
        }
        return null
    }

    /**
     * 发送校园网注销认证请求
     */
    fun logoutNet() {
        try {
            val ipLocal = getIp4fromLocal()
            val urlLogout= "http://10.50.255.11:801/eportal/?c=ACSetting&a=Logout&wlanuserip=$ipLocal&wlanacip=10.50.255.1&wlanacname=me60&port=&hostname=10.50.255.11&iTermType=2&session=&queryACIP=0&mac=00-00-00-00-00-00&jsVersion=2.4.3"
            val requestBody = FormBody.Builder().build()
            val request = Request.Builder().url(urlLogout)
                .addHeader("Cache-Control", "max-age=0")
                .addHeader("Upgrade-Insecure-Requests", "1")
                .addHeader("Content-Type", "application/x-www-form-urlencoded")
                .addHeader("User-Agent", "Mozilla/5.0 (Linux; U; Android 11; zh-cn; Redmi K20 Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36")
                .addHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
                .addHeader("Referer", "http://10.50.255.11/")
                .addHeader("Accept-Encoding", "gzip, deflate")
                .addHeader("Accept-Language", "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7")
                .post(requestBody).build()
            NetUtil.client.newCall(request).execute()
        } catch (ex: Exception) {
            Log.d("HERKIN", "注销失败：无法接入学校内网")
        }

    }

}




@Deprecated("认证返回的重定向连接")
const val temp = """
您已经成功登录。 
You have successfully logged into our system.
http://10.50.255.11:80/3.htm?wlanuserip=10.40.177.167&wlanacname=me60&wlanacip=10.50.255.1&mac=00-00-00-00-00-00&session=&redirect=

注销失败  
Logout failed
http://10.50.255.11/2.htm?wlanuserip=10.40.177.167&wlanacname=me60&wlanacip=10.50.255.1&mac=00-00-00-00-00-00&session=&redirect=&ACLogOut=2

请检查您绑定的运营商账号是否正确
Account does not exist
http://10.50.255.11:80/2.htm?wlanuserip=10.40.177.167&wlanacname=me60&wlanacip=10.50.255.1&mac=00-00-00-00-00-00&session=&redirect=&ACLogOut=5&RetCode=1&ErrorMsg=dXNlcmlkIGVycm9yMQ%3D%3D

账号或密码错误（ldap校验）
http://10.50.255.11:80/2.htm?wlanuserip=10.40.177.167&wlanacname=me60&wlanacip=10.50.255.1&mac=00-00-00-00-00-00&session=&redirect=&ACLogOut=5&RetCode=1&ErrorMsg=bGRhcCBhdXRoIGVycm9y

终端IP已经在线 
IP already online
http://10.50.255.11:80/2.htm?wlanuserip=10.40.177.167&wlanacname=me60&wlanacip=10.50.255.1&mac=00-00-00-00-00-00&session=&redirect=&ACLogOut=5&RetCode=2&ErrorMsg=

AC认证失败
http://10.50.255.11/2.htm?wlanuserip=192.168.94.2&wlanacname=me60&wlanacip=10.50.255.1&mac=00-00-00-00-00-00&session=&redirect=&ACLogOut=3&RetCode=1&ErrorMsg=
"""

@Deprecated("旧的智慧南工认证类")
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
















