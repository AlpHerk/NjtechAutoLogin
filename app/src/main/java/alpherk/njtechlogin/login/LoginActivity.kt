package alpherk.njtechlogin.login
import alpherk.njtechlogin.MainActivity
import alpherk.njtechlogin.databinding.ActivityLoginBinding
import alpherk.njtechlogin.util.LOGIN_FILE
import alpherk.njtechlogin.util.NETCOMPA
import alpherk.njtechlogin.util.PASSWORD
import alpherk.njtechlogin.util.USERNAME
import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.edit


class LoginActivity : AppCompatActivity() {
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

    private fun loadLoginData() {
        val netCompa  = LoginData().netCompa
        if (netCompa == "1") {
            binding.cmccRbtn.isChecked = true
        } else {
            binding.teleRbtn.isChecked = true
        }
    }
    private fun saveLoginData() {
        getSharedPreferences(LOGIN_FILE, 0).edit() {
            putString(USERNAME, binding.usernameEdit.text.toString())
            putString(PASSWORD, binding.passwordEdit.text.toString())
            if (binding.cmccRbtn.isChecked)
                 putString(NETCOMPA, "1")
            else putString(NETCOMPA, "2")
        }
    }

}