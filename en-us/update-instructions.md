### CurseForge Launcher

If you haven't changed the mods:

1. Select _Minecraft_ from the grid or sidebar
1. On My Modpacks, right click _Fabulously Optimized_, then `⇄ Change Version`
   * Don't see that option? Follow the other instructions below.
1. Select the topmost version, then `Continue`.
1. Modpack will now update. 
1. After updating you can run it and check the version difference in the bottom right corner.

If you added or removed some mods:

1. Select _Minecraft_ from the grid or sidebar
1. On My Modpacks, click _Fabulously Optimized_
1. Click `⫶`
1. Click `Profile Options`
1. Uncheck "Allow content management for this profile". You can re-enable content management after the update.
1. Click `Continue`
1. Click `⫶`
1. Click `⇄ Change Version`. 
1. Select the topmost version, then `Continue`.
1. Modpack will now update. 
1. After updating you can run it and check the version difference in the bottom right corner.

### MultiMC
1.17 needs Java 16+, 1.18 needs Java 17+. [Get Java](https://www.oracle.com/java/technologies/downloads/)

1. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
1. Click `Download` on the latest **MultiMC version**
   * Don't see the MultiMC version? Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there. 
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
1. Drag the ZIP-archive to MultiMC window
1. Click that version, then `Minecraft Folder`
1. Click the previous version, then `Minecraft Folder`
1. Copy the important files and folders over:
   * `saves` for your local worlds
   * `resourcepacks`, if you use any (do not copy the _Mod Menu Helper_ though)
   * `screenshots`
   * `servers.dat` for your multiplayer servers
   * `options.txt`, if you want to keep your vanilla option changes
1. Close the folders and run the new version
1. If everything looks right, delete the old version

### MultiMC (auto-update)
1.17 needs Java 16+, 1.18 needs Java 17+. [Get Java](https://www.oracle.com/java/technologies/downloads/)

In most cases:
1. Run the existing version, wait for the progress bar to fill up
1. Check the version difference in the bottom right corner.

To update the Fabric Loader (if you get an error like "mod X needs fabric-loader x.y.z"):

1. Click the instance
1. Click `Edit Instance`
1. On Minecraft, select the Fabric Loader, click `Remove`
1. Click `Install Fabric`, click `OK`
1. `Close` the window, you can now play the game.

If there is a new Minecraft version or you are lazy to update your Fabric Loader:

1. Go to [readme](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads), click "Alternative downloads"
2. Click the version number you need in the MultiMC (auto-update) section  
1. Drag the ZIP-archive to MultiMC window
1. Click that version, then `Minecraft Folder`
1. Click the previous version, then `Minecraft Folder`
1. Copy the important files and folders over:
   * `saves` for your local worlds
   * `resourcepacks`, if you use any (do not copy the _Mod Menu Helper_ though)
   * `screenshots`
   * `servers.dat` for your multiplayer servers
   * `options.txt`, if you want to keep your vanilla option changes
1. Close the folders and run the new version
1. If everything looks right, delete the old version

### GDLauncher
1. Right click the _Fabulously Optimized_ instance
1. Select `🔧 Manage`
1. Select `Modpack` from the right
1. Click `Select a version` and choose the topmost option
1. Click `Switch Version`
1. Modpack will now update.
1. After updating you can run it and check the version difference in the bottom right corner.

### Minecraft Launcher (the vanilla)
Currently the only way to update is to "reinstall" the pack.

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.13.3**
1. Open Minecraft Launcher, click `Installations` and then click 📂 on the Fabric installation
1. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) on Curseforge
1. Click `Download` the latest **MultiMC version** of the pack
   * Don't see the MultiMC version? Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there. 
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
1. Open the zip file, go to _Fabulously Optimized x.x.x_ > _.minecraft_
1. Copy all folders from zip's .minecraft folder to your .minecraft folder; if asked - replace the files
2. If you want [FO default settings](./changed-options.md) as well, delete `options.txt` (your vanilla options will be reset)
3. Launch the installed Fabric profile
4. If you now see "Fabulously Optimized" in the right bottom corner and its version number is newer than before, you're done!

### Resetting settings

Because the pack is using YOSBR, your vanilla options and most of the mod ones will not change when you upgrade, [despite what is stated in the changelog](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md). 
This is made so that you can upgrade without having to reconfigure your options all the time. However, at some point you may still want to do that in order to get the latest changes. So:

1. Open the modpack folder.
   * CurseForge Launcher: right click on the modpack tile -> `Open Folder`
   * MultiMC: right click on the instance -> `Minecraft Folder`
   * GDLauncher: right click on the instance -> `Open Folder`
   * Vanilla launcher: go to `Installations` tab -> hover on the instance -> click `📁`
2. Delete `options.txt` if you prefer (these are vanilla options - [see what the modpack changes](./changed-options.md))
3. Open "config" and delete the following:
   * _fabric_ folder
   * _config.json5_ inside _slightguimodifications_
   * other files, except for 
        * _citresewn.json_
        * _fabric_loader_dependencies.json_
        * _yosbr_ folder
4. Launch the game and new options are applied.
