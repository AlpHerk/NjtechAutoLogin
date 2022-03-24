package alpherk.njtechlogin.main.setting
import alpherk.njtechlogin.util.*
import androidx.core.content.edit


class SettingData {
    private val prefs = MyApp.context.getSharedPreferences(SETING_FIL, 0)
    val isGardNet = prefs.getBoolean(GARDNET, GARDNET_defVal)
    val isAutoRun = prefs.getBoolean(AUTORUN, AUTORUN_defVal)
//    val reCnttime = prefs.getBoolean(CNTTIME, AUTORUN_defVal)

    fun save(controller: String, boolean: Boolean) {
        MyApp.context.getSharedPreferences(SETING_FIL, 0).edit() {
            putBoolean(controller, boolean)
        }
    }
}