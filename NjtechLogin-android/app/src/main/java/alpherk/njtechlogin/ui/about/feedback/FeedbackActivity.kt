package alpherk.njtechlogin.ui.about.feedback
import alpherk.njtechlogin.databinding.ActivityFeedbackBinding
import alpherk.njtechlogin.util.CSDN_PRJ_URL
import alpherk.njtechlogin.util.GITHUB_URL
import alpherk.njtechlogin.util.OFFICE_WEB
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
            val uri = Uri.parse(GITHUB_URL)
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.contactCSDNImg.setOnClickListener {
            val uri = Uri.parse(CSDN_PRJ_URL)
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.goMyPage.setOnClickListener {
            val uri = Uri.parse(OFFICE_WEB)
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
    }
}