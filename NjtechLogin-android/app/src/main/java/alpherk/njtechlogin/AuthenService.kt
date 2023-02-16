package alpherk.njtechlogin
import alpherk.njtechlogin.login.LoginData
import alpherk.njtechlogin.util.AutoLogin
import alpherk.njtechlogin.util.NetUtil
import alpherk.njtechlogin.util.showToast
import android.app.Service
import android.content.Intent
import android.os.IBinder
import kotlinx.coroutines.*

class AuthenService : Service() {
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }

    override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {

        scope.launch {
            launch(Dispatchers.IO) {
                if (!NetUtil.setWiFiEnabled()) {
                    showToast("安卓9以上，请手动打开 WiFi")
                    stopSelf()
                }
            }
            showToast("正在网络认证中···")
            val userData = LoginData().postUserData()
            val deferred1 = async(Dispatchers.IO) {
                AutoLogin.askLogin(userData)
            }
//            val deferred2 = async(Dispatchers.IO) {
//                delay(1)
//                AutoLogin.askLogin(userData)
//            }
//            if (deferred1.await().first || deferred2.await().first) {
//                showToast(deferred1.await().second)
//                stopSelf()
//            } else if (!(deferred1.await().first && deferred2.await().first)) {
//                showToast(deferred2.await().second) // 输出错误信息
//                stopSelf()
//            }
            showToast(deferred1.await().second)
        }
        return super.onStartCommand(intent, flags, startId)
    }

    override fun onDestroy() {
        super.onDestroy()
        job.cancel()
    }

}