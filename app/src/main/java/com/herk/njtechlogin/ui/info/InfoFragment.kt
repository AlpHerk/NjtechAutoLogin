package com.herk.njtechlogin.ui.info
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.herk.njtechlogin.feedback.FeedbackActivity
import com.herk.njtechlogin.util.MyApp
import com.herk.njtechlogin.databinding.FragmentInfoBinding


class InfoFragment : Fragment() {

    private lateinit var binding: FragmentInfoBinding

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentInfoBinding.inflate(inflater, container, false)

        binding.updateBtn.setOnClickListener {
            Toast.makeText(MyApp.context, "已经是最新版了~", Toast.LENGTH_SHORT).show()
        }
        binding.explainBtn.setOnClickListener {
            val uri = Uri.parse("https://blog.csdn.net/Alpherkin/article/details/120580798")
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        }
        binding.feedbackBtn.setOnClickListener {
            startActivity(Intent(MyApp.context, FeedbackActivity::class.java))
        }
        return binding.root
    }

}