# Update instructions

### Disclaimers

- As with any update, *things may break*. Probably not due to the modpack itself, but maybe your launcher, your custom mods or your hard drive. If worried, make backups.
- Upgrades from stable to unstable (alpha, beta) versions are **never** supported (make a separate instance!), while updates from unstable versions to stable ones are.
- Any kind of instance downgrading is **never** supported. Make a separate old instance or [use something like ViaFabric](chat-reporting-faq.md#but-my-favorite-server-requires-1.19) if your server hasn't updated yet.
- If you follow these instructions properly, all custom mods and most mod settings you have will persist (except those that need to change). If you want, you can [reset your settings](#resetting-settings) to get the latest changes.

### CurseForge Launcher

If you haven't changed the mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, right click _Fabulously Optimized_, then `⇄ Change Version`
   * Don't see that option? Follow the other instructions below.
3. Select the topmost version, then `Continue`.
4. Modpack will now update.
5. Run it and check the version difference in the bottom right corner.

If you added or removed some mods:

1. Select _Minecraft_ from the grid or sidebar
2. On My Modpacks, click _Fabulously Optimized_
3. Click `⫶`→ `Profile Options`
4. Uncheck "Allow content management for this profile". You can re-enable content management after the update.
5. Click `Continue`
6. Click `⫶` → `⇄ Change Version`.
7. Select the topmost version, then `Continue`.
8. Modpack will now update.
9. Run it and check the version difference in the bottom right corner.

### Prism Launcher

1. Select existing FO instance
2. Click `Edit` on the sidebar
3. Select `Modrinth` on the tab list
4. Click `Update pack`
5. Once the name prompt comes up, click `Yes`

### MultiMC

1. Click `Add Instance`
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click `OK`
5. The modpack will now install.
6. Click that version you just created, then `Minecraft Folder`
7. Click the previous version, then `Minecraft Folder`
8. Copy the important files and folders over:
   * `saves` for your local worlds
   * `resourcepacks`, if you use any (do not copy old versions of FO-bundled packs though)
   * `screenshots`
   * `servers.dat` for your multiplayer servers
   * `options.txt`, if you want to keep your vanilla option changes
   * Ignore the `Copy all 3 folders!` file, that's for vanilla launcher users 
9. Close the folders and run the new version
10. If everything looks right, delete the old version

### MultiMC (auto-update)

In most cases:

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

If there is a new Minecraft version:

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

### Minecraft Launcher (vanilla)

Currently the only way to update is to "reinstall" the pack. Consider installing a different launcher for a smoother upgrade experience.

1. Download and install [Fabric Loader](https://fabricmc.net/use/) **version 0.14.19**
   * Older versions of the modpack - 1.12.3, 2.7.3 and 3.14.1 require the use of Fabric Loader 0.14.12 instead.
   * Remember that the _installer version_ doesn't matter, what matters is the _loader version_ that appears when you run the installer.
2. Open Minecraft Launcher, click `Installations` and then click 📂 on the Fabric installation
3. Delete all files in `mods` folder
   * This is to ensure all mods will reflect the latest FO version. You can [add your custom mods back later](adding-more-mods.md).
4. **For 4.8.0-4.9.x**: Download [this version of Sodium](https://modrinth.com/mod/sodium/version/mc1.19.4-0.4.10)
5. Go to [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) on CurseForge
6. Click the topmost version, scroll down to "Additional files" section
7. Click `⋮` → `Download file` on the latest **MultiMC version**
   * If you see 0-5 mods in the zip, you downloaded the wrong version.  
8. Open the zip file, go to _Fabulously Optimized x.x.x_ > _minecraft_
9. Copy **all folders** from zip's _minecraft_ folder to your _.minecraft_ folder; if asked - replace the files
10. **For 4.8.0-4.9.x**: Copy downloaded Sodium JAR to _mods_ folder
11. If you want [FO default settings](changed-options.md) as well, delete `options.txt` (your vanilla options will be reset)
12. Launch the installed Fabric profile
13. If you now see "Fabulously Optimized" in the right bottom corner and its version number is newer than before, you're done!

### Pojav Launcher (Android)

1. [Download Fabric installer](https://fabricmc.net/use/installer/) (Universal/.JAR)
2. [Download CurseForge GUI installer](https://github.com/Madis0/CurseForge-GUI/releases/download/694de8b/CurseForge-GUI-1.0-SNAPSHOT.jar)
3. Download Fabulously Optimized patches for Pojav Launcher: [1.19.4](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/Fabulously-Optimized/fabulously-optimized/tree/pojav/PojavLauncher/1.19.4)
4. Run Pojav Launcher
5. Tap `Install .jar` → select `fabric-installer-x.x.x.jar`. You'll see the Fabric installer with some logs.
11. Tap `❌` to close the logs, then `Install` → `OK` → `⛝`
12. Tap `Install .jar` → select `CurseForge-GUI-1.0-SNAPSHOT.jar`. You'll see a different kind of installer with some logs.
13. Tap `❌` to close the logs, then `Install modpack` → `KEYBOARD`
14. Enter the following code, according to the version you prefer. The keyboard may cover your screen, but try to get it right regardless.
    * **Latest for 1.19.4**: enter `396246`.
    * **3.14.1 for 1.18.2**: enter `396246_3983420`.
    * **2.7.3 for 1.17.1**: enter `396246_3667614`.
    * **1.12.3 for 1.16.5**: enter `396246_3667608`.
15. Press Enter on the keyboard and wait for the install to complete. Once installed, press `OK` → `⛝`
    * If you failed to enter the correct code, just close and try again from step 12.
16. Close Pojav and open Files.
17. Tap `☰` → `Downloads` → `(Minecraft version).zip` or `DownGit.zip` → `(Minecraft version)`
18. Hold down on `config` folder and tap on both items, then tap `⋮` → `Extract to...`
19. Tap `☰` → `PojavLauncher` → `curseforge-cli` → `modpack` → `fabulously-optimized_396246` → `EXTRACT`
20. Tap `☰` → `PojavLauncher` → `curseforge-cli` → `modpack` → `fabulously-optimized_396246` → `config (2)`
21. Hold on any file and select the other one
21. Tap `⋮` → `Move to...` → `☰` → `PojavLauncher` → `curseforge-cli` → `modpack` → `fabulously-optimized_396246` → `config`
22. Press `fabulously-optimized_396246` on the "address bar"
23. Hold down on `config (2)` → tap `🗑️` → `OK`
24. Launch Pojav, tap `New - Latest Release` → `Fabulously Optimized - ...` → `Play`.
25. Fabulously Optimized should now be running! 

### GDLauncher

No longer supported. [Please migrate to Prism Launcher.](install-instructions.md#gdlauncher)

### Updating mods

* If you are using a supported version of Fabulously Optimized and you haven't added any extra mods, **do not update any mods manually**, just update the modpack instead.
   * If you did add extra mods, **update those individually** after you've ensured you're on latest version of Fabulously Optimized.
   * Updating mods that are in FO may cause unexpected issues which FO releases would prevent, so manual updates only make your own life harder.
* If you are using an unsupported (legacy) version of Fabulously Optimized, **you may carefully update the mods**.
   * Keep in mind that we haven't tested those updates, so you may run into issues and need to revert back to previous versions.
* Some launchers have options to update all mods at once. **Do not use this feature** for reasons listed above.
    * Even for legacy versions of FO, updating everything at once like that may cause problems like mod loader mismatch, Minecraft version mismatch, mod platform variances (more recent version on one platform vs another) and so on.
    * It is always safer to update each mod individually so that you can see the update was successful and valid for your MC version/mod loader.
* If you did any of the things above and are having issues, simply update Fabulously Optimized again, even if you have the same version.

### Resetting settings

Because the pack is using YOSBR, your vanilla options and most of the mod ones will not change when you upgrade, [despite what is stated in the changelog](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/CHANGELOG.md). This is made so that you can upgrade without having to reconfigure your options all the time. 

However, at some point you may still want to do that in order to get the latest changes. So:

1. Open the modpack folder
   * CurseForge Launcher: right click on the modpack tile → `Open Folder`
   * Prism Launcher: right click on the instance → `Folder` → `.minecraft`
   * MultiMC: right click on the instance → `Minecraft Folder`
   * Vanilla launcher: go to `Installations` tab → hover on the instance → click `📁`
2. Delete the `config` folder
   * If you prefer, also delete `options.txt` which stores vanilla options
3. Download [your version of FO again from Modrinth](https://modrinth.com/modpack/fabulously-optimized/versions)
4. Rename the file to `pack.zip`
5. Open the file you renamed, go to `overrides`
6. Copy/extract the folder `configs` out to the modpack folder you previously opened
   * You may delete the `pack.zip` after you're done
7. Launch the game. Modpack's defaults are now applied!
