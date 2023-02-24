package alpherk.njtechlogin.ui.login
import alpherk.njtechlogin.R
import alpherk.njtechlogin.ui.MainActivity
import alpherk.njtechlogin.databinding.ActivityLoginBinding
import alpherk.njtechlogin.ui.BaseActivity
import alpherk.njtechlogin.util.*
import android.annotation.SuppressLint
import android.content.Intent
import android.content.res.Configuration
import android.os.Bundle
import android.widget.Toast
import androidx.core.content.edit


class LoginActivity : BaseActivity() {
    private lateinit var binding: ActivityLoginBinding

    @SuppressLint("CommitPrefEdits", "ResourceType")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityLoginBinding.inflate(layoutInflater)
        binding.loginData = LoginData()
        setContentView(binding.root)
        loadLoginData()

        binding.loginBtn.setOnClickListener {
            if (binding.usernameEdit.text.toString() == "" || binding.passwordEdit.text.toString() == "") {
                Toast.makeText(this, "学号密码不能为空", Toast.LENGTH_SHORT).show()
            } else {
                startActivity(Intent(this, MainActivity::class.java))
            }
            saveLoginData()
        }
    }

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)
        setContentView(R.layout.activity_login)
    }

    /**
     * 登录页面：加载登录数据
     */
    private fun loadLoginData() {
        val netCompa  = LoginData().netCompa
        if (netCompa == "1") {
            binding.cmccRbtn.isChecked = true
        } else {
            binding.teleRbtn.isChecked = true
        }
    }

    /**
     * 登录页面：保存登录数据
     */
    private fun saveLoginData() {
        getSharedPreferences(USER_DATA, 0).edit() {
            putString(USERNAME, binding.usernameEdit.text.toString())
            putString(PASSWORD, binding.passwordEdit.text.toString())
            if (binding.cmccRbtn.isChecked)
                 putString(NETCOMPA, "1")
            else putString(NETCOMPA, "2")
        }
    }

}