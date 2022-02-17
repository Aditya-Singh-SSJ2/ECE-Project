package com.example.MyApplicationpd;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import org.opencv.android.OpenCVLoader;

public class MainActivity extends AppCompatActivity {
  static{
      if(OpenCVLoader.initDebug()){
          Log.d("main activity","opencv loaded");
      }
      else{
          Log.d("main activit","not loaded");
      }
  }
    static {
        System.loadLibrary("native-lib");
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
