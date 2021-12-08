package com.herk.njtechlogin.main.setting
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.provider.Settings
import android.widget.Toast
import java.util.*

object JumptoSetting {
    private val hashMap: HashMap<String, List<String>> = object : HashMap<String, List<String>>() {
            init {
                put("Xiaomi", listOf(
                    "com.miui.securitycenter/com.miui.permcenter.autostart.AutoStartManagementActivity",
                    "com.miui.securitycenter"))
                put("samsung", listOf(
                    "com.samsung.android.sm_cn/com.samsung.android.sm.mainui.ram.AutoRunActivity",
                    "com.samsung.android.sm_cn/com.samsung.android.sm.mainui.appmanagement.AppManagementActivity",
                    "com.samsung.android.sm_cn/com.samsung.android.sm.mainui.cstyleboard.SmartManagerDashBoardActivity",
                    "com.samsung.android.sm_cn/.mainui.ram.RamActivity",
                    "com.samsung.android.sm_cn/.app.dashboard.SmartManagerDashBoardActivity",
                    "com.samsung.android.sm/com.samsung.android.sm.mainui.ram.AutoRunActivity",
                    "com.samsung.android.sm/com.samsung.android.sm.mainui.appmanagement.AppManagementActivity",
                    "com.samsung.android.sm/com.samsung.android.sm.mainui.cstyleboard.SmartManagerDashBoardActivity",
                    "com.samsung.android.sm/.mainui.ram.RamActivity",
                    "com.samsung.android.sm/.app.dashboard.SmartManagerDashBoardActivity",
                    "com.samsung.android.lool/com.samsung.android.sm.mainui.battery.BatteryActivity",
                    "com.samsung.android.sm_cn",
                    "com.samsung.android.sm"))
                put("HUAWEI", listOf(
                    "com.huawei.systemmanager/.startupmgr.mainui.StartupNormalAppListActivity",  //EMUI9.1.0(方舟,9.0)
                    "com.huawei.systemmanager/.appcontrol.activity.StartupAppControlActivity",
                    "com.huawei.systemmanager/.optimize.process.ProtectActivity",
                    "com.huawei.systemmanager/.optimize.bootstart.BootStartActivity",
                    "com.huawei.systemmanager"))
                put("vivo", listOf(
                    "com.iqoo.secure/.mainui.phoneoptimize.BgStartUpManager",
                    "com.iqoo.secure/.safeguard.PurviewTabActivity",
                    "com.vivo.permissionmanager/.activity.BgStartUpManagerActivity",
                    "com.iqoo.secure",
                    "com.vivo.permissionmanager"))
                put("Meizu", listOf(
                    "com.meizu.safe/.permission.SmartBGActivity",
                    "com.meizu.safe/.permission.PermissionMainActivity",
                    "com.meizu.safe"))
                put("OPPO", listOf(
                    "com.coloros.safecenter/.startupapp.StartupAppListActivity",
                    "com.coloros.safecenter/.permission.startup.StartupAppListActivity",
                    "com.oppo.safe/.permission.startup.StartupAppListActivity",
                    "com.coloros.oppoguardelf/com.coloros.powermanager.fuelgaue.PowerUsageModelActivity",
                    "com.coloros.safecenter/com.coloros.privacypermissionsentry.PermissionTopActivity",
                    "com.coloros.safecenter",
                    "com.oppo.safe",
                    "com.coloros.oppoguardelf"))
                put("oneplus", listOf(
                    "com.oneplus.security/.chainlaunch.view.ChainLaunchAppListActivity",
                    "com.oneplus.security"
                ))
                put("letv", listOf(
                    "com.letv.android.letvsafe/.AutobootManageActivity",
                    "com.letv.android.letvsafe/.BackgroundAppManageActivity",
                    "com.letv.android.letvsafe"))
                put("smartisanos", listOf(
                    "com.smartisanos.security/.invokeHistory.InvokeHistoryActivity",
                    "com.smartisanos.security"))
                put("lenovo", listOf(
                    "com.lenovo.security/.purebackground.PureBackgroundActivity",
                    "com.lenovo.security"))
            }
        }

    fun jumptoAutoRunSetting(context: Context) {
        var contain = false
        val entries: Set<Map.Entry<String, List<String>>> = hashMap.entries
        for ((manufacturer, actCompatList) in entries) {
            if (Build.MANUFACTURER.equals(manufacturer, ignoreCase = true)) {
                for (act in actCompatList) {
                    try { var intent: Intent?
                        if (act.contains("/")) {
                            val componentName = ComponentName.unflattenFromString(act)
                            intent = Intent()
                            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                            intent.component = componentName
                        } else {
                            intent = context.packageManager.getLaunchIntentForPackage(act)
                        }
                        context.startActivity(intent)
                        contain = true
                        break
                    } catch (e: Exception) { }
                }
            }
        }
        if (!contain) {
            Toast.makeText(context, "设置失败，请手动设置自启动", Toast.LENGTH_SHORT).show()
            try { val intent = Intent()
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                intent.action = "android.settings.APPLICATION_DETAILS_SETTINGS"
                intent.data = Uri.fromParts("package", context.packageName, null)
                context.startActivity(intent)
            } catch (e: Exception) { val intent = Intent(Settings.ACTION_SETTINGS)
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                context.startActivity(intent)
            }
        }
    }
}