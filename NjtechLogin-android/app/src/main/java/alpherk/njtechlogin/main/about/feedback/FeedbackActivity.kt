package alpherk.njtechlogin.main.about.feedback
import alpherk.njtechlogin.databinding.ActivityFeedbackBinding
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class FeedbackActivity : AppCompatActivity() {

    private lateinit var binding: ActivityFeedbackBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityFeedbackBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.contactGithubImg.setOnClickListener {
            val uri = Uri.parse("https://github.com/AlpHerk")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.contactCSDNImg.setOnClickListener {
            val uri = Uri.parse("https://blog.csdn.net/Alpherkin/article/details/115599094")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.goMyPage.setOnClickListener {
            val uri = Uri.parse("https://alpherk.github.io/NjtechAutoLogin/")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
    }
}