package alpherk.njtechlogin
import alpherk.njtechlogin.login.LoginData
import alpherk.njtechlogin.util.AutoLogin
import alpherk.njtechlogin.util.NetUtil
import alpherk.njtechlogin.util.showToast
import android.app.Service
import android.content.Intent
import android.os.IBinder
import kotlinx.coroutines.*

class LoginService : Service() {
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }

    override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {

        scope.launch {
            launch(Dispatchers.IO) {
                if (!NetUtil.setWiFiEnabled()) {
                    showToast("安卓9以上版本，请手动打开 WiFi")
                    stopSelf()
                }
            }
            showToast("正在努力认证···")
            val userData = LoginData().postUserData()
            val deferred1 = async(Dispatchers.IO) {
                AutoLogin.askLogin(userData)
            }
            val deferred2 = async(Dispatchers.IO) {
                AutoLogin.askLogin(userData)
            }
            val deferred3 = async(Dispatchers.IO) {
                AutoLogin.askLogin(userData)
            }
            if (deferred1.await() || deferred2.await() || deferred3.await()) {
                showToast("认证成功，恭喜你畅享网络~")
                stopSelf()
            } else if (!(deferred1.await() && deferred2.await() && deferred3.await())) {
                delay(3)
                showToast("认证失败，请检测账号状态!")
                stopSelf()
            }
        }
        return super.onStartCommand(intent, flags, startId)
    }

    override fun onDestroy() {
        super.onDestroy()
        job.cancel()
    }

}