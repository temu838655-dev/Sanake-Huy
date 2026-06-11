[app]
title = Snake Game
package.name = snakegame
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Đã cập nhật lên Kivy 2.3.0 để tương thích với Android mới
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 1

# Đã nâng lên API 34 theo tiêu chuẩn Google Play và sửa lỗi biên dịch
android.api = 34
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a

android.ndk = 25b

log_level = 2
warn_on_root = 0
