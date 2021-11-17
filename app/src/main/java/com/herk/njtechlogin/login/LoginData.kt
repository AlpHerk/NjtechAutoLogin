package com.herk.njtechlogin.login
import com.herk.njtechlogin.util.MyApp
import com.herk.njtechlogin.util.NETCOMPANY
import com.herk.njtechlogin.util.PASSWORD
import com.herk.njtechlogin.util.USERNAME
import com.herk.njtechlogin.R


class LoginData {
    private val dataName = MyApp.context.getString(R.string.prefs_login_data)
    private val prefs = MyApp.context.getSharedPreferences(dataName, 0)
    private val netCompany = prefs.getString(NETCOMPANY, "1")!!
    val username = prefs.getString(USERNAME, "")!!
    val password = prefs.getString(PASSWORD, "")!!

    fun postUserData(): List<String> {
        return listOf(username, password, netCompany)
    }
}

















