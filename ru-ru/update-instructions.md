# Update instructions

Please __do not upgrade from stable to alpha/beta__, use a separate instance. Any downgrades are also not supported.

### CurseForge Launcher

If you haven't changed the mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, right click _Fabulously Optimized_, then `⇄ Change Version`
   * Don't see that option? Follow the other instructions below.
3. Select the topmost version, then `Continue`.
4. Modpack will now update.
5. After updating you can run it and check the version difference in the bottom right corner.

If you added or removed some mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, click _Fabulously Optimized_
3. Click `⫶`
4. Click `Profile Options`
5. Uncheck "Allow content management for this profile". You can re-enable content management after the update.
6. Click `Continue`
7. Click `⫶`
8. Click `⇄ Change Version`.
9. Select the topmost version, then `Continue`.
10. Modpack will now update.
11. After updating you can run it and check the version difference in the bottom right corner.

### MultiMC

1.17 needs Java 16+, 1.18 needs Java 17+. [Get Java](https://www.oracle.com/java/technologies/downloads/)

1. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Click `Download` on the latest **MultiMC version**
   * Don't see the MultiMC version? Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
     * Alternatively, look for it in the sidebar under "server packs".
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
3. Drag the ZIP-archive to MultiMC window
4. Click that version, then `Minecraft Folder`
5. Click the previous version, then `Minecraft Folder`
6. Copy the important files and folders over:
   * `saves` for your local worlds
   * `resourcepacks`, if you use any (do not copy the _Mod Menu Helper_ though)
   * `screenshots`
   * `servers.dat` for your multiplayer servers
   * `options.txt`, if you want to keep your vanilla option changes
7. Close the folders and run the new version
8. If everything looks right, delete the old version

### MultiMC (auto-update)

1.17 needs Java 16+, 1.18 needs Java 17+. [Get Java](https://www.oracle.com/java/technologies/downloads/)

In most cases:

1. Run the existing version, wait for the progress bar to fill up
2. If you get asked to download a specific jar, it means I am not allowed to bundle it and you must add it manually:
   1. Copy its url to your browser
   2. Click Cancel Launch
   3. Click Download on the mod
   4. On MultiMC, right click on the instance -> View Mods
   5. Drag the downloaded mod into the mod list
   6. Click Launch
3. Check the version difference in the bottom right corner.

To update the Fabric Loader (if you get an error like "mod X needs fabric-loader x.y.z"):

1. Click the instance
2. Click `Edit Instance`
3. On Minecraft, select the Fabric Loader, click `Remove`
4. Click `Install Fabric`, click `OK`
5. `Close` the window, you can now play the game.

If there is a new Minecraft version or you are lazy to update your Fabric Loader:

1. Go to [readme](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads), click "Alternative downloads"
2. Click the version number you need in the MultiMC (auto-update) section
3. Drag the ZIP-archive to MultiMC window
4. Click that version, then `Minecraft Folder`
5. Click the previous version, then `Minecraft Folder`
6. Copy the important files and folders over:
   * `saves` for your local worlds
   * `resourcepacks`, if you use any (do not copy the _Mod Menu Helper_ though)
   * `screenshots`
   * `servers.dat` for your multiplayer servers
   * `options.txt`, if you want to keep your vanilla option changes
7. Close the folders and run the new version
8. If everything looks right, delete the old version

### GDLauncher

**You must update to v1.1.14 or later to play FO, see settings for which version you have. [Easiest way is to redownload](https://gdevs.io/#downloadContainer) (no need to remove first).** 

**Do NOT attempt to update FO on an older version of GDLauncher because it will delete your instance!**

1. Right click the _Fabulously Optimized_ instance
2. Select `🔧 Manage`
3. Select `Modpack` from the right
4. Click `Select a version` and choose the topmost option
5. Click `Switch Version`
6. Modpack will now update.
7. After updating you can run it and check the version difference in the bottom right corner.

### Minecraft Launcher (the vanilla)

Currently the only way to update is to "reinstall" the pack.

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.14.8**
2. Open Minecraft Launcher, click `Installations` and then click 📂 on the Fabric installation
3. Delete all files in `mods` folder
   * This is to ensure all mods will reflect the latest FO version. You can [add your custom mods back later](adding-more-mods.md).
4. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) on CurseForge
5. Click `Download` the latest **MultiMC version** of the pack
   * Don't see the MultiMC version? Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
      * Alternatively, look for it in the sidebar, under "server packs".
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
6. Open the zip file, go to _Fabulously Optimized x.x.x_ > _.minecraft_
7. Copy all folders from zip's .minecraft folder to your .minecraft folder; if asked - replace the files
8. If you want [FO default settings](changed-options.md) as well, delete `options.txt` (your vanilla options will be reset)
9. Launch the installed Fabric profile
10. If you now see "Fabulously Optimized" in the right bottom corner and its version number is newer than before, you're done!

### Resetting settings

Because the pack is using YOSBR, your vanilla options and most of the mod ones will not change when you upgrade, [despite what is stated in the changelog](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md). This is made so that you can upgrade without having to reconfigure your options all the time. However, at some point you may still want to do that in order to get the latest changes. So:

1. Open the modpack folder.
   * CurseForge Launcher: right click on the modpack tile -> `Open Folder`
   * MultiMC: right click on the instance -> `Minecraft Folder`
   * GDLauncher: right click on the instance -> `Open Folder`
   * Vanilla launcher: go to `Installations` tab -> hover on the instance -> click `📁`
2. Delete `options.txt` if you prefer (these are vanilla options - [see what the modpack changes](changed-options.md))
3. Open "config" and delete the following:
   * _fabric_ folder
   * other files, except for
     * _citresewn.json_
     * _fabric\_loader\_dependencies.json_
     * _yosbr_ folder
4. Launch the game and new options are applied.
