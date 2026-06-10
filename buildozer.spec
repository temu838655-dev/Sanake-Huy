[app]
android.accept_sdk_license = True
# (str) Title of your application
title = Snake Game

# (str) Package name
package.name = snakegame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test.snake

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# 'kivy' là bắt buộc. 'python3' giúp chạy trên nền tảng Python mới.
requirements = python3,kivy

# (str) Presplash of the application
# orientation = portrait (dọc) là phù hợp nhất với Window.size = (360, 640)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
