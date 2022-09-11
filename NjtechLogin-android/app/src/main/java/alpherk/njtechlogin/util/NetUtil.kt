package alpherk.njtechlogin.util
import alpherk.njtechlogin.AuthenService
import alpherk.njtechlogin.main.setting.SettingData
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
import java.util.concurrent.TimeUnit
import kotlin.concurrent.thread


object NetUtil {

    private lateinit var wifiManager: WifiManager
    val client: OkHttpClient = OkHttpClient.Builder()
        .connectTimeout(5, TimeUnit.SECONDS)
        .writeTimeout(5, TimeUnit.SECONDS)
        .readTimeout(5, TimeUnit.SECONDS)
        .build()

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
            Log.d("HERKS", e.toString())
            false
        }
    }


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
        // Optional (Wait for post connection broadcast to one of your suggestions)
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