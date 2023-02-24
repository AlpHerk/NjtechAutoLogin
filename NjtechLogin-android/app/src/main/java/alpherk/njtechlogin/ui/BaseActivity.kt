package alpherk.njtechlogin.ui

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class BaseActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_base)
    }
}