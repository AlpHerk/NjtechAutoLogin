package com.herk.njtechlogin.util

import android.content.pm.PackageInfo
import android.content.pm.PackageManager
import android.os.Build
import androidx.annotation.RequiresApi
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import okhttp3.OkHttpClient
import okhttp3.Request

class ChekUpdate {

    @RequiresApi(Build.VERSION_CODES.P)
    fun checkUpdate(): Boolean {
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
                    if (code.versionCode > currentVer) {
                        return true
                    }
                }
            }
        } catch (e: Exception) {
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
        val mg: PackageManager = MyApp.context.packageManager
        try {
            val info: PackageInfo = mg.getPackageInfo(MyApp.context.packageName, 0)
            return info.longVersionCode
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return 0
    }

    class App(val version: String, val versionCode: Long)
}