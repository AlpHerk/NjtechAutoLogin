package com.herk.njtechlogin.main.setting
import androidx.core.content.edit
import com.herk.njtechlogin.util.*


class SettingData {
    private val prefs = MyApp.context.getSharedPreferences(SETTING_FILE, 0)
    val isGardNet = prefs.getBoolean(GARDNET, GARDNET_defVal)
    val isAutoRun = prefs.getBoolean(AUTORUN, AUTORUN_defVal)

    fun save(controller: String, boolean: Boolean) {
        MyApp.context.getSharedPreferences(SETTING_FILE, 0).edit() {
            putBoolean(controller, boolean)
        }
    }
}