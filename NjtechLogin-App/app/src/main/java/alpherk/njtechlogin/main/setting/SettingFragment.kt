package alpherk.njtechlogin.main.setting
import alpherk.njtechlogin.GuardService
import alpherk.njtechlogin.databinding.FragmentSettingBinding
import alpherk.njtechlogin.util.AUTORUN
import alpherk.njtechlogin.util.GARDNET
import alpherk.njtechlogin.util.MyApp
import alpherk.njtechlogin.util.SETING_FIL
import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.edit
import androidx.fragment.app.Fragment

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
        MyApp.context.getSharedPreferences(SETING_FIL,0).edit() {
            putBoolean(GARDNET, binding.gardNetSwt.isChecked)
            putBoolean(AUTORUN, binding.autoRunSwt.isChecked)
        }
    }

}