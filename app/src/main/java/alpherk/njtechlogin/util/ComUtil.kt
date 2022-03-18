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