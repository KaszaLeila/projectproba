[app]

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma-separated, e.g., requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Application entry point (full path)
# main.py should be in the source code directory
source.include_exts = py,png,jpg,kv,atlas

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait, or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
# android.api = 27

# (int) Minimum API required
# android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 27

# (str) Android NDK version to use
# android.ndk = 17c

# (int) Android NDK API to use. This is the minimum API your code will need to run
# android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = 

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.renpy.android.PythonActivity

# (bool) Indicate whether the screen should stay on
# keep_screen_on = 1

# (str) How to minimize the app
# android.minimize = shrink
