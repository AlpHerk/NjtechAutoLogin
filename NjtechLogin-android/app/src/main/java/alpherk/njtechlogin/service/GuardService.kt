package alpherk.njtechlogin.service
import alpherk.njtechlogin.R
import alpherk.njtechlogin.ui.about.feedback.FeedbackActivity
import alpherk.njtechlogin.ui.setting.SettingData
import alpherk.njtechlogin.util.CNTTIME_defVal
import alpherk.njtechlogin.util.MyApp.Companion.context
import alpherk.njtechlogin.util.NetUtil
import alpherk.njtechlogin.util.showToast
import android.annotation.SuppressLint
import android.app.*
import android.content.Intent
import android.graphics.Color
import android.os.IBinder
import android.util.Log
import androidx.core.app.NotificationCompat
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlin.concurrent.thread

const val CHANNEL_ID = "alpherk.njtechlogin.channel"
const val CHANNEL_NAME = "网络守护服务"

/**
 * 网络守护服务
 */
class GuardService : Service() {
    private val job = Job()
    private val scope = CoroutineScope(job)
    private var isGuardRun = false

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }


    override fun onCreate() {

        val notification = buildNotification()

        startForeground(1, notification.build()); //开始前台服务
        isGuardRun = true


        thread {
            while(SettingData().isGardNet) {
                if (!NetUtil.pingNetwork()) {
                    startService(Intent(this, AuthenService::class.java))
                    Log.d("Herkin", "守护中，启动认证")
                } else {
                    Log.d("Herkin", "守护中，网络畅通")
                }
                Thread.sleep((CNTTIME_defVal * 60 * 1000).toLong())
            }
        }

        super.onCreate()
    }

    override fun onDestroy() {
        scope.launch {
            showToast("守护服务已关闭")
            job.cancel()
        }
        isGuardRun = false
        stopForeground(true); // 停止服务并移除通知

        super.onDestroy()
    }


    private fun buildNotification(): Notification.Builder {

        // IMPORTANCE_UNSPECIFIED 在安卓11上不显示通知
        try {
            val noteChannel =  NotificationChannel(CHANNEL_ID, CHANNEL_NAME, NotificationManager.IMPORTANCE_UNSPECIFIED)
            noteChannel.lockscreenVisibility = Notification.VISIBILITY_PRIVATE
            noteChannel.setShowBadge(false)

            val manager = context.getSystemService(NOTIFICATION_SERVICE) as NotificationManager
            manager.createNotificationChannel(noteChannel)
            Log.d("Herkin", "前台服务：IMPORTANCE_UNSPECIFIED --------------")

        } catch (ex: Exception) {
            val noteChannel =  NotificationChannel(CHANNEL_ID, CHANNEL_NAME, NotificationManager.IMPORTANCE_DEFAULT)
            noteChannel.lockscreenVisibility = Notification.VISIBILITY_PRIVATE
            noteChannel.setShowBadge(false)

            val manager = context.getSystemService(NOTIFICATION_SERVICE) as NotificationManager
            manager.createNotificationChannel(noteChannel)
            Log.d("Herkin", "前台服务：IMPORTANCE_DEFAULT --------------")

        }

        val guardIntent: PendingIntent = Intent(this, FeedbackActivity::class.java).let {
                notifyIntent -> PendingIntent.getActivity(this, 0, notifyIntent, PendingIntent.FLAG_IMMUTABLE)
        }

        val notification = Notification.Builder(this, CHANNEL_ID)
            .setChannelId(CHANNEL_ID)
            .setOngoing(true)
            .setSmallIcon(R.drawable.shield)
            .setContentTitle(getText(R.string.notification_title))
            .setContentText(getText(R.string.notification_message))
            .setTicker(getText(R.string.ticker_text))
            .setContentIntent(guardIntent)

        return notification
    }

}