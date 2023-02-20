package alpherk.njtechlogin.receiver

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.net.wifi.WifiManager
import android.util.Log


class NetReceiver: BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {

        if (intent.action == WifiManager.NETWORK_STATE_CHANGED_ACTION) {
            Log.d("HERKIN", "网络变化")
            // val wifiManager = context.applicationContext.getSystemService(Context.WIFI_SERVICE) as WifiManager
            val wifiState = intent.getIntExtra(WifiManager.EXTRA_WIFI_STATE, 0)
            Log.e("HERKIN", wifiState.toString())
        }

    }

}









