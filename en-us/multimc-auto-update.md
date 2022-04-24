# MultiMC auto-update

Here's a quick FAQ about the auto-updating MultiMC pack.

### What is it?

It is a normal MultiMC modpack that simply launches [packwiz](https://github.com/comp500/packwiz), a mod handling tool on every start. That means it will add and update any mods according to what I specify in the pack.toml file.

### How to install it?

The same way you would install any other MultiMC modpack - download the zip and drag to MultiMC window.

### How does it update?

It asks the server if the modpack has any updates _every time you launch it_. This means you do need internet or you'll get an error (though you can skip the error).

If there are any, they will be downloaded and launched, otherwise the current game will launch.

It does _not_ auto-update the individual mods outside of what is set in the the modpack. This is a common misconception and it could cause problems anyway.

### Why are you not distributing it in Curseforge?

* To keep it visible in files list, I'd have to reupload it every time I update the pack, which is often unnecessary.
* It may not actually [support the mod developers via downloads](https://support.curseforge.com/en/support/solutions/articles/9000197898-rewards-program-terms-of-service#1.-Description-of-Rewards-Program) so I'd prefer if only a limited amount of technical users use it.
* It is still somewhat experimental and may have unexpected issues or variances from the normal packs I distribute (Curseforge and MultiMC)

### So why did you make this at all?

* Because MultiMC doesn't have this yet, see their issues [#2640](https://github.com/MultiMC/MultiMC5/issues/2640) and [#3037](https://github.com/MultiMC/MultiMC5/issues/3057)
* Because the developer is planning to make an installer using the same system for the vanilla launcher as well, which I definitely want for FO
* Because it was suggested for this pack previously, where an user wanted to upgrade without needing to have a separate profile

### What happens if a new version of Minecraft is released?

You'll have to download a new version of the pack that is specific to that Minecraft version.

### Can I ignore some of the mods?

There is no official procedure for this yet, but RaptaG has made a tutorial and an improved version of the [Remty5's workaround](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/81). The user now only has to replace the instance parameters and list the mods that will be disabled. It has been confirmed to work on Linux, may also work for MacOS. Volunteers are free to port it to Windows as well.
 
**Steps:**

1. Open a terminal and run the command below:
   * Arch Linux: `sudo pacman -S jq --needed`
   * Debian-Ubuntu Linux: `sudo apt-get install jq`
   * Fedora Linux: `sudo dnf install jq`
   * openSUSE Linux: `sudo zypper install jq`
   * Other distros/macOS: [follow this tutorial](https://stedolan.github.io/jq/download/)

This will install a program called [jq](https://stedolan.github.io/jq/), needed for automatically adapting this script to any Minecraft version you use.

2. Download the mod disabling scripts:
   1. Open MultiMC, right click your instance and click "Instance Folder"
   2. Inside the folder right click and select "Open Terminal here"
       * On macOS, [follow this tutorial](https://www.petenetlive.com/KB/Article/0001060) to get that option
   3. Within the terminal, run the following command - this will install the files and make them executable:
```
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

**FAQ:**

What if I want to disable more or less than 6 mods?

* Removing: Just remove the extra rows from the start and end of `pre-launch.sh`, eg. from lines 10 & 11 `mod4=`, `mod5=` and `$mod4.jar\`, `$mod5.jar\` from lines 35 & 36, if you want to have 4 mods disabled.
* Adding: Press `Enter` in the end of line 11 and type `mod6=` for example. Then, in the end of line 36, press again `Enter` and type `$mod6.jar\`. Repeat the same for more mods by just changing the number (`mod6=` to `mod7=` and `$mod6.jar\` to `$mod7.jar\` etc.).

If you have any problems, you can ask for support in the [Discord server](https://discord.gg/yxaXtaQqdB). This tutorial was made by RaptaG.
