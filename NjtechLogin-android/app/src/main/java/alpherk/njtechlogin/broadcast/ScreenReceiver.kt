package alpherk.njtechlogin.broadcast

import alpherk.njtechlogin.AuthenService
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent

class ScreenReceiver: BroadcastReceiver() {

    override fun onReceive(context: Context?, intent: Intent?) {

        val action = intent!!.action
        if ("android.intent.action.SCREEN_ON" == action) {
            context?.startService(Intent(context, AuthenService::class.java))
        }
    }

}