package com.herk.njtechlogin.util
import android.util.Log
import android.widget.Toast
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext


suspend fun showToast(string: String, duration: Int = Toast.LENGTH_SHORT)
    = withContext(Dispatchers.Main) {
    Toast.makeText(MyApp.context, string, duration).show()
    Log.e("Herk", "$string: ${Thread.currentThread().name}")
}
suspend fun showSnackbar(string: String, duration: Int = Toast.LENGTH_SHORT)
    = withContext(Dispatchers.Main) {
    Toast.makeText(MyApp.context, string, duration).show()
    Log.e("Herk", "$string: ${Thread.currentThread().name}")
}