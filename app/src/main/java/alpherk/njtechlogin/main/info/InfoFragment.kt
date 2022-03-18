package alpherk.njtechlogin.main.info
import alpherk.njtechlogin.databinding.FragmentInfoBinding
import alpherk.njtechlogin.feedback.FeedbackActivity
import alpherk.njtechlogin.help.HelpActivity
import alpherk.njtechlogin.util.ChekUpdate
import alpherk.njtechlogin.util.MyApp
import alpherk.njtechlogin.util.showToast
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.annotation.RequiresApi
import androidx.fragment.app.Fragment
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch

class InfoFragment : Fragment() {

    private lateinit var binding: FragmentInfoBinding

    @RequiresApi(Build.VERSION_CODES.P)
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentInfoBinding.inflate(inflater, container, false)

        binding.updateBtn.setOnClickListener {
            update()
        }
        binding.explainBtn.setOnClickListener {
            startActivity(Intent(MyApp.context, HelpActivity::class.java))
        }
        binding.feedbackBtn.setOnClickListener {
            startActivity(Intent(MyApp.context, FeedbackActivity::class.java))
        }
        return binding.root
    }

    private val job = Job()
    private val scope = CoroutineScope(job)

    @RequiresApi(Build.VERSION_CODES.P)
    fun update() {
        scope.launch {
            showToast("版本检测中~")
            if (ChekUpdate().checkUpdate()) {
                showToast("有新版本可用")
                val uri = Uri.parse("https://alpherk.github.io/NjtechAutoLogin/release/NjtechLogin.apk")
                startActivity(Intent(Intent.ACTION_VIEW, uri))
            } else {
                showToast("已更新最新版")
            }
        }
    }
}