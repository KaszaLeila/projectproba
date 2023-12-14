[app]

# Title of your application
title = Speech Emotion Recognition

# Package name
package.name = speechemotionrecognition

# Package domain
package.domain = org.test

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application version
version = 0.1
osx.kivy_version = 2.1.0

# Application requirements
requirements = python3==3.7.6,hostpython3==3.7.6, kivy, pillow, https://github.com/kivy/python-for-android/archive/master.zip, pyaudio==0.2.15


# Supported orientations
orientation = portrait


osx.python_version = 3.7.6



# Android specific settings
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
# android.sdk = 31
android.ndk = 25b
android.ndk_version = 21.3.6528147
android.ndk_api = 21

# Permissions
android.permissions = RECORD_AUDIO,WRITE_EXTERNAL_STORAGE

# Python for android (p4a) settings
p4a.branch = master
p4a.source_dir =
p4a.local_recipes =

[buildozer]
buildozer.version = 1.2.0
# Log level
log_level = 2

# Display warning if run as root
warn_on_root = 1
