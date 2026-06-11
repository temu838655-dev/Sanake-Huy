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

android.arch = arm64-v8a
android.minapi = 21
android.ndk = 25.2.9519653

[buildozer]
log_level = 2
warn_on_root = 1