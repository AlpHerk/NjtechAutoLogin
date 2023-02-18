package alpherk.njtechlogin
import alpherk.njtechlogin.receiver.ScreenReceiver
import alpherk.njtechlogin.databinding.MainNavDrawerBinding
import alpherk.njtechlogin.service.AuthenOffService
import alpherk.njtechlogin.service.AuthenService
import alpherk.njtechlogin.service.GuardService
import alpherk.njtechlogin.ui.login.LoginActivity
import alpherk.njtechlogin.ui.login.LoginData
import alpherk.njtechlogin.ui.setting.SettingData
import alpherk.njtechlogin.util.*
import android.annotation.SuppressLint
import android.content.Intent
import android.content.IntentFilter
import android.net.Uri
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.navigateUp
import androidx.navigation.ui.setupActionBarWithNavController
import androidx.navigation.ui.setupWithNavController
import com.google.android.material.snackbar.Snackbar
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlin.system.exitProcess

class MainActivity : AppCompatActivity() {

    private lateinit var binding: MainNavDrawerBinding
    private lateinit var appBarConfig: AppBarConfiguration
    private lateinit var screenReceiver: ScreenReceiver

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = MainNavDrawerBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.appBarMain.toolbar)

        val (username, password) = LoginData().postUserData()
        if (username == "" || password == "") {
//            fistTimeDialog()
            startActivity(Intent(this, LoginActivity::class.java))
        } else {
            startService(Intent(this, AuthenService::class.java))
        }

        if (SettingData().isGardNet) {
            startService(Intent(this, GuardService::class.java))
        }

        val navController = findNavController(R.id.nav_host_fragment_content_main)
        val menuset = setOf(R.id.nav_account, R.id.nav_setting, R.id.nav_info)
        appBarConfig = AppBarConfiguration(menuset, binding.drawerLayout)
        setupActionBarWithNavController(navController, appBarConfig)
        binding.navView.setupWithNavController(navController)



        val filter = IntentFilter()
        filter.addAction(Intent.ACTION_SCREEN_ON)   // 注册解锁屏幕广播
//        filter.addAction(WifiManager.NETWORK_STATE_CHANGED_ACTION);
//        filter.addAction(WifiManager.WIFI_STATE_CHANGED_ACTION);
//        val netReceiver = NetReceiver()
//        registerReceiver(netReceiver, filter)
        val screenReceiver = ScreenReceiver()
        registerReceiver(screenReceiver, filter)

        checkUpdateHome()


    }

    override fun onDestroy() {
        super.onDestroy()
        unregisterReceiver(screenReceiver)
    }



    @SuppressLint("SetTextI18n") // 首页侧滑栏菜单配置
    override fun onSupportNavigateUp(): Boolean {
        val stunName : TextView = findViewById(R.id.netName)
        val studentID: TextView = findViewById(R.id.studentID)
        val prefs = getSharedPreferences(LOGIN_FILE,0)
        val username = prefs.getString(USERNAME, "")

        if (username == "")
             studentID.text = "点击登录或修改账号"
        else studentID.text = "学号: $username"

        stunName.setOnClickListener {
            startActivity(Intent(this, LoginActivity::class.java))
        }
        studentID.setOnClickListener {
            startActivity(Intent(this, LoginActivity::class.java))
        }
        val navController = findNavController(R.id.nav_host_fragment_content_main)

        return navController.navigateUp(appBarConfig) || super.onSupportNavigateUp()
    }


    // 标题栏的 toolbar 菜单设置
    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.toolbar, menu)
        return true
    }
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.toolbar_setting -> Toast.makeText(this,"跳转失败，请从侧滑栏打开设置", Toast.LENGTH_SHORT).show()
            R.id.toolbar_logout_net -> startService(Intent(this, AuthenOffService::class.java))
            R.id.toolbar_logout -> exitProcess(0)
        }
        return super.onOptionsItemSelected(item)
    }
//    private fun jumptoSettingFragment(){
//        supportFragmentManager
//            .beginTransaction()
//            .replace(R.id.nav_host_fragment_content_main, SettingFragment())
//            .commit()
//        Toast.makeText(this,"BUG：嘿，页面重叠，有空再改", Toast.LENGTH_SHORT).show()
//    }

    private val job = Job()
    private val scope = CoroutineScope(job)
    private fun checkUpdateHome() {
        scope.launch {
            val downUrl = Update().checkUpdate()
            if (downUrl != null) {
                Snackbar.make(binding.root, "检测到有新版本", 30000)
                    .setAction("下载") {
                        val uri = Uri.parse(downUrl)
                        startActivity(Intent(Intent.ACTION_VIEW, uri))
                    }
                    .show()
            }
        }
    }

//    private fun fistTimeDialog() {
//        AlertDialog.Builder(this).apply {
//            setTitle("使用说明")
//            setMessage("shuoming")
//            setCancelable(false)
//            setPositiveButton("确认") {
//                dialog, which ->
//            }
//            setNegativeButton("退出") {
//                dialog, which -> exitProcess(0)
//            }
//            show()
//        }
//    }

}