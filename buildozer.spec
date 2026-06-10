[app]
title = Snake Game
package.name = snakegame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1

android.archs = arm64-v8a, armeabi-v7a
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
