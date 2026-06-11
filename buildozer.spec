[app]
title = Snake Game
package.name = snakegame
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# ======================
# REQUIREMENTS
# ======================
requirements = python3,kivy

orientation = portrait
fullscreen = 1

# ======================
# ANDROID CONFIG (STABLE)
# ======================

android.api = 33
android.minapi = 21

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license = True

# NDK nên để buildozer tự chọn hoặc set nhẹ
android.ndk = 23b

# ======================
# BUILD SYSTEM
# ======================

[buildozer]
log_level = 2
warn_on_root = 0