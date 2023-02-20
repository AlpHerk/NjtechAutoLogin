package alpherk.njtechlogin.util
import alpherk.njtechlogin.util.MyApp.Companion.context
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.net.wifi.WifiManager
import android.net.wifi.WifiNetworkSuggestion
import android.os.Build
import android.provider.Settings
import android.util.Log
import androidx.annotation.RequiresApi
import okhttp3.OkHttpClient
import okhttp3.Request
import java.net.Inet4Address
import java.net.NetworkInterface
import java.util.concurrent.TimeUnit


object NetUtil {

    private lateinit var wifiManager: WifiManager

    /**
     * 自定义网络 client
     */
    val client: OkHttpClient = OkHttpClient.Builder()
        .connectTimeout(5, TimeUnit.SECONDS)
        .writeTimeout(5, TimeUnit.SECONDS)
        .readTimeout(5, TimeUnit.SECONDS)
        .followRedirects(true)
        .followSslRedirects(true)
        .build()




    /**
     * 从本地获取 IPv4 地址
     */
    @Deprecated("停用")
    fun getIp4fromLocal(): String? {
        try {
            val inter = NetworkInterface.getNetworkInterfaces()
            while (inter.hasMoreElements()) {
                val enumIpAdd = inter.nextElement().inetAddresses
                while (enumIpAdd.hasMoreElements()) {
                    val inetAddress = enumIpAdd.nextElement()
                    if (!inetAddress.isLoopbackAddress && inetAddress is Inet4Address) {
                        Log.d("Herkin", "本机 ip 为：${inetAddress.getHostAddress()}")
                        return inetAddress.getHostAddress()?.toString()
                    }
                }
            }
        } catch (ex: Exception) {
        }
        return null
    }

    /**
     * 从网页获取 IPv4 地址
     */
    fun getIpFormNet(): String? {

        val request1 = Request.Builder().url("http://10.50.255.11")
            .addHeader("Connection", "keep-alive")
            .addHeader("Content-Type", "text/html; charset=gbk")
            .addHeader("Upgrade-Insecure-Requests", "1")
            .addHeader("User-Agent", "Mozilla/5.0 (Linux; U; Android 11; zh-cn; Redmi K20 Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36")
            .addHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
            .addHeader("Accept-Encoding", "gzip, deflate")
            .addHeader("Accept-Language", "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7")
            .addHeader("Host", "10.50.255.11")
            .build()

        val response = client.newCall(request1).execute()
        val respBody = response.body?.string()
        val ip = respBody?.let {
            Regex("v46ip=\'(.*?)\'").find(it)!!.groupValues[1]
        }
        Log.d("HERKIN", "网页获取 ip 为：$ip")
        return ip
    }



    /**
     * 开启 WiFi or 弹出 WiFi 连接面板
     */
    fun setWiFiEnabled(): Boolean {
        wifiManager = context.applicationContext.getSystemService(Context.WIFI_SERVICE) as WifiManager
        return if (!wifiManager.isWifiEnabled) {
            if (Build.VERSION.SDK_INT<=28) {
                wifiManager.isWifiEnabled = true
                true
            } else {
                val intent = Intent(Settings.Panel.ACTION_WIFI)
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                context.startActivity(intent)
                false
            }
        } else true
    }

    fun isWifiEnable(): Boolean {
        wifiManager = context.applicationContext.getSystemService(Context.WIFI_SERVICE) as WifiManager
        return wifiManager.isWifiEnabled
    }

    fun pingNetwork(): Boolean {
        return try {
            client.newCall(Request.Builder().url("https://www.baidu.com").build()).execute()
            true
        } catch (e:java.lang.Exception) {
            Log.d("Herkin", e.toString())
            false
        }
    }

    @Deprecated("暂时停用")
    @RequiresApi(Build.VERSION_CODES.Q)
    fun connectWiFi() {
        // TODO
        val suggestion1 = WifiNetworkSuggestion.Builder()
            .setSsid("Njtech-Home")
            .setIsAppInteractionRequired(true) // Optional (Needs location permission)
            .build()
        val suggestionsList = listOf(suggestion1)
        val wifiManager = context.getSystemService(Context.WIFI_SERVICE) as WifiManager
        val status = wifiManager.addNetworkSuggestions(suggestionsList)

        if (status != WifiManager.STATUS_NETWORK_SUGGESTIONS_SUCCESS) {
            // do error handling here
        }
        // Optional (Wait for post connection receiver to one of your suggestions)
        val intentFilter = IntentFilter(WifiManager.ACTION_WIFI_NETWORK_SUGGESTION_POST_CONNECTION)

        val broadcastReceiver = object : BroadcastReceiver() {
            override fun onReceive(context: Context, intent: Intent) {
                if (!intent.action.equals(WifiManager.ACTION_WIFI_NETWORK_SUGGESTION_POST_CONNECTION)) {
                    return
                }
                // do post connect processing here
            }
        }
        context.registerReceiver(broadcastReceiver, intentFilter)
    }

}