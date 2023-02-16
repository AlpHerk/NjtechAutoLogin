package alpherk.njtechlogin.broadcast

import alpherk.njtechlogin.AuthenService
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
import kotlin.concurrent.thread

class ScreenReceiver: BroadcastReceiver() {
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onReceive(context: Context, intent: Intent) {

        val action = intent.action
        if (action == Intent.ACTION_SCREEN_ON) {
//            thread {
//                if (NetUtil.isWifiEnable() && !NetUtil.pingNetwork()) {
//                    context.startService(Intent(context, AuthenService::class.java))
//                    Log.d("HERKS", "屏幕解锁，WiFi无网")
//                } else {
//                    Log.d("HERKS", "屏幕解锁，网络连通")
//
//                }
//            }
            scope.launch {
                launch(Dispatchers.IO) {
                    if (NetUtil.isWifiEnable() && !NetUtil.pingNetwork()) {
                        context.startService(Intent(context, AuthenService::class.java))
                        Log.d("HERKS", "屏幕解锁，WiFi无网")
                        showToast("WiFi无网，自动认证中")
                    } else {
                        Log.d("HERKS", "屏幕解锁，网络连通")
                    }
                }
            }
        }
    }

}
