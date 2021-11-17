package com.herk.njtechlogin
import android.app.Service
import android.content.Intent
import android.os.IBinder
import com.herk.njtechlogin.ui.setting.SettingData
import com.herk.njtechlogin.util.NetUtil
import com.herk.njtechlogin.util.showToast
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlin.concurrent.thread


class LoginGuardService : Service() {
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }

    override fun onCreate() {
        super.onCreate()
        scope.launch {
            showToast("守护服务开始运行")
        }
    }

    override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {
        thread {
            val condition = SettingData().reLogin
            while(condition) {
                if (!NetUtil.isNetWorked()) startService(Intent(this, LoginService::class.java))
                Thread.sleep(10)
            }
        }
        return super.onStartCommand(intent, flags, startId)
    }

    override fun onDestroy() {
        super.onDestroy()
        scope.launch {
            showToast("守护服务已经关闭")
            job.cancel()
        }
    }
}