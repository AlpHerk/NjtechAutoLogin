package com.herk.njtechlogin
import android.annotation.SuppressLint
import android.app.*
import android.content.Intent
import android.graphics.Color
import android.os.Build
import android.os.IBinder
import androidx.annotation.RequiresApi
import com.herk.njtechlogin.feedback.FeedbackActivity
import com.herk.njtechlogin.main.setting.SettingData
import com.herk.njtechlogin.util.CNTTIME_defVal
import com.herk.njtechlogin.util.MyApp.Companion.context
import com.herk.njtechlogin.util.NetUtil
import com.herk.njtechlogin.util.showToast
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlin.concurrent.thread

const val CHANNEL_GUARD_ID = "channel guard"
const val CHANNEL_GUARD_NAME = "守护服务"


class GuardService : Service() {
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }

    @RequiresApi(Build.VERSION_CODES.O)
    @SuppressLint("UnspecifiedImmutableFlag")
    override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {
        thread {
            while(SettingData().isGardNet) {
                if (!NetUtil.isNetWorked())
                    startService(Intent(this, LoginService::class.java))
                Thread.sleep((CNTTIME_defVal*60*1000).toLong())
            }
        }
        val noteChannel: NotificationChannel
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            noteChannel = NotificationChannel(
                CHANNEL_GUARD_ID, CHANNEL_GUARD_NAME, NotificationManager.IMPORTANCE_DEFAULT)
            noteChannel.lockscreenVisibility = Notification.VISIBILITY_PUBLIC
            noteChannel.lightColor = Color.GREEN
            noteChannel.setSound(null, null)
            noteChannel.enableLights(true)
            noteChannel.setShowBadge(true)
            val manager = context.getSystemService(NOTIFICATION_SERVICE) as NotificationManager
            manager.createNotificationChannel(noteChannel)
        }
        val guardIntent: PendingIntent = Intent(this, FeedbackActivity::class.java).let {
                notifyIntent -> PendingIntent.getActivity(this, 0, notifyIntent, 0)}
        val notification = Notification.Builder(this, CHANNEL_GUARD_ID)
            .setChannelId(CHANNEL_GUARD_ID)
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