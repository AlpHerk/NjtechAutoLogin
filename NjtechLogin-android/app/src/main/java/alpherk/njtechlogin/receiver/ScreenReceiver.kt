package alpherk.njtechlogin.receiver

import alpherk.njtechlogin.service.AuthenService
import alpherk.njtechlogin.util.NetUtil
import alpherk.njtechlogin.util.showToast
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch

class ScreenReceiver: BroadcastReceiver() {
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onReceive(context: Context, intent: Intent) {

        val action = intent.action
        if (action == Intent.ACTION_SCREEN_ON) {

            scope.launch {
                launch(Dispatchers.IO) {
                    if (NetUtil.isWifiEnable() && !NetUtil.pingNetwork()) {
                        context.startService(Intent(context, AuthenService::class.java))
                        Log.d("Herkin", "屏幕解锁，WiFi无网")
                        showToast("自动认证，正在接入互联网")
                    } else {
                        Log.d("Herkin", "屏幕解锁，网络连通")
                    }
                }
            }
        }

    }

}
