package com.herk.njtechlogin.main.info
import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.herk.njtechlogin.feedback.FeedbackActivity
import com.herk.njtechlogin.util.MyApp
import com.herk.njtechlogin.databinding.FragmentInfoBinding
import com.herk.njtechlogin.help.HelpActivity


class InfoFragment : Fragment() {

    private lateinit var binding: FragmentInfoBinding

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentInfoBinding.inflate(inflater, container, false)

        binding.updateBtn.setOnClickListener {
            Toast.makeText(MyApp.context, "检查失败，请点击使用教程~", Toast.LENGTH_SHORT).show()
        }
        binding.explainBtn.setOnClickListener {
            startActivity(Intent(MyApp.context, HelpActivity::class.java))
        }
        binding.feedbackBtn.setOnClickListener {
            startActivity(Intent(MyApp.context, FeedbackActivity::class.java))
        }
        return binding.root
    }

}