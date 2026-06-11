[app]
title = Snake Game
package.name = snakegame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 1

# Cấu hình Android
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.gradle_version = 7.4
android.archs = arm64-v8a, armeabi-v7a

# [buildozer]
log_level = 2
warn_on_root = 1
# Thêm dòng này để tăng bộ nhớ cho quá trình build (tránh lỗi OOM)
buildozer.commands = -v
