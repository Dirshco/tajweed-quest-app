import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Simple safe platform detection
try:
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    ON_ANDROID = True
except ImportError:
    ON_ANDROID = False

class TajweedQuestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Point to your exact file name
        self.html_filename = "Tajweed_quest_full_20260523_6mdqn9k67.html"
        
        if ON_ANDROID:
            self.start_android_webview()
        else:
            print("Running on desktop/simulation runner setup.")
            
        return layout

    def start_android_webview(self):
        @run_on_ui_thread
        def launch():
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            
            activity = PythonActivity.mActivity
            webview = WebView(activity)
            webview.getSettings().setJavaScriptEnabled(True)
            webview.getSettings().setDomStorageEnabled(True)
            webview.getSettings().setAllowFileAccess(True)
            
            webview.setWebViewClient(WebViewClient())
            activity.setContentView(webview)
            
            # This loads the file from your compiled APK assets folder
            webview.loadUrl(f"file:///android_asset/{self.html_filename}")
        launch()

if __name__ == '__main__':
    TajweedQuestApp().run()
