package alpherk.njtechlogin.service

import alpherk.njtechlogin.util.LogoutNet
import alpherk.njtechlogin.util.showToast
import android.app.Service
import android.content.Intent
import android.os.IBinder
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch

/**
 * 注销认证服务
 */
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }
    override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {
        scope.launch {
            LogoutNet.logoutNet()
            showToast("ℹ️ 已注销认证")
        }

        return super.onStartCommand(intent, flags, startId)
    }
}