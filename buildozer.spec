[app]
title = Snake Game
package.name = snakegame
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# QUAN TRỌNG: dùng kivy ổn định hơn cho build CI
requirements = python3,kivy==2.2.0

orientation = portrait
fullscreen = 1

# ======================
# ANDROID CONFIG FIXED
# ======================

android.api = 35
android.minapi = 21
android.sdk = 35
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

# bắt buộc cho CI
android.accept_sdk_license = True

# KHÔNG dùng gradle_version thủ công (rất dễ lỗi CI)
# android.gradle_version = 7.4  ❌ XÓA DÒNG NÀY

# ======================
# BUILD SYSTEM
# ======================

[buildozer]
log_level = 2
warn_on_root = 0