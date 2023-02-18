package alpherk.njtechlogin.ui.about
import alpherk.njtechlogin.databinding.FragmentInfoBinding
import alpherk.njtechlogin.ui.about.feedback.FeedbackActivity
import alpherk.njtechlogin.ui.about.help.HelpActivity
import alpherk.njtechlogin.util.*
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.appcompat.app.AlertDialog
import androidx.fragment.app.Fragment


class InfoFragment : Fragment() {

    private lateinit var binding: FragmentInfoBinding

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentInfoBinding.inflate(inflater, container, false)

        binding.updateBtn.setOnClickListener {
            this.context?.let { it1 -> dialogUpdate(it1) }
        }
        binding.explainBtn.setOnClickListener {
            startActivity(Intent(MyApp.context, HelpActivity::class.java))
        }
        binding.feedbackBtn.setOnClickListener {
            startActivity(Intent(MyApp.context, FeedbackActivity::class.java))
        }

        return binding.root
    }

    /**
     * 关于帮助页：检查跟新对话框
     */
    private fun dialogUpdate(context: Context) {

        val checkInfo = Update.checkUpdateFromLocalCache(context)
        if (checkInfo.vercode != Update.getCurrentVerCode()) {
            AlertDialog.Builder(context).apply {
                setCancelable(true)
                setTitle("检测更新")
                setMessage("是否跳转到浏览器下载")
                setPositiveButton("确认") { _, _ ->
                    try {
                        val uri = Uri.parse(checkInfo.downUrl)
                        startActivity(Intent(Intent.ACTION_VIEW, uri))
                    } catch (ex: Exception) {
                        Log.d("Herkin", "已更新最新版")
                    }
                }
                setNegativeButton("取消") { _, _ ->
                }
                show()
            }
        } else {
            AlertDialog.Builder(context).apply {
                setCancelable(true)
                setTitle("检测更新")
                setMessage("当前已经是最新版：${checkInfo.vername}")
                setPositiveButton("确认") { _, _ ->
                }
                setNegativeButton("查看") { _, _ ->
                    val uri = Uri.parse(CSDN_PRJ_URL)
                    startActivity(Intent(Intent.ACTION_VIEW, uri))
                }
                show()
            }
        }
//        Log.d("Herkin", "${checkInfo.vercode}")
    }
}