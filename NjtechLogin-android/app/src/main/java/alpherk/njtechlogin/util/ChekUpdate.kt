package alpherk.njtechlogin.util

import android.content.pm.PackageInfo
import android.content.pm.PackageManager
import android.os.Build
import androidx.annotation.RequiresApi
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import okhttp3.OkHttpClient
import okhttp3.Request
import org.json.JSONArray
import org.json.JSONObject

class ChekUpdate {
 
    fun checkUpdate(): String? {
        try {
            val client = OkHttpClient()
            val request = Request.Builder()
                .url("https://api.github.com/repos/AlpHerk/NjtechAutoLogin/releases/latest")
                .build()
            val resp = client.newCall(request).execute()
            val respJson = resp.body?.string()

            if (respJson != null) {
                val curcode = getCurrentVerCode()
                val version = latestVers(respJson)
                if (version.vercode > curcode) {
                    return version.downUrl
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return null
    }

    data class Version(val vercode: Int, val downUrl: String)

    private fun latestVers(jsonData: String): Version {
        val jsonObject  = JSONObject(jsonData)
        val assets      = jsonObject.getString("assets")
        val assetsArray = JSONArray(assets)

        for (i in 0 until assetsArray.length()) {
            val jsonObj = assetsArray.getJSONObject(i)
            val name    = jsonObj.getString("name")

            if (name.endsWith(".apk")) {
                val downUrl = jsonObj.getString("browser_download_url")
                val vercode = name.filter { it.isDigit() }.toInt()
                return Version(vercode, downUrl)
            }
        }
        return Version(0, "NunUrl")
    }

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


    // 以下检查更新已被弃用
    class App(val version: String, val versionCode: Long)
    fun checkUpdateDeprecated(): Boolean {
        try {
            val client = OkHttpClient()
            val request = Request.Builder()
                .url("https://alpherk.github.io/NjtechAutoLogin/release/version.json")
                .build()
            val response = client.newCall(request).execute()
            val responseData = response.body?.string()
            if (responseData != null) {
                val versionList: List<App> = parseJsonDeprecated(responseData)
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
    private fun parseJsonDeprecated(jsonData: String): List<App> {
        val gson = Gson()
        val typeOf = object : TypeToken<List<App>>() {}.type
        return gson.fromJson(jsonData, typeOf)
    }

}