# MultiMC

{% tabs %}
{% tab title="Default - added mod | Default - modpack mod | Auto-update - added mod" %}

1. Open MultiMC
2. Click on Fabulously Optimized, then `Edit Instance`
3. Go to `Loader mods`
4. Find the mod you need, uncheck the checkbox.

{% endtab %}

{% tab title="Auto-update - modpack mod" %}

{% hint style="info" %}
The tool downloads missing mods back on launch, therefore you need to make a custom script. Consider [switching to Prism Launcher instead](install-instructions/prism-launcher.md), which allows disabling mods with just a click.
{% endhint %}

{% tabs %}
{% tab title="Windows" %}

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

{% endtab %}
{% tab title="macOS/Linux" %}

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

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Don't disable anything that says "API", because other mods need those to work.
{% endhint %}

#### What if I want to disable more or less than 6 mods?

* Removing: Just remove the extra rows from the start and end of `pre-launch.sh`, eg. from lines 10 & 11 `mod4=`, `mod5=` and `$mod4.jar\`, `$mod5.jar\` from lines 35 & 36, if you want to have 4 mods disabled.
* Adding: Press `Enter` in the end of line 11 and type `mod6=` for example. Then, in the end of line 36, press again `Enter` and type `$mod6.jar\`. Repeat the same for more mods by just changing the number (`mod6=` to `mod7=` and `$mod6.jar\` to `$mod7.jar\` etc.).

{% endtab %}

{% endtabs %}