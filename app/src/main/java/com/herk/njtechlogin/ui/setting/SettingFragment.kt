package com.herk.njtechlogin.ui.setting
import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.edit
import androidx.fragment.app.Fragment
import com.herk.njtechlogin.LoginGuardService
import com.herk.njtechlogin.util.*
import com.herk.njtechlogin.R
import com.herk.njtechlogin.databinding.FragmentSettingBinding


class SettingFragment : Fragment() {

    private lateinit var binding: FragmentSettingBinding

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle? ): View {
        binding = FragmentSettingBinding.inflate(inflater, container, false)

        loadLoginData()

        binding.reLoginSwt.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                activity?.startService(Intent(activity, LoginGuardService::class.java))
            } else {
                activity?.stopService(Intent(activity, LoginGuardService::class.java))
            }
            saveLoginData()
        }
        binding.autoRunSwt.setOnCheckedChangeListener { _, _ ->
            JumptoSetting.jumptoAutoRunSetting(MyApp.context)
            saveLoginData()
        }
        return binding.root
    }

    private fun loadLoginData() {
        val dataName = getString(R.string.prefs_setting_data)
        val prefs = MyApp.context.getSharedPreferences(dataName, 0)
        binding.autoRunSwt.isChecked = prefs.getBoolean(RELOGIN, RELOGIN_STATE)
        binding.reLoginSwt.isChecked = prefs.getBoolean(AUTORUN, AUTORUN_STATE)
    }

    private fun saveLoginData() {
        val dataName = getString(R.string.prefs_setting_data)
        MyApp.context.getSharedPreferences(dataName, 0).edit() {
            putBoolean(AUTORUN, binding.reLoginSwt.isChecked)
            putBoolean(RELOGIN, binding.autoRunSwt.isChecked)
        }
    }

}