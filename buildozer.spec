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
requirements = python3,kivy==2.2.0

# ======================
# DISPLAY
# ======================
orientation = portrait
fullscreen = 1

# ======================
# ANDROID STABLE CONFIG
# ======================
android.api = 33
android.minapi = 21

android.archs = arm64-v8a,armeabi-v7a

# QUAN TRỌNG: tránh build-tools 37 lỗi AIDL
android.sdk = 33
android.build_tools_version = 33.0.2

# NDK ổn định cho kivy CI
android.ndk = 25b

# ======================
# DEBUG / BUILD
# ======================
log_level = 2
warn_on_root = 0