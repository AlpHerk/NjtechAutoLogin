package com.herk.njtechlogin

import android.app.Service
import android.content.Intent
import android.content.pm.PackageInfo
import android.content.pm.PackageManager
import android.os.Build
import android.os.IBinder
import androidx.annotation.RequiresApi
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import com.herk.njtechlogin.util.MyApp.Companion.context
import com.herk.njtechlogin.util.showToast
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import okhttp3.OkHttpClient
import okhttp3.Request

class UpDateService : Service() {
    private val job = Job()
    private val scope = CoroutineScope(job)

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }

    @RequiresApi(Build.VERSION_CODES.P)
    override fun onCreate() {
        super.onCreate()
        scope.launch {
            if (checkUpdate()) {
                showToast("有新版本可用")
            } else {
                showToast("已更新最新版")
            }
        }
    }

    @RequiresApi(Build.VERSION_CODES.P)
    private fun checkUpdate(): Boolean {
        try {
            val client = OkHttpClient()
            val request = Request.Builder()
                .url("https://alpherk.github.io/NjtechAutoLogin/release/version.json")
                .build()
            val response = client.newCall(request).execute()
            val responseData = response.body?.string()
            if (responseData != null) {
                val versionList: List<App> = parseJson(responseData)
                val currentVer = getCurrentVerCode()
                for (code in versionList) {
                    if (currentVer > code.versionCode) {
                        return true
                    }
                }
            }
        } catch (e:Exception) {
            e.printStackTrace()
        }
        return false
    }

    @RequiresApi(Build.VERSION_CODES.P)
    private fun parseJson(jsonData: String): List<App> {
        val gson = Gson()
        val typeOf = object : TypeToken<List<App>>() {}.type
        val versionList = gson.fromJson<List<App>>(jsonData, typeOf)
        return versionList
    }

    @RequiresApi(Build.VERSION_CODES.P)
    private fun getCurrentVerCode(): Long {
        val mg: PackageManager = context.packageManager
        try {
            val info: PackageInfo = mg.getPackageInfo(context.packageName, 0)
            return info.longVersionCode
        } catch (e:Exception) {
            e.printStackTrace();
        }
        return 0
    }

    class App(val version: String, val versionCode: Long)
}