package alpherk.njtechlogin.ui

import alpherk.njtechlogin.R
import alpherk.njtechlogin.util.ActivityCollector
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity


open class BaseActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_base)
        ActivityCollector.addActivity(this);
    }
    override fun onDestroy() {
        super.onDestroy()
        ActivityCollector.removeActivity(this)
    }

}