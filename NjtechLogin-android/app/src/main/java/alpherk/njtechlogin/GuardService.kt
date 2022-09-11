package alpherk.njtechlogin
import alpherk.njtechlogin.main.about.feedback.FeedbackActivity
import alpherk.njtechlogin.main.setting.SettingData
import alpherk.njtechlogin.util.CNTTIME_defVal
import alpherk.njtechlogin.util.MyApp.Companion.context
import alpherk.njtechlogin.util.NetUtil
import alpherk.njtechlogin.util.showToast
import android.annotation.SuppressLint
import android.app.*
import android.content.Intent
import android.graphics.Color
import android.os.IBinder
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlin.concurrent.thread

const val CHANNEL_ID = "channel guard"
const val CHANNEL_NAME = "网络守护服务"


class GuardService : Service() {
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }

    @SuppressLint("UnspecifiedImmutableFlag")
    override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {
        thread {
            while(SettingData().isGardNet) {
                if (!NetUtil.pingNetwork()) {
                    startService(Intent(this, AuthenService::class.java))
                }
                Thread.sleep((CNTTIME_defVal * 60 * 1000).toLong())
            }
        }
        val noteChannel = NotificationChannel(CHANNEL_ID, CHANNEL_NAME, NotificationManager.IMPORTANCE_DEFAULT)
        noteChannel.lockscreenVisibility = Notification.VISIBILITY_PUBLIC
        noteChannel.lightColor = Color.GREEN
        noteChannel.setSound(null, null)
        noteChannel.enableLights(true)
        noteChannel.setShowBadge(true)
        val manager = context.getSystemService(NOTIFICATION_SERVICE) as NotificationManager
        manager.createNotificationChannel(noteChannel)
        val guardIntent: PendingIntent = Intent(this, FeedbackActivity::class.java).let {
                notifyIntent -> PendingIntent.getActivity(this, 0, notifyIntent, PendingIntent.FLAG_IMMUTABLE)
        }
        val notification = Notification.Builder(this, CHANNEL_ID)
            .setChannelId(CHANNEL_ID)
            .setSmallIcon(R.drawable.shield)
            .setContentTitle(getText(R.string.notification_title))
            .setContentText(getText(R.string.notification_message))
            .setTicker(getText(R.string.ticker_text))
            .setContentIntent(guardIntent)
            .build()
        startForeground(1, notification); //开始前台服务
        return super.onStartCommand(intent, flags, startId)
    }

    override fun onDestroy() {
        scope.launch {
            showToast("守护服务已关闭")
            job.cancel()
        }
        stopForeground(true); // 停止服务并移除通知
        super.onDestroy()
    }
}