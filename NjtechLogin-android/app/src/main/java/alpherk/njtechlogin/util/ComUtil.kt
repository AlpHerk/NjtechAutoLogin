package alpherk.njtechlogin.util
import android.view.View
import android.widget.Toast
import androidx.core.content.edit
import com.google.android.material.snackbar.Snackbar
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext


/**
 * 显示 `toast`
 */
suspend fun showToast(toast: String, duration: Int = Toast.LENGTH_SHORT)
    = withContext(Dispatchers.Main) {
    Toast.makeText(MyApp.context, toast, duration).show()
}

/**
 * `Snackbar`
 */
suspend fun showSnackbar(view: View, toast: String, duration: Int = Snackbar.LENGTH_SHORT)
    = withContext(Dispatchers.Main) {
    Snackbar.make(view, toast, duration).show()
}
fun View.showSnackbar(text:String, duration: Int = Snackbar.LENGTH_SHORT) {
    Snackbar.make(this, text, duration).show()
}
fun View.showSnackbar(resId:Int, duration: Int = Snackbar.LENGTH_SHORT) {
    Snackbar.make(this, resId, duration).show()
}
fun View.showSnackbar(text:String, actionText:String?=null,
                      duration: Int = Snackbar.LENGTH_LONG,
                      block:(()->Unit)?=null) {
    val snackbar = Snackbar.make(this, text, duration)
    if (actionText!=null && block!=null) {
        snackbar.setAction(actionText) {
            block()
        }
    }
    snackbar.show()
}
fun View.showSnackbar(resId:Int, actionText:String? = null,
                      duration: Int = Snackbar.LENGTH_LONG,
                      block: (() -> Unit)? = null) {
    val snackbar = Snackbar.make(this, resId, duration)
    if (actionText!=null && block!=null) {
        snackbar.setAction(actionText) {
            block()
        }
    }
    snackbar.show()
}

/**
 * 读取 SharedPreferences 数据
 */
fun getSharedPrefs(key: String, defValue: Any, fromFile: String=USER_DATA): Any? {
    val prefs = MyApp.context.getSharedPreferences(fromFile, 0)

    when (defValue) {
        is Boolean -> return prefs.getBoolean(key, defValue)
        is String  -> return prefs.getString(key,  defValue)
        is Int     -> return prefs.getInt(key,     defValue)
        is Long    -> return prefs.getLong(key,    defValue)
        is Float   -> return prefs.getFloat(key,   defValue)
    }
    return "null"
}

/**
 * 写入 SharedPreferences 数据
 */
fun saveSharedPrefs(key: String, value: Any, to: String=USER_DATA) {
    MyApp.context.getSharedPreferences(to, 0).edit() {

        when (value) {
            is Boolean -> putBoolean(key, value)
            is String  -> putString(key,  value)
            is Int     -> putInt(key,     value)
            is Long    -> putLong(key,    value)
            is Float   -> putFloat(key,   value)
        }
    }
}



