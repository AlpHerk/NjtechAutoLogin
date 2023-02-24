package alpherk.njtechlogin.ui

import alpherk.njtechlogin.R
import alpherk.njtechlogin.service.AuthenService
import android.content.Intent
import android.os.Bundle

class NoneActivity : BaseActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        moveTaskToBack(true)
        setContentView(R.layout.activity_none)

        startForegroundService(Intent(applicationContext, AuthenService::class.java))
        finish()
    }

}