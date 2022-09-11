package alpherk.njtechlogin.main.about
import alpherk.njtechlogin.databinding.FragmentInfoBinding
import alpherk.njtechlogin.main.about.feedback.FeedbackActivity
import alpherk.njtechlogin.main.about.help.HelpActivity
import alpherk.njtechlogin.util.Update
import alpherk.njtechlogin.util.MyApp
import alpherk.njtechlogin.util.showToast
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.appcompat.app.AlertDialog
import androidx.fragment.app.Fragment
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch

class InfoFragment : Fragment() {

    private lateinit var binding: FragmentInfoBinding

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentInfoBinding.inflate(inflater, container, false)

        binding.updateBtn.setOnClickListener {
            update(MyApp.context)
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

    private fun update(context: Context) {
        scope.launch {
            showToast("版本检测中~")
            val downUrl = Update().checkUpdate()

            if (downUrl != null) {
                showToast("检测到有新版本可用")
                val uri = Uri.parse(downUrl)
                startActivity(Intent(Intent.ACTION_VIEW, uri))
//                AlertDialog.Builder(context).apply {
//                    setTitle("检测更新")
//                    setMessage("是否前往下载")
//                    setCancelable(false)
//                    setPositiveButton("确认") { dialog, which ->
//                        val uri = Uri.parse(downUrl)
//                        startActivity(Intent(Intent.ACTION_VIEW, uri))
//                    }
//                    setNegativeButton("下次再说") { dialog, which ->
//                    }
//                    show()
//                }
            } else {
                showToast("已更新最新版")
            }
        }
    }
}