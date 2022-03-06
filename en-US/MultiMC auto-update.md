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

That's the time when you'll have to download a new version of the MultiMC pack, because packwiz cannot edit the pack itself just yet.

### Can I ignore some of the mods?

There is no official procedure for this yet, but a [workaround by Remty5](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/81) which has been tested in Linux and will probably work in MacOS, but **not** in Windows. 

* First things first you have to install the scripts that will ignore the mods.. Open your file manager and select the folder you want to install the scripts that will ignore the mods you'll select (Suggested: the instance's folder). Then, right click within the folder and select "Open Terminal". If this option does not exist in your Mac, you could use [this](https://www.petenetlive.com/KB/Article/0001060) tutorial (or Google it 😅)

![Screenshot-1](https://user-images.githubusercontent.com/77157639/156615703-f113293c-e821-4c94-a891-2fccd0ff8848.png)

Now, inside the terminal paste the command below:

`curl -Os https://gist.githubusercontent.com/Remty5/1b8a8d7c842dda56dacebf6db8c10961/raw/c0149c39ef4be375d013fa254b71899fb4bd6105/post-exit.sh && curl -Os https://gist.githubusercontent.com/Remty5/1b8a8d7c842dda56dacebf6db8c10961/raw/c0149c39ef4be375d013fa254b71899fb4bd6105/pre-launch.sh`


If everything goes well, the scripts are installed!

Now there are 3 things remaining: 
  1. upgrade the checksums,
  2. actually select which mods you want to ignore,
  3. make them work in MultiMC

* Within the terminal, run another command:

  `cd .minecraft && md5sum packwiz.json`

  This will print "`randomnumber` - packwiz.json". Copy **only** the number.

* After this is done, open with a text editor the `pre-launch.sh` and on the 12th line where is says

  `checksum=101c3431ead01d42ffbc80fecdccf903` replace the big number with the number you copied previously.

   **NOTE:** You'll have to do this every time FO has an upgrade, otherwise the game will crash :(

* Now, head to line 20 of the same script

  Here, you have to copy the mods' names you want to ignore from your `mods` folder and add them in order, like it is shown in the script.
  After each mods' name add a `\`, except from the last one, otherwise it won't work.

* This is the final step! These scripts have to be run by MultiMC, and this is very simple:
  
  1) Open MultiMC, right click your auto-upgrade instance and click "Edit Instance"
  2) Go to Settings and click "Custom Commands" and enable them
  3) Here, add to the "Pre-launch command" `/path/to/pre-launch.sh` (replace `/path/to/` with the location you saved the scripts)
     and to the "Post-exit command" `/path/to/post-exit.sh` (replace `/path/to/` with the location you saved the scripts)

If you have any problems, you can ask for support in the [Discord server](https://discord.gg/yxaXtaQqdB). This tutorial was made by RaptaG.
