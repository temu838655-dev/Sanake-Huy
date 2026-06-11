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

android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25c
android.build_tools_version = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 1