package com.herk.njtechlogin
import android.annotation.SuppressLint
import android.content.Intent
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
import com.herk.njtechlogin.databinding.MainNavDrawerBinding
import com.herk.njtechlogin.login.LoginActivity
import com.herk.njtechlogin.login.LoginData
import com.herk.njtechlogin.main.setting.SettingData
import com.herk.njtechlogin.main.setting.SettingFragment
import com.herk.njtechlogin.util.LOGIN_FILE
import com.herk.njtechlogin.util.USERNAME
import kotlin.system.exitProcess

class MainActivity : AppCompatActivity() {

    private lateinit var binding: MainNavDrawerBinding
    private lateinit var appBarConfig: AppBarConfiguration

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = MainNavDrawerBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.appBarMain.toolbar)

        val (username, password) = LoginData().postUserData()
        if (username != "" && password != "") {
            startService(Intent(this, LoginService::class.java))
        } else {
            startActivity(Intent(this, LoginActivity::class.java))
        }
        if (SettingData().isGardNet) {
            startService(Intent(this, GuardService::class.java))
        }

        val navController = findNavController(R.id.nav_host_fragment_content_main)
        val menuset = setOf(R.id.nav_account, R.id.nav_setting, R.id.nav_info)
        appBarConfig = AppBarConfiguration(menuset, binding.drawerLayout)
        setupActionBarWithNavController(navController, appBarConfig)
        binding.navView.setupWithNavController(navController)
    }
    @SuppressLint("SetTextI18n") // 首页侧滑栏菜单配置
    override fun onSupportNavigateUp(): Boolean {
        val studnName: TextView = findViewById(R.id.netName)
        val studentID: TextView = findViewById(R.id.studentID)
        val prefs = getSharedPreferences(LOGIN_FILE,0)
        val username = prefs.getString(USERNAME, "")

        if (username == "")
             studentID.text = "点击登录或修改账号"
        else studentID.text = "学号: $username"

        studnName.setOnClickListener {
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
            R.id.toolbar_logout -> exitProcess(0)
        }
        return super.onOptionsItemSelected(item)
    }

    private fun jumptoSettingFragment(){
        supportFragmentManager
            .beginTransaction()
            .replace(R.id.nav_host_fragment_content_main, SettingFragment())
            .commit()
        Toast.makeText(this,"BUG：嘿，页面重叠，有空再改", Toast.LENGTH_SHORT).show()
    }

}