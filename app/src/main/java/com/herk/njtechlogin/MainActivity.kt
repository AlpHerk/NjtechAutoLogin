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
import com.herk.njtechlogin.ui.setting.SettingData

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
            if (SettingData().postData()[0]) startService(Intent(this, LoginGuardService::class.java))
        } else {
            startActivity(Intent(this, LoginActivity::class.java))
        }

        val navController = findNavController(R.id.nav_host_fragment_content_main)
        appBarConfig = AppBarConfiguration(setOf(R.id.nav_account, R.id.nav_setting, R.id.nav_info), binding.drawerLayout)
        setupActionBarWithNavController(navController, appBarConfig)
        binding.navView.setupWithNavController(navController)

    }


    @SuppressLint("SetTextI18n") // 首页侧滑栏菜单配置
    override fun onSupportNavigateUp(): Boolean {
        val netName: TextView = findViewById(R.id.netName)
        val studentID:TextView = findViewById(R.id.studentID)
        val prefs = getSharedPreferences("LOGIN_DATA",0)
        val username = prefs.getString("username", "")

        if (username != "") studentID.text = "学号: $username"
        else studentID.text = "点击进行登录或修改账号"
        netName.setOnClickListener {
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
            R.id.toolbar_setting -> Toast.makeText(this, "点击了设置，然鹅什么都没有，功能正在开发~", Toast.LENGTH_SHORT).show()
            R.id.toolbar_logout -> Toast.makeText(this, "点击了退出，然鹅什么都没发生，功能正在开发~", Toast.LENGTH_SHORT).show()
        }
        return super.onOptionsItemSelected(item)
    }


}