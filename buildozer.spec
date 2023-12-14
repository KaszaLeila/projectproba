[app]

# Alkalmazás neve
title = SimpleKivyApp

# Csomag neve
package.name = simplekivyapp

# Alkalmazás domainje
package.domain = org.test

# Forrásfájlok és könyvtárak
source.include_exts = py,png,jpg,kv,atlas

# Az alkalmazás verziószáma
version = 0.1

# Az alkalmazás forrásának könyvtára
source.dir = .

# Az alkalmazás forrásának belépési pontja (a python fájl neve)
source.include_exts = main.py

# Engedélyek a kamera használatához
android.permissions = INTERNET

# Forrásfájl az ikonhoz
source.icon.filename = icon.png

# SDL opciók
android.presplash.filename = %(source.dir)s/data/presplash.png
android.presplash.color = #000000
android.presplash.scale = True

# Kivy által használt modulok
requirements = python3,kivy

[buildozer]

# Kiadandó apk neve
name = simplekivyapp

# Kiválasztott eszköz
# hostpython3 kiválasztása a Cython fordításhoz
# cython = use Cython during compilation
# kivy = the Kivy version to use
# openssl = use a custom openssl version
# sqlite3 = use a custom sqlite3 version
# sdl2_image = use a custom sdl2_image version
# sdl2_mixer = use a custom sdl2_mixer version
# sdl2_ttf = use a custom sdl2_ttf version
# pygame = use a custom pygame version
# pyjnius = use a custom pyjnius version
# android = add platform here if you use android and need specific
#       requirements (recommended to not use anything else than
#       python2 or python3 android p4a)
# ios = add platform here if you use ios and need specific requirements
#       (always uses python2)

# p4a.source_dir = /path/to/your/p4a/source
# Egyéb könyvtárak és fájlok
include_exts = py,png,jpg,kv,atlas
