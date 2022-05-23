<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">MyAndroidApp</string>
    <string name="lblPassword">peler :</string>
    <string name="btn_submit">Submit</string>
</resources>

=========================================

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical" >

    <TextView
        android:id="@+id/lblPassword"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/lblPassword"
        android:textAppearance="?android:attr/textAppearanceLarge" />

    <EditText
        android:id="@+id/txtPassword"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:inputType="textPassword" >

        <requestFocus />
    </EditText>

    <Button
        android:id="@+id/btnSubmit"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/btn_submit" />

</LinearLayout>

