[app]

# (str) Title of your application
title = Bigganify

# (str) Package name
package.name = bigganify

# (str) Package domain (needed for android packaging)
package.domain = org.bigganify

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) List of directory to exclude
source.exclude_dirs = tests, bin, venv, .git, .github

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) If True, skip updating SDK
android.skip_update = False

#
# Buildozer section
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
