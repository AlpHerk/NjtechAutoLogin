package alpherk.njtechlogin.util
import android.app.Activity

@Deprecated("")
object ActivityCollector {
    private val activities = ArrayList<Activity>()

    // 用于在ArrayList中添加Activity
    fun addActivity(activity: Activity){
        activities.add(activity)
    }

    // 用于在ArrayList中移除Activity
    fun removeActivity(activity: Activity){
        activities.remove(activity)
    }
    // 用于将存储在ArrayList的Activity全部移除
    fun finishAll() {
        for (activity in activities){
            if (!activity.isFinishing){
                activity.finish()
            }
        }
        activities.clear()
    }
}
