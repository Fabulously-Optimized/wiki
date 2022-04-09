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

 I (RaptaG) made an better version of [Remty5's workaround](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/81) which is more automatical and the only thing need to be added by the user is the mods that will be disabled. It still works on Linux, testers are needed for MacOS and for Windows, anyone willing to port it should do so.
 
 **Steps:**
 
 1. Installing jq
 2. Dowloading the script
 3. Selecting the mods that you want to disable
 4. Setting the scripts as pre-launch and post-exit commands in the MultiMC instance

----------------------------------------------------------------------------------------------------------------------------------------------------------

1) Enter [this](https://stedolan.github.io/jq/download/) website and install `jq`, according to your OS. It is needed for an important part of the script (the Mincraft version for Packwiz) Don't worry about the its size, it is very lightweight!

2) Inside a teminal run the following command:

`curl -Os https://raw.githubusercontent.com/RaptaG/fabulously-optimized/main/Packwiz/pre-launch.sh | curl -Os https://raw.githubusercontent.com/RaptaG/fabulously-optimized/main/Packwiz/post-exit.sh && chmod 755 pre-launch.sh post-exit.sh`

You can install them wherever you like, just make sure to enter this place before, by running `cd /path/to/folder` (replace `/path/to/folder` with the folder's location).

This will install the files and make them executable

3) 
- Copy the name of the mod(s) you want to disable
- Open `pre-launch.sh` with a text editor (the choise is yours!).
- You'll see in the beggining of it saying "Select the mods you wish to disable:" and below it `mod0=`, `mod1=`, `mod3=`, `mod4=` and `mod5=`.
  After `=` place the name of the mods you previously copied, one by one.
  
  **IMPORTANT:** Whatever you select, **never** remove `mod0=` and `$mod0.jar`

4)  
- Open MultiMC
- Click on your instance "Edit Instance"
- Go to "Settings" and then to "Custom Commands"
- Remove the pre-launch command and replace it with `/path/to/folder/pre-launch.sh` (again, replace `/path/to/folder` with the folder where you              installed the scripts
- Do the same thing for the post-exit command but with `path/to/folder/post-exit.sh` this time.


That's it! Now, the mods you disabled shouldn't work neither appear inside the mod's menu!


**FAQ:**

What if I want more-less than 6 mods to disable?


The answer is quite simple!

Removing: Just remove from the beggining of `pre-launch.sh` the extra mods you don't want (eg. `mod4=`, `mod5=` etc.) and then head to the end of the script where you'll see the extra mods too (`$mod4.jar\`, `$mod5.jar\` etc.).

Adding: What you have to do here is: Add more definitions after `mod5=` (eg. `mod6=`, `mod7=` etc.). Then, near the end of the script, on line 36 copy `mod5.jar\`, press enter after `mod5.jar\`, paste what you copied and replace `5` with the number of the extra mod ( `6`, `7` etc.).

If you have any problems, you can ask for support in the [Discord server](https://discord.gg/yxaXtaQqdB). This tutorial was made by RaptaG.
