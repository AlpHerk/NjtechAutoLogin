package com.herk.njtechlogin.ui.setting
import androidx.core.content.edit
import com.herk.njtechlogin.util.*
import com.herk.njtechlogin.R


class SettingData {
    private val dataName = MyApp.context.getString(R.string.prefs_setting_data)
    private val prefs = MyApp.context.getSharedPreferences(dataName, 0)
    val reLogin = prefs.getBoolean(RELOGIN, RELOGIN_STATE)
    private val autoRun = prefs.getBoolean(AUTORUN, AUTORUN_STATE)



    fun postData(): List<Boolean> {
        return listOf(reLogin, autoRun)
    }
    fun saveData(controller: String, boolean: Boolean) {
        val dataName = MyApp.context.getString(R.string.prefs_setting_data)
        MyApp.context.getSharedPreferences(dataName, 0).edit() {
            putBoolean(controller, boolean)
        }
    }
    fun loadData() {

    }

}