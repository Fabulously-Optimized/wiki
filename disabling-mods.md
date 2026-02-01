# Disabling mods

Don't like a feature or having a mod conflict? Easiest way to resolve it is to disable the mod. For resource pack-related issues, [see this page](resource-pack-issues.md).

Notes:

* You can also delete the mod(s), but that will make it harder to [use them later](adding-more-mods.md), unless you remember the mod's name exactly.
* Don't disable anything that says "API", other mods need it to work.

### Mod Menu

1. With the game open, click `Mods`
2. Scroll down to the specific mod you want to disable, note the third row with the ⚒️ (tools) or ✏️ (pencil) icon 
   * If the icon is **blue** and the text mentions **"Toggle mod"**, click the config button ![config](https://i.ibb.co/j35cBtn/image.png) and find the setting that disables the mod
   * If the icon is **blue and the text says something else**, click the config button ![config](https://i.ibb.co/j35cBtn/image.png) and see if you can disable the specific feature you need
   * If the icon is **gray** and there is no config button, or you know you added the mod yourself, follow your launcher-specific instructions below
   * If you **don't see any icons** and you didn't add the mod yourself, you don't have the Mod Menu Helper resource pack enabled for some reason.
     1. For the latter, click `Done` → `Options...` → `Resource Packs...` → `⏵` on "Mod Menu Helper.zip" → `Done` → go to point 1 of this tutorial

### CurseForge App

1. Open CurseForge App
2. Go to `My Modpacks`, click on Fabulously Optimized
3. Click on the three dots, select `Profile Options`
4. Check "Allow content management for this profile", click `Done`
5. Find the mod you need, toggle the knob.

### Modrinth App

1. Open Modrinth App
2. Open `|||\` "Library"
3. Click on Fabulously Optimized
4. Find the mod you need, toggle the knob.

### Prism Launcher

1. Open Prism Launcher
2. Click on Fabulously Optimized, then `Edit`
3. Go to `Mods`
4. Find the mod you need, uncheck the checkbox.

### MultiMC

1. Open MultiMC
2. Click on Fabulously Optimized, then `Edit Instance`
3. Go to `Loader mods`
4. Find the mod you need, uncheck the checkbox.

### MultiMC (auto-update)

{% hint style="info" %}
There is no _easy_ way to disable mods because the tool downloads missing mods back on launch. Consider [switching to Prism Launcher instead](install-instructions.md#prism-launcher), which also has a seamless modpack updater.
{% endhint %}

You need to create a custom script to disable mods. See instructions by platform below.

<details>
  <summary>Windows instructions</summary>

{% hint style="warning" %}
These instructions are here as-is to be used at your own risk, no support is provided.
{% endhint %}

1. Download the mod disabling scripts:
     1. Open MultiMC, right click your instance and click "Instance Folder"
     2. Inside the folder, shift-right click and select Open in Terminal (or equivalent PowerShell prompt)
     3. Within the terminal, run the following commands to download the files.
```
(Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/pre-launch.ps1" -OutFile "pre-launch.ps1")
(Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/post-exit.ps1" -OutFile "post-exit.ps1")
```
   If you wish to install them somewhere else, run `cd path\to\folder` (where `path\to\folder` is the path to your folder's location) before running the command above.

2. Select the mods to disable.
    1. Copy the name of the mod(s) you want to disable.
    2. Open `pre-launch.ps1` with any text editor
    3. On line 4, double click `mod1` and paste the name of the mod you previously copied. You can do this on line 5 too! If you want to disable more mods, copy all of line 5, press the `Enter` key at the end of line 5 and hit paste. (Make sure to change the name to match the new mod, though!)
        * Mod names may change with modpack updates so you'll need to update them here again.
  
3. Setup the scripts to run on your MultiMC (auto-update) instance  
   1. Open MultiMC
   2. Click on your instance "Edit Instance"
   3. Go to "Settings" and then to "Custom Commands"
   4. Remove the pre-launch command and replace it with `powershell -ExecutionPolicy Bypass -File ..\pre-launch.ps1`
       * If you've installed it elsewhere, use `path\to\folder\pre-launch.ps1` (where `path\to\folder` is the path to the folder)
   5. Do the same thing for the post-exit command but with `powershell -ExecutionPolicy Bypass -File ..\post-exit.ps1` this time.
       * Or `path\to\folder\post-exit.ps1` (where `path\to\folder` is the path to the folder)
4. That's it! Now, the mods you disabled will not run with the instance nor appear inside Mod Menu!

_Tutorial and scripts are made by [Ultrasonic1209](https://github.com/Ultrasonic1209) based on [Remty5's workaround](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/81)._

</details>

<details>
  <summary>Linux, macOS instructions</summary>

{% hint style="warning" %}
Not fully tested on macOS. These instructions are here as-is to be used at your own risk, no support is provided.
{% endhint %}

1. Open a terminal and run the command below:
   * Debian-Ubuntu Linux: `sudo apt-get install jq`
   * Fedora Linux: `sudo dnf install jq`
   * openSUSE Linux: `sudo zypper install jq`
   * Arch Linux: `sudo pacman -S jq --needed`
   * Other distros/macOS: [follow this tutorial](https://stedolan.github.io/jq/download/)

This will install a program called [jq](https://stedolan.github.io/jq/), needed for automatically adapting this script to any Minecraft version you use.

2. Download the mod disabling scripts:
   1. Open MultiMC, right click your instance and click "Instance Folder"
   2. Inside the folder right click and select "Open Terminal here"
       * On macOS, [follow this tutorial](https://www.petenetlive.com/KB/Article/0001060) to get that option
   3. Within the terminal, run the following command - this will install the files and make them executable:
```shell
curl -Os https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/pre-launch.sh | curl -Os https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/post-exit.sh && chmod +x pre-launch.sh post-exit.sh
```
   If you want to install them somewhere else, run `cd /path/to/folder` (where `/path/to/folder` is the path to your folder's location) before running the command above.

3. Select the mods to disable
   1. Copy the name of the mod(s) you want to disable
   2. Open `pre-launch.sh` with any text editor
   3. Find the line saying "Select the mods you wish to disable:" and below it `mod0=`, `mod1=`, `mod2=`,`mod3=`, `mod4=` and `mod5=`. 
      After `=` place the name of the mods you previously copied, one by one.
      * No matter how many mods you disable, **never** remove `mod0=` and `$mod0.jar`. 
      * Mod names may change with modpack updates so you'll need to update them here again.

4. Setup the scripts to run on your MultiMC (auto-update) instance  
   1. Open MultiMC
   2. Click on your instance "Edit Instance"
   3. Go to "Settings" and then to "Custom Commands"
   4. Remove the pre-launch command and replace it with `../pre-launch.sh`
       * If you've installed it elsewhere, use `/path/to/folder/pre-launch.sh` (where `/path/to/folder` is the path to the folder)
   5. Do the same thing for the post-exit command but with `../post-exit.sh` this time.
       * Or `path/to/folder/post-exit.sh` (where `/path/to/folder` is the path to the folder)
5. That's it! Now, the mods you disabled will not run with the instance nor appear inside Mod Menu!

_Tutorial and scripts made by [RaptaG](https://github.com/RaptaG) based on [Remty5's workaround](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/81)._

#### What if I want to disable more or less than 6 mods?

* Removing: Just remove the extra rows from the start and end of `pre-launch.sh`, eg. from lines 10 & 11 `mod4=`, `mod5=` and `$mod4.jar\`, `$mod5.jar\` from lines 35 & 36, if you want to have 4 mods disabled.
* Adding: Press `Enter` in the end of line 11 and type `mod6=` for example. Then, in the end of line 36, press again `Enter` and type `$mod6.jar\`. Repeat the same for more mods by just changing the number (`mod6=` to `mod7=` and `$mod6.jar\` to `$mod7.jar\` etc.).

</details>

### Minecraft Launcher (vanilla)

1. Open Minecraft Launcher, click on `Installations`
2. Hover on the Fabric installation, click 📂
3. Click `mods`
4. Rename the specific mod from "modname.jar" to "modname.jar.disabled"
   * Don't see ".jar" at the end of the name? [See this page for help.](https://www.thewindowsclub.com/show-file-extensions-in-windows)
   * Rename ".jar.disabled" back to ".jar" to use the mod again.

### GDLauncher

No longer supported. [Please migrate to Prism Launcher.](install-instructions.md#gdlauncher)
