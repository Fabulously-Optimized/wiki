# Update instructions

### Disclaimers

- As with any update, *things may break*. Probably not due to the modpack itself, but maybe your launcher, your custom mods or your hard drive. If worried, make backups.
- Upgrades from stable to unstable (alpha, beta) versions are **never** supported (make a separate instance!), while updates from unstable versions to stable ones are.
- Any kind of instance downgrading is **never** supported. Make a separate old instance or [use something like ViaFabric](chat-reporting-faq.md#but-my-favorite-server-requires-1.19) if your server hasn't updated yet.
- If you follow these instructions properly, all custom mods and most mod settings you have will persist (except those that need to change). If you want, you can [reset your settings](#resetting-settings) to get the latest changes.

### CurseForge Launcher

#### If you haven't changed the mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, right click _Fabulously Optimized_, then `⇄ Change Version`
   * Don't see that option? Follow the other instructions below.
3. Select the topmost version, then `Continue`.
4. Modpack will now update.
5. After updating you can run it and check the version difference in the bottom right corner.

#### If you added or removed some mods:

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

1. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Click `Download` on the latest **MultiMC version**
   * On CurseForge's new UI, `⌵` → `Download file`
   * Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
     * Alternatively, look for it in the sidebar under "server packs".
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
3. Drag the ZIP-archive to MultiMC window, and hit OK in the window that pops up.
4. Click that version you just created, then `Minecraft Folder`
5. Click the previous version, then `Minecraft Folder`
6. Copy the important files and folders over:
   * `saves` for your local worlds
   * `resourcepacks`, if you use any (do not copy the _Mod Menu Helper_ though)
   * `screenshots`
   * `servers.dat` for your multiplayer servers
   * `options.txt`, if you want to keep your vanilla option changes
   * Ignore the `Copy all 3 folders!` file, that's for vanilla launcher users 
7. Close the folders and run the new version
8. If everything looks right, delete the old version

### MultiMC (auto-update)

#### In most cases:

1. Run the existing version, wait for the progress bar to fill up
   * If you get a popup "This modpack uses new versions of the following...", just click `Update`.
       <details>
          <summary>Need to download some mods manually?</summary>
          If you get asked to download a specific jar, it means I am not allowed to bundle it and you must add it manually:

        1. Copy and paste the given address to your browser
        2. Click `Cancel Launch`
        3. Click `Download` on the mod
        4. On MultiMC, click on the instance, then click `View Mods`
        5. Drag the downloaded mod into the mod list
        6. Click `Launch`
  
      </details>
2. Check the version difference in the bottom right corner.

#### If there is a new Minecraft version:

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
   * Ignore the `Copy all 3 folders!` file, that's for vanilla launcher users 
7. Close the folders and run the new version
8. If everything looks right, delete the old version

### Prism Launcher

1. Select existing FO instance
2. Click `Edit` on the sidebar
3. Select `Modrinth` on the tab list
4. Click `Update pack`
5. Once the name prompt comes up, click `Yes`

### Steam Deck

See [Prism Launcher](#prism-launcher).

### GDLauncher

1. Right click the _Fabulously Optimized_ instance
2. Select `🔧 Manage`
3. Select `Modpack` from the right
4. Click `Select a version` and choose the topmost option
5. Click `Switch Version`
6. Modpack will now update.
7. After updating you can run it and check the version difference in the bottom right corner.

### Minecraft Launcher (vanilla)

Currently the only way to update is to "reinstall" the pack. Consider installing a different launcher for a smoother upgrade experience.

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.14.18**
   * Older versions of the modpack - 1.12.3, 2.7.3 and 3.14.1 require the use of Fabric Loader 0.14.12 instead.
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations` and then click 📂 on the Fabric installation
3. Delete all files in `mods` folder
   * This is to ensure all mods will reflect the latest FO version. You can [add your custom mods back later](adding-more-mods.md).
4. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) on CurseForge
5. Click `Download` the latest **MultiMC version** of the pack
   * On CurseForge's new UI, `⌵` → `Download file`
   * Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
      * Alternatively, look for it in the sidebar, under "server packs".
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
6. Open the zip file, go to _Fabulously Optimized x.x.x_ > _.minecraft_
7. Copy **all folders** from zip's .minecraft folder to your .minecraft folder; if asked - replace the files
8. If you want [FO default settings](changed-options.md) as well, delete `options.txt` (your vanilla options will be reset)
9. Launch the installed Fabric profile
10. If you now see "Fabulously Optimized" in the right bottom corner and its version number is newer than before, you're done!

### Pojav Launcher (Android)

1. [Download Fabric installer](https://fabricmc.net/use/installer/) (Universal/.JAR)
2. [Download the latest **MultiMC version** of Fabulously Optimized](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
   * On CurseForge's new UI, `⌵` → `Download file`
   * Click the title of the CurseForge version you need and scroll down, you'll find the MultiMC variant there.
      * Alternatively, look for it in the sidebar, under "server packs". Don't worry, these are not server packs, just marked as such for findability.
   * If you don't see any mods inside the zip or only see one, you downloaded the wrong version.
3. Download Fabulously Optimized patches for Pojav Launcher: [1.19.3](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/Fabulously-Optimized/fabulously-optimized/tree/pojav/PojavLauncher/1.19.3)
4. Run Pojav Launcher
5. Tap `Install .jar` → select `fabric-installer-x.x.x.jar`. You'll see the Fabric installer with some logs.
6. Tap `❌` to close the logs, then `Install` → `OK` → `⛝`
7. Close Pojav and open Files.
8. Tap `☰` → `PojavLauncher` → hold down on `mods`, tap `🗑️` → `OK`
9. Tap `☰` → `Downloads` → `Fabulously+Optimized+x.x.x.zip` → `Fabulously Optimized x.x.x` → `minecraft`
10. Hold down on one folder and tap on all three folders, then tap `⋮` → `Extract to...`
11. Tap `☰` → `PojavLauncher` → `⋮` → `Show hidden files` → `.minecraft` → `EXTRACT`
12. Tap `☰` → `Downloads` → `DownGit.zip` → `(Minecraft version)`
    * Can't see .minecraft? Tap `⋮` → `Show hidden files` 
13. Hold down on `config` folder and tap on both items, then tap `⋮` → `Extract to...`
14. Tap `☰` → `PojavLauncher` → `.minecraft` → `EXTRACT`
15. Tap `☰` → `PojavLauncher` → `.minecraft` 
16. On each duplicated folder (e.g. "config (2)" or "resourcepacks (2)"), do the following:
     1. Open the folder
     2. Hold on any file and select all
     3. Tap `⋮` → `Move to...` → `☰` → `PojavLauncher` → `.minecraft` → (the original folder, e.g. "config" or "resourcepacks")
          * Can't see .minecraft? Tap `⋮` → `Show hidden files` 
     4. Repeat until all files are transferred
     5. Delete the duplicate folders
17. Launch Pojav, make sure `fabric-loader-x.x.x` is selected, `Play`.
18. Fabulously Optimized should now be running! 

### Resetting settings

Because the pack is using YOSBR, your vanilla options and most of the mod ones will not change when you upgrade, [despite what is stated in the changelog](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md). This is made so that you can upgrade without having to reconfigure your options all the time. 

However, at some point you may still want to do that in order to get the latest changes. So:

1. Open the modpack folder
   * CurseForge Launcher: right click on the modpack tile → `Open Folder`
   * MultiMC: right click on the instance → `Minecraft Folder`
   * Prism Launcher: right click on the instance → `Folder` → `.minecraft`
   * GDLauncher: right click on the instance → `Open Folder`
   * Vanilla launcher: go to `Installations` tab → hover on the instance → click `📁`
2. Delete the `config` folder
   * If you prefer, also delete `options.txt` which stores vanilla options
3. Download [your version of FO again from Modrinth](https://modrinth.com/modpack/fabulously-optimized/versions)
4. Rename the file to `pack.zip`
5. Open the file you renamed, go to `overrides`
6. Copy/extract the folder `configs` out to the modpack folder you previously opened
   * You may delete the `pack.zip` after you're done
7. Launch the game. Modpack's defaults are now applied!
