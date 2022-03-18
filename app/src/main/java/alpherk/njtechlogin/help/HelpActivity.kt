package alpherk.njtechlogin.help
import alpherk.njtechlogin.databinding.ActivityHelpBinding
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class HelpActivity : AppCompatActivity() {
    private lateinit var binding: ActivityHelpBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityHelpBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.csdnHelpBtn.setOnClickListener {
            val uri = Uri.parse("https://blog.csdn.net/Alpherkin/article/details/120580798")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.downWinVersion.setOnClickListener {
            val uri = Uri.parse("https://alpherk.github.io/NjtechAutoLogin/release/NjtechLogin.apk")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
    }
}