package alpherk.njtechlogin.ui

import alpherk.njtechlogin.R
import alpherk.njtechlogin.service.AuthenService
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.MenuItem

class NoneActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        moveTaskToBack(true)
        setContentView(R.layout.activity_none)

        startForegroundService(Intent(applicationContext, AuthenService::class.java))
        finish()
    }
//    override fun onOptionsItemSelected(item: MenuItem) = when (item.itemId) {
//        android.R.id.home -> {
//            onBackPressed()
//            true
//        }
//        else -> super.onOptionsItemSelected(item)
//    }

}