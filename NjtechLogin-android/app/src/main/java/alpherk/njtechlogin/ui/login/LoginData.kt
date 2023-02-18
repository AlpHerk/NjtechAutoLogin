package alpherk.njtechlogin.ui.login
import alpherk.njtechlogin.util.*


class LoginData {
    private val prefs = MyApp.context.getSharedPreferences(USER_DATA, 0)
    val username = prefs.getString(USERNAME, "")!!
    val password = prefs.getString(PASSWORD, "")!!
    val netCompa = prefs.getString(NETCOMPA, "1")!!

    fun postUserData(): List<String> {
        return listOf(username, password, netCompa)
    }
}

















