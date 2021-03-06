package alpherk.njtechlogin.feedback
import alpherk.njtechlogin.databinding.ActivityFeedbackBinding
import alpherk.njtechlogin.util.MyApp
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class FeedbackActivity : AppCompatActivity() {
    private lateinit var binding: ActivityFeedbackBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityFeedbackBinding.inflate(layoutInflater)
        setContentView(binding.root)

        Toast.makeText(MyApp.context, "点击图标自动跳转", Toast.LENGTH_SHORT).show()
        binding.contactQQImg.setOnClickListener {
            try {
                val qqUrl = "mqqwpa://im/chat?chat_type=wpa&uin=1924450620"
                startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(qqUrl)))
            } catch (e: Exception) {
                Toast.makeText(MyApp.context, "请安装QQ后重试", Toast.LENGTH_SHORT).show()
            }
        }
        binding.contactGithubImg.setOnClickListener {
            val uri = Uri.parse("https://github.com/AlpHerk")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.contactCSDNImg.setOnClickListener {
            val uri = Uri.parse("https://blog.csdn.net/Alpherkin?spm=1000.2115.3001.5343")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.goMyPage.setOnClickListener {
            val uri = Uri.parse("https://alpherk.github.io/NjtechAutoLogin/")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
    }
}