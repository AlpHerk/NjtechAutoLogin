package alpherk.njtechlogin.util
import android.view.View
import android.widget.Toast
import com.google.android.material.snackbar.Snackbar
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext


suspend fun showToast(toast: String, duration: Int = Toast.LENGTH_SHORT)
    = withContext(Dispatchers.Main) {
    Toast.makeText(MyApp.context, toast, duration).show()
}
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