import os
import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView

class TajweedQuestApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TajweedQuest Mobile Preview")
        self.resize(450, 800)  # Mobile view dimension

        # Create embedded browser view
        self.browser = QWebEngineView()
        
        # Enable Local Storage (saves your XP/Hearts progress)
        profile = QWebEngineProfile.defaultProfile()
        profile.setPersistentStoragePath(os.path.abspath("./storage"))

        # --- FIX: Dynamically find the folder where main.py sits ---
        script_dir = os.path.dirname(os.path.abspath(__file__))
        html_filename = "Tajweed_quest_full_20260523_6mdqn9k67.html"
        html_path = os.path.join(script_dir, html_filename)
        
        # Double check if the file is truly there to prevent crashes
        if not os.path.exists(html_path):
            print(f"Error: Could not find '{html_filename}' in folder: {script_dir}")
            print("Please make sure the HTML file is placed in the exact same folder as main.py!")
            sys.exit(1)

        # Load the HTML file directly into the app window
        self.browser.setUrl(QUrl.fromLocalFile(html_path))
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TajweedQuestApp()
    window.show()
    sys.exit(app.exec())