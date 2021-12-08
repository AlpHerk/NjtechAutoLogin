package com.herk.njtechlogin.main.setting
import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.edit
import androidx.fragment.app.Fragment
import com.herk.njtechlogin.GuardService
import com.herk.njtechlogin.util.*
import com.herk.njtechlogin.databinding.FragmentSettingBinding

class SettingFragment : Fragment() {

    private lateinit var binding: FragmentSettingBinding

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle? ): View {
        binding = FragmentSettingBinding.inflate(inflater, container, false)

        loadLoginData()

        binding.gardNetSwt.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                activity?.startService(Intent(activity, GuardService::class.java))
            } else {
                activity?.stopService(Intent(activity, GuardService::class.java))
            }
            saveLoginData()
        }
        binding.autoRunSwt.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                JumptoSetting.jumptoAutoRunSetting(MyApp.context)
            }
            saveLoginData()
        }
        return binding.root
    }

    private fun loadLoginData() {
        val settingData = SettingData()
        binding.gardNetSwt.isChecked = settingData.isGardNet
        binding.autoRunSwt.isChecked = settingData.isAutoRun
    }

    private fun saveLoginData() {
        MyApp.context.getSharedPreferences(SETTING_FILE,0).edit() {
            putBoolean(GARDNET, binding.gardNetSwt.isChecked)
            putBoolean(AUTORUN, binding.autoRunSwt.isChecked)
        }
    }

}