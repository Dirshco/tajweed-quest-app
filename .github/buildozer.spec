[app]
title = TajweedQuest
package.name = tajweedquest
package.domain = org.learning

# Source code files to include
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,css

version = 1.0.0
requirements = python3,kivy,pyjnius

# UI Orientation
orientation = portrait

# Android specific configurations
osx.kivy_version = 2.3.1
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
