package alpherk.njtechlogin.util

import alpherk.njtechlogin.R
import android.content.Context
import android.content.pm.PackageInfo
import android.content.pm.PackageManager
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import okhttp3.OkHttpClient
import okhttp3.Request
import org.json.JSONArray
import org.json.JSONObject

object Update {

    data class Version(val vername: String, val vercode: Int, val downUrl: String)

    /**
     * 从网站链接检查更新，返回最新的版本信息 `Version`
     */
    fun checkUpdate(): Version? {
        try {
            val client = OkHttpClient()
            val request = Request.Builder().url(CHECKUP_URL).build()
            val resp = client.newCall(request).execute()
            val respJson = resp.body?.string()

            if (respJson != null) {
                val curcode = getCurrentVerCode()
                val newVer = analysisVersionFormJson(respJson)
                if (newVer != null) {
                    if (newVer.vercode > curcode) {
                        return Version(newVer.vername, newVer.vercode, newVer.downUrl)
                    }
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return null
    }

    /**
     * 从更新链接 `downUrl` 中解析出 `Version(vername, vercode, downUrl)`
     */
    private fun analysisVersionFormJson(jsonData: String): Version? {
        val jsonObject  = JSONObject(jsonData)
        val assets      = jsonObject.getString("assets")
        val assetsArray = JSONArray(assets)

        for (i in 0 until assetsArray.length()) {
            val jsonObj = assetsArray.getJSONObject(i)
            val name    = jsonObj.getString("name")
            val downUrl = jsonObj.getString("browser_download_url")

            if (name.endsWith(".apk")) {
                val vername = name.substringAfter("-v").substringBefore(".apk")
                val vercode = vername.filter { it.isDigit() }.toInt()

                return Version(vername, vercode, downUrl)
            }
        }
        return null
    }

    /**
     * 从本地缓存中检查更新， 返回版本信息 `Version`
     */
    fun checkUpdateFromLocalCache(context:Context): Version {

        val downUrl = getSharedPrefs(LOCAL_UPGRADE_URL, "") as String
        val curcode = getCurrentVerCode()

        if (downUrl  != "") {
            // !!! vercode vername 两句调换位置报错原因？
            val vername = downUrl.substringAfter("-v").substringBefore(".apk")
            val vercode = vername.filter { it.isDigit() }.toInt()
            if (vercode > curcode) {
                return Version(vername, vercode, downUrl)
            }
        }
        return Version(context.getString(R.string.app_version_name), curcode, "NunUrl")
    }

    @Deprecated("从更新链接中解析版本信息")
    private fun analysisVersionFormDownUrl(downUrl: String): Version{
        if (downUrl != "") {
            // !!! vercode vername 两句调换位置报错原因？
            val vername = downUrl.substringAfter("-v").substringBefore(".apk")
            val vercode = vername.filter { it.isDigit() }.toInt()
            return Version(vername, vercode, downUrl)
        }
        return Version("null", 0, "NunUrl")
    }

    fun getCurrentVerCode(): Int {
        val mg: PackageManager = MyApp.context.packageManager
        try {
            val info: PackageInfo = mg.getPackageInfo(MyApp.context.packageName, 0)
            return info.longVersionCode.toInt()
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return 0
    }


    @Deprecated("此检查更新已被弃用")
    class App(val version: String, val versionCode: Long)
    @Deprecated("此检查更新已被弃用")
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


    @Deprecated("此检查更新已被弃用")
    private fun parseJsonDeprecated(jsonData: String): List<App> {
        val gson = Gson()
        val typeOf = object : TypeToken<List<App>>() {}.type
        return gson.fromJson(jsonData, typeOf)
    }

}