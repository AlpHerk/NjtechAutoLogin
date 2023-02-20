package alpherk.njtechlogin.ui.setting
import alpherk.njtechlogin.util.*
import androidx.core.content.edit


class SettingData {
    private val prefs = MyApp.context.getSharedPreferences(USER_DATA, 0)
    val isGardNet = prefs.getBoolean(GARDNET, GARDNET_defVal)
    val isAutoRun = prefs.getBoolean(AUTORUN, AUTORUN_defVal)

    fun save(controller: String, boolean: Boolean) {
        MyApp.context.getSharedPreferences(USER_DATA, 0).edit() {
            putBoolean(controller, boolean)
        }
    }
}