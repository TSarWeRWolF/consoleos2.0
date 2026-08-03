hello this version im give new funktion and give new games and give googl chrome b im make start port monile games 

emulator -avd ConsoleOS_Minecraft_New

Wait for Android to load, then check:

adb devices

You should see something like:

List of devices attached
emulator-5554 device

Check that it's Android 9:

adb shell getprop ro.build.version.release

Should show:

9

And the architecture:

adb shell getprop ro.product.cpu.abi

Should show:

x86_64

If an old emulator is already running and interfering, close it:

adb emu kill

Or find processes:

ps aux | grep emulator

And then again:

emulator -avd ConsoleOS_Minecraft_New



View installed AVDs:
avdmanager list avd

Shows what has been created:

Name: ConsoleOS_Minecraft
Target: Android 4.4
ABI: x86
View installed Android SDK packages:
sdkmanager --list

You can filter to only installed ones:

sdkmanager --list | grep "Installed"
View the Android version inside the running emulator:

First:

adb devices

Then:

adb shell getprop ro.build.version.release

For example:

4.4.2

API level:

adb shell getprop ro.build.version.sdk

For example:

19
View the emulator architecture:
adb shell getprop ro.product.cpu.abi

The result may be:

x86

or:

x86_64

or:

armeabi-v7a

If you're talking about which Minecraft APK is installed, then:

adb shell pm list packages | grep -i minecraft

And information about it:

adb shell dumpsys package com.mojang.minecraftpe

By the way, you already had:

package:com.mojang.minecraftpe

So Minecraft is installed in the emulator.



in future im create wery big funcktion 
