package com.herk.njtechlogin.login
import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.edit
import com.herk.njtechlogin.MainActivity
import com.herk.njtechlogin.util.NETCOMPANY
import com.herk.njtechlogin.util.PASSWORD
import com.herk.njtechlogin.util.USERNAME
import com.herk.njtechlogin.R
import com.herk.njtechlogin.databinding.ActivityLoginBinding


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
                saveLoginData()
                startActivity(Intent(this, MainActivity::class.java))
            }
        }
    }

    private fun loadLoginData():List<String> {
        val prefs    = getSharedPreferences(getString(R.string.prefs_login_data), 0)
        val username = prefs.getString(USERNAME, "")!!
        val password = prefs.getString(PASSWORD, "")!!
        val netCompany = prefs.getString(NETCOMPANY, "1")!!

        if (netCompany == "1") binding.cmccRbtn.isChecked = true else binding.teleRbtn.isChecked = true
        return listOf(username, password, netCompany)
    }

    private fun saveLoginData() {
        val dataName = getString(R.string.prefs_login_data)
        getSharedPreferences(dataName, 0).edit() {
            putString(USERNAME, binding.usernameEdit.text.toString())
            putString(PASSWORD, binding.passwordEdit.text.toString())
            if (binding.cmccRbtn.isChecked) putString(NETCOMPANY, "1") else putString(NETCOMPANY, "2")
        }
    }

}