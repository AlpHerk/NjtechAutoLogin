package com.herk.njtechlogin.main.home
import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.herk.njtechlogin.LoginService
import com.herk.njtechlogin.databinding.FragmentHomeBinding


class HomeFragment : Fragment() {
    private lateinit var binding: FragmentHomeBinding

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentHomeBinding.inflate(inflater, container, false)

        binding.requestLoginBtn.setOnClickListener {
            activity?.startService(Intent(activity, LoginService::class.java))
        }

        return binding.root
    }

}