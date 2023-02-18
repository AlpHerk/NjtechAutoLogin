package alpherk.njtechlogin.ui.about.help
import alpherk.njtechlogin.databinding.ActivityHelpBinding
import alpherk.njtechlogin.util.CSDN_PRJ_URL
import alpherk.njtechlogin.util.OFFICE_WEB
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
            val uri = Uri.parse(CSDN_PRJ_URL)
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.downWinVersion.setOnClickListener {
            val uri = Uri.parse(OFFICE_WEB)
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
    }
}