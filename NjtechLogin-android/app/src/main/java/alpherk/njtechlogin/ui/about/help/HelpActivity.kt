package alpherk.njtechlogin.ui.about.help
import alpherk.njtechlogin.R
import alpherk.njtechlogin.databinding.ActivityHelpBinding
import alpherk.njtechlogin.ui.BaseActivity
import alpherk.njtechlogin.util.CSDN_PRJ_URL
import alpherk.njtechlogin.util.OFFICE_WEB
import android.content.Intent
import android.content.res.Configuration
import android.net.Uri
import android.os.Bundle

class HelpActivity : BaseActivity() {
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

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)
        setContentView(R.layout.activity_help)
    }
}