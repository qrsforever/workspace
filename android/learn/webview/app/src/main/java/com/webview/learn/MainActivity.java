package com.webview.learn;

import android.graphics.Bitmap;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.KeyEvent;
import android.view.MotionEvent;
import android.view.ViewGroup;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebSettings.RenderPriority;
import android.widget.TextView;
import android.util.Log;
import android.app.Instrumentation;
import android.os.SystemClock;


public class MainActivity extends AppCompatActivity {
    public static final String TAG = MainActivity.class.getSimpleName();
    WebView mWebview;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mWebview = (WebView) findViewById(R.id.webView);

        mWebview.getSettings().setBuiltInZoomControls(false);
        mWebview.getSettings().setJavaScriptEnabled(true);
        mWebview.getSettings().setRenderPriority(RenderPriority.HIGH);
        mWebview.getSettings().setBlockNetworkImage(true);
        mWebview.getSettings().setJavaScriptCanOpenWindowsAutomatically(true);
        mWebview.getSettings().setAllowFileAccess(true);
        mWebview.getSettings().setAppCacheEnabled(true);
        mWebview.getSettings().setSaveFormData(false);
        mWebview.getSettings().setLoadsImagesAutomatically(true);

        mWebview.loadUrl("http://10.58.82.240:4000/");

        mWebview.setWebViewClient(new WebViewClient() {
            //直接显示在当前Webview
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                Log.d(TAG, "shouldOverrideUrlLoading: " + url);
                view.loadUrl(url);
                return true;
            }

            //设置加载前的函数
            @Override
            public void onPageStarted(WebView view, String url, Bitmap favicon) {
                Log.d(TAG, "onPageStarted :" + url);
                super.onPageStarted(view, url, favicon);
            }

            //设置结束加载函数
            @Override
            public void onPageFinished(WebView view, String url) {
                Log.d(TAG, "onPageFinished :" + url);
                super.onPageFinished(view, url);
            };
        });

        //设置WebChromeClient类
        mWebview.setWebChromeClient(new WebChromeClient() {
            //获取网站标题
            @Override
            public void onReceivedTitle(WebView view, String title) {
                Log.d(TAG, "onReceivedTitle:" + title);
            }

            //获取加载进度
            @Override
            public void onProgressChanged(WebView view, int newProgress) {
                Log.d(TAG, "onProgressChanged :" + newProgress);
            }
        });
    }

    //销毁Webview
    @Override
    protected void onDestroy() {
        if (mWebview != null) {
            mWebview.loadDataWithBaseURL(null, "", "text/html", "utf-8", null);
            mWebview.clearHistory();

            ((ViewGroup) mWebview.getParent()).removeView(mWebview);
            mWebview.destroy();
            mWebview = null;
        }
        super.onDestroy();
    }
}
